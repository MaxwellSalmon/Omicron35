from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject, Audio3DManager
from panda3d.core import *
from direct.task import Task
from math import sin, cos, radians, floor, ceil
import math
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import *

from superloader import *
import settings


#Setting up a function that should run when an object is interacted with:
#Simply execute a function with no parameters:
#   object_functions[str(object)] = object_function
#Execute a function with parameters:
#   object_functions[str(object)] = [object_function, {'a':1, 'b':2, 'c':3}]

#Loading models the fast way
#Models can be loaded by using the load_model function. It needs a path or simply just the name of the file.
#It can also take keyword arguments being the following:
#parent = node path
#scale = float
#pos = tuple 3
#hpr = tuple 3
#tag = string
#function = object_function

#Creating cutscenes:
#self.cutscene([self, [{point},{point},{point}]])
#Points are dictionaries with following keys:
#x, y, z = world coordinates
#h, p, r = object rotation
#d = duration
#b = blend mode - 'easeIn', 'easeOut', 'noBlend', default is 'easeInOut'
#Note, that the player's p value can only be between -90 and 90.

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        superload = SuperLoader()
        
        self.taskMgr.add(self.player_control_task, "ControlTask")
        self.taskMgr.add(self.check_ray_collision, "RayTask")

        self.speed = 0.08
        self.forward_btn = KeyboardButton.ascii_key('w')
        self.backward_btn = KeyboardButton.ascii_key('s')
        self.strafe_right_btn = KeyboardButton.ascii_key('d')
        self.strafe_left_btn = KeyboardButton.ascii_key('a')
        self.free_mouse = False
        self.control_mouse()

        self.setFrameRateMeter(True)
        self.crosshair = OnscreenText(text='+', pos=(0,0), scale=(0.1), fg=(0,0.5,0,0.8))

        
        self.audio3d = Audio3DManager.Audio3DManager(self.sfxManagerList[0], self.camera)
        self.audio3d.attachListener(self.camera)

        

    #    z = self.load_sound('duga.ogg', self.door, 1) Maybe set audio as a parameter on model class.
     #   z.play()
        



    def check_ray_collision(self, task):
        if settings.variables['picked_obj']:
            settings.variables['picked_obj'].clear_color()
            self.accept("mouse1", self.click_mouse, [settings.variables['picked_obj']])
            settings.variables['picked_obj'] = None
        else:
            self.ignore("mouse1")
            
        #Set ray from center of screen (0,0)
        self.pickerRay.setFromLens(self.camNode, 0,0)

        self.cTrav.traverse(self.render)
        #Get all objects that are collinding with the ray.
        if self.queue.getNumEntries() > 0:
            #Sort by distance.
            self.queue.sortEntries()
            pickedObj = self.queue.getEntry(0).getIntoNodePath()
            pickedObj = pickedObj.findNetTag('interactive')
            if not pickedObj.isEmpty():
                dist = self.queue.getEntry(0).getSurfacePoint(self.camera).lengthSquared()
                if dist <= 10:
                    pickedObj.set_color(1,1,0)
                    settings.variables['picked_obj'] = pickedObj
                
        return Task.cont

    def click_mouse(self, obj):
        s = str(obj)
        if s not in self.object_functions:
            print(f"'{s}' is not a keyword!")
            return
        else:
            v = self.object_functions[s]

        if callable(v):
            #If v just a function?
            v()
        elif type(v) is list:
            #It is a list with v and parameters.
            v[0](**v[1])
        
            
    def player_control_task(self, task):
        old_pos = self.player.getPos()
        new_pos = old_pos
        add_pos = [0,0,0]
        is_down = self.mouseWatcherNode.is_button_down

        h = radians(self.camera.getH())
        add_pos = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        if is_down(self.forward_btn):
            add_pos[0] = [-sin(h)*self.speed,cos(h)*self.speed,0]
        if is_down(self.backward_btn):
            add_pos[1] = [-sin(h)*-self.speed,cos(h)*-self.speed,0]
        if is_down(self.strafe_right_btn):
            add_pos[2] = [cos(h)*self.speed,sin(h)*self.speed,0]
        if is_down(self.strafe_left_btn):
            add_pos[3] = [cos(h)*-self.speed,sin(h)*-self.speed,0]

        move_pos = [0,0,0]
        for i in add_pos:
            move_pos[0] += i[0]
            move_pos[1] += i[1]
            move_pos[2] += i[2]

        new_pos[0] = old_pos[0] + move_pos[0]
        new_pos[1] = old_pos[1] + move_pos[1]
        new_pos[2] = old_pos[2] + move_pos[2]
        self.player.setPos(new_pos)

        mpos = [0,0]
        if not self.free_mouse:
            mpos = self.control_mouse()

        self.fps_camera(mpos)
            
        return Task.cont

    def control_mouse(self):
        #Siden relative mouse ikke virker med Windows, gøres det manuelt.
        md = self.win.getPointer(0)
        x, y = md.get_x(), md.get_y()
        props = self.win.getProperties()
        
        #Flyt musemarkør til midten af skærmen.
        center = [int(props.getXSize() / 2), int(props.getYSize() / 2)]
        if self.win.movePointer(0, center[0], center[1]):
            return [x-center[0], center[1]-y]
        return [0,0]

    def fps_camera(self, mpos):
        x, y = mpos
        hpr = self.camera.getHpr()
        h = hpr[0] - x * settings.variables['sensitivity']
        p = hpr[1] + y * settings.variables['sensitivity']
        r = hpr[2]

        if h > 360:
            h -= 360
        elif h < 0:
            h += 360
        if p > 90:
            p = 90
        elif p < -90:
            p = -90
        if r > 360:
            r -= 360
        elif r < 0:
            r += 360
        
        self.camera.set_h(h)
        self.camera.set_p(p)
            
    def cutscene(self, points):

        pos_seq = Sequence()
        hpr_seq = Sequence()
        h,p,r = self.camera.get_hpr()
        x,y,z = self.player.get_pos()
        for point in points:
            d = 1
            b = 'easeInOut'

            if 'h' in point:
                h = point['h']
            if 'p' in point:
                p = point['p']
            if 'r' in point:
                r = point['r']
            if 'x' in point:
                x = point['x']
            if 'y' in point:
                y = point['y']
            if 'z' in point:
                z = point['z']
            if 'd' in point:
                d = point['d']
            if 'b' in point:
                b = point['b']
            
            pos_seq.append(LerpPosInterval(self.player, d, (x,y,z), blendType=b))
            hpr_seq.append(LerpHprInterval(self.camera, d, (h,p,r), blendType=b))
        

        pos_seq.start()
        hpr_seq.start()

    def load_sound(self, path, obj, *args):
        #Args[0] is dropoff factor
        if 'sounds/' not in path:
            path = 'sounds/'+path
        
        sound = self.audio3d.loadSfx(path)
        if str(sound)[:14] == 'NullAudioSound':
            print(f"Audio file {path} is not found")
        
        self.audio3d.attachSoundToObject(sound, obj)

        if args:
            self.audio3d.setDropOffFactor(args[0])
        
        return sound
        
        
        

            
class FreeMouse(DirectObject.DirectObject):

    def __init__(self):
        self.accept('escape', self.free_mouse)
        self.accept('g', self.move_camera)

    def free_mouse(self):
        app.free_mouse = not app.free_mouse
        props = WindowProperties()
        props.setCursorHidden(not app.free_mouse)
        app.win.requestProperties(props)

    def move_camera(self):
        app.camera.setHpr(0,0,0)
        
        
app = MyApp()
m = FreeMouse()
app.run()
