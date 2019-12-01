from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject, Audio3DManager
from panda3d.core import *
from direct.task import Task
from math import sin, cos, radians, floor, ceil
import math
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import *

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

        self.object_functions = {}
        self.variables = {'clothes_on' : False,
                          'environment' : 'inside',
                          'sensitivity' : 0.21,
                          'picked_obj' : None,
                          }
        
        self.load_scene()
        self.load_mouse()
        self.load_camera()
        self.load_light()
        self.load_collision()
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

        

        z = self.load_sound('duga.ogg', self.door, 1)
        z.play()
        

    def load_scene(self):
        self.scene = self.loader.loadModel("models/interior.egg")
        self.scene.setDepthOffset(1)
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.5)
        self.scene.setPos(0,0,-1.8)
        
        self.outside = self.loader.loadModel("models/exterior.egg")
        self.outside.setDepthOffset(1)
        self.outside.setScale(0.5)
        self.outside.setPos(-3,0,-1.8)
        

       # mat = Material()
       # mat.setAmbient((1,1,1,1))
       # self.scene.setMaterial(mat)

        self.door = self.load_model('door', parent=self.render, tag='interactive', function=self.door_function,
                                    pos=(10,1.35,0.4), scale=0.5, solid=True)
        self.clothes = self.load_model('clothes', parent=self.scene, tag='interactive',
                                       function=[self.put_on_clothes, {'test' : 'Her er en string'}])

    def load_model(self, path, **kwargs):
        kg = kwargs.get

        if 'models/' not in path:
            path = 'models/'+path
        model = self.loader.load_model(path)
        name = path[7:]
        
        if kg('parent'):
            model.reparent_to(kg('parent'))
        else:
            model.reparent_to(self.render)
        if kg('pos'):
            p = kg('pos')
            model.set_pos(p[0], p[1], p[2])
        if kg('hpr'):
            hpr = kg('hpr')
            model.set_hpr(hpr[0], hpr[1], hpr[2])
        if kg('tag'):
            model.set_tag(kg('tag'), '1')
        if kg('scale'):
            model.set_scale(kg('scale'))
        if kg('function'):
            self.object_functions[str(model)] = kg('function')
        if kg('solid'):
            bmin, bmax = model.get_tight_bounds()
            bounds = bmax-bmin
            col = model.attachNewNode(CollisionNode(name))
            col.node().add_solid(CollisionBox((0,0,0), bounds[0], bounds[1], bounds[2]))
            model.show_tight_bounds()
            col.show()
        return model

    def door_function(self):
        if self.variables['clothes_on']:
            if self.variables['environment'] == "inside":
                self.outside.reparentTo(self.render)
                self.scene.detachNode()
                self.variables['environment'] = "outside"
                self.door.setPos(6.5,1.2,0.4)
            else:
                self.outside.detachNode()
                self.scene.reparentTo(self.render)
                self.variables['environment'] = "inside"
                self.door.setX(0)
        else:
            print("Jeg skal have tøj på først")

    def put_on_clothes(self, test):
        self.variables['clothes_on'] = True
        self.clothes.set_z(10)
        print("Jeg har taget tøjet på")
        print(test)

        self.cutscene([{'h':0,'p':90,'r':0, 'x':-0.36, 'y':-11.36, 'z':-1.5, 'd':0},
                        {'p':0, 'y':-11,'z':-1, 'd':2},
                        {'h':85, 'p':-5, 'y':-10.5, 'd':2},
                        {'x':-2.3, 'p':-8, 'z':0, 'd':2}])
        


        
    def load_camera(self):
        self.player = render.attachNewNode("player node")
        self.camera.reparentTo(self.player)
        self.camera.setPos(0,3,2)
        self.camLens.setFov(80)
        self.camLens.setNear(0.2)

    def load_collision(self):
        self.cTrav = CollisionTraverser()
        self.pusher = CollisionHandlerPusher()
        self.queue = CollisionHandlerQueue()

        #Camera
        pickerNode = CollisionNode('mouseRay')
        pickerNP = self.camera.attachNewNode(pickerNode)
        pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.pickerRay = CollisionRay()
        pickerNode.addSolid(self.pickerRay)
        self.cTrav.addCollider(pickerNP, self.queue)

        #Player
        self.player_col = self.player.attachNewNode(CollisionNode('cnode'))
        self.player_col.node().addSolid(CollisionSphere(0,3,0,0.4))

        self.player_col.show()

        self.pusher.setHorizontal(True)
        self.cTrav.addCollider(self.player_col, self.pusher)
        self.pusher.addCollider(self.player_col, self.player)

        #Eksempler
        #Skab
##        skab = self.skab.attachNewNode(CollisionNode('skab'))
##        skab.node().addSolid(CollisionSphere(0,0,0.1,0.15))
##
##        #Lampe
##        lampe = self.lampe.attachNewNode(CollisionNode('lampe'))
##        lampe.node().addSolid(CollisionSphere(0,0,0.1,0.2))

    
    
    def load_light(self):
        #Nødvendig for skygger og sådan.
        render.setShaderAuto()
        self.light = render.attachNewNode(DirectionalLight("dlight"))
        dlight = render.attachNewNode(DirectionalLight("dlight2"))
        dlight.setH(317)
        dlight.node().setColor((0.1, 0.1, 0.1, 1))
        lens = OrthographicLens()
        lens.setFov(45)
        lens.setNearFar(7.5, 20)
        lens.setFilmSize(12)
        self.light.node().setLens(lens)
        self.light.node().setShadowCaster(True, 1024, 1024)
        ambient_light = render.attachNewNode(AmbientLight("alight"))
        ambient_light.node().setColor((0.7, 0.7, 0.7, 1))
        self.light.lookAt(self.scene)
        render.setLight(self.light)
        render.setLight(ambient_light)
        render.setLight(dlight)

    def load_mouse(self):
        self.disableMouse()
        props = WindowProperties()
        props.setCursorHidden(True)
        self.win.requestProperties(props)

    def check_ray_collision(self, task):
        if self.variables['picked_obj']:
            self.variables['picked_obj'].clear_color()
            self.accept("mouse1", self.click_mouse, [self.variables['picked_obj']])
            self.variables['picked_obj'] = None
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
                    self.variables['picked_obj'] = pickedObj
                
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
        h = hpr[0] - x * self.variables['sensitivity']
        p = hpr[1] + y * self.variables['sensitivity']
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
