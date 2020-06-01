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

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.superloader = SuperLoader()
        self.superloader.load("dayone")
        self.player = Player()
        
        #Smid ind i en funktion
        self.taskMgr.add(self.player.control_task, "ControlTask")
        self.taskMgr.add(self.player.check_ray_collision, "RayTask")

        self.setFrameRateMeter(settings.show_fps)
        self.crosshair = OnscreenText(text='+', pos=(0,0), scale=(0.1), fg=(0,0.5,0,0.8))

        
        self.audio3d = Audio3DManager.Audio3DManager(self.sfxManagerList[0], self.player.camera)
        self.audio3d.attachListener(self.player.camera)
        self.pos_seq = Sequence()
        self.hpr_seq = Sequence()

        

    #    z = self.load_sound('duga.ogg', self.door, 1) Maybe set audio as a parameter on model class.
     #   z.play()
        
              
    def cutscene(self, points):

        self.pos_seq = Sequence()
        self.hpr_seq = Sequence()
        h,p,r = self.camera.get_hpr()
        x,y,z = self.player.body.get_pos()
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
            
<<<<<<< HEAD
            pos_seq.append(LerpPosInterval(self.player.body, d, (x,y,z), blendType=b))
            hpr_seq.append(LerpHprInterval(self.camera, d, (h,p,r), blendType=b))
=======
            self.pos_seq.append(LerpPosInterval(self.player.body, d, (x,y,z), blendType=b))
            self.hpr_seq.append(LerpHprInterval(self.camera, d, (h,p,r), blendType=b))
>>>>>>> f5e97686b4dc7f71aa9fe39ff61fef7e12925388
        

        self.pos_seq.start()
        self.hpr_seq.start()

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
