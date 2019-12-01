from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject, Audio3DManager
from panda3d.core import *
from direct.task import Task
import math
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import *

from superloader import *
from player import *
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

        self.superload = SuperLoader()
        self.player = Player()
        
        #Smid ind i en funktion
        self.taskMgr.add(self.player.control_task, "ControlTask")
        self.taskMgr.add(self.player.check_ray_collision, "RayTask")

        self.setFrameRateMeter(settings.show_fps)
        self.crosshair = OnscreenText(text='+', pos=(0,0), scale=(0.1), fg=(0,0.5,0,0.8))

        
        self.audio3d = Audio3DManager.Audio3DManager(self.sfxManagerList[0], self.player.camera)
        self.audio3d.attachListener(self.player.camera)

        

    #    z = self.load_sound('duga.ogg', self.door, 1) Maybe set audio as a parameter on model class.
     #   z.play()
        
              
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

    def load_sound(self, path, obj, *args): #Smid over i superloader
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
        settings.free_mouse = not settings.free_mouse
        props = WindowProperties()
        props.setCursorHidden(not settings.free_mouse)
        app.win.requestProperties(props)

    def move_camera(self):
        app.camera.setHpr(0,0,0)
        
        
app = MyApp()
m = FreeMouse()
app.run()
