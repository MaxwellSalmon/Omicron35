from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject, Audio3DManager
from panda3d.core import *
from direct.task import Task
import math
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import *

from direct.particles.ParticleEffect import ParticleEffect #Temp?

import scene_setup, manager
from superloader import *
from player import *
import settings

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.interactive_objects = render.attachNewNode("interactive_objects")
        self.superloader = SuperLoader()
        self.superloader.load(settings.environment, True)
        self.player = Player()
        self.superloader.load_audio3d()
        base.scene.flattenStrong()
        
        self.taskMgr.add(self.player.control_task, "ControlTask")
        self.taskMgr.doMethodLater(0.05, self.player.check_ray_collision, "RayTask")
        self.taskMgr.doMethodLater(0.3, manager.manage, "ManageTask")

        self.setFrameRateMeter(settings.show_fps)
        #self.crosshair = OnscreenText(text='+', pos=(0,0), scale=(0.1), fg=(0,0.5,0,0.8))

        self.pos_seq = Sequence()
        self.hpr_seq = Sequence()


        self.enableParticles() #Make better

##        self.p = ParticleEffect()
##        self.p.loadConfig('particles/heavy_snow.ptf')
##        self.p.start(parent=render, renderParent=render)
##        self.taskMgr.add(self.temp, "temp")

        #z = self.load_sound('piano.mp3', self.scene, 1)
        #z.play()

       # PStatClient.connect()

    def temp(self, task):
        self.p.set_pos(self.player.body.get_pos())
        self.p.set_z(8)
        return Task.cont
        
              
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

            if settings.dev_control:
                d=0

            self.pos_seq.append(LerpPosInterval(self.player.body, d, (x,y,z), blendType=b))
            self.hpr_seq.append(LerpHprInterval(self.camera, d, (h,p,r), blendType=b))
        

        self.pos_seq.start()
        self.hpr_seq.start()

            
class FreeMouse(DirectObject.DirectObject):

    def __init__(self):
        self.accept('escape', self.free_mouse)
        self.accept('g', self.move_camera)
        
        if settings.dev_control:
            self.accept(settings.fov_up_dwn[0], self.add_fov, [-10])
            self.accept(settings.fov_up_dwn[1], self.add_fov, [10])

    def add_fov(self, added):
        settings.fov += added
        base.player.camLens.setFov(settings.fov)

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
