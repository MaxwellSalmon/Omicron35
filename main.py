from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject, Audio3DManager
from panda3d.core import *
from direct.task import Task
import math, threading
from direct.interval.IntervalGlobal import *
from direct.filter.CommonFilters import CommonFilters #temp?

import scene_setup, manager, weather, text, voice_strings, conversation_gui
import model, console, conversation_flow
from superloader import *
from player import *
import settings

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        base.free_mouse()
        self.console = console.Console()

        self.weather = weather.Weather()
        self.interactive_objects = render.attachNewNode("interactive_objects")
        self.triggers = render.attachNewNode("triggers")
        self.text = text.Text()
        self.superloader = SuperLoader()
        self.superloader.load(settings.environment, True)
        self.player = Player()
        self.superloader.load_audio3d()
        self.superloader.start_ambience() #Was commented out?
        self.default_model = Model('dev/sphere.egg', name='default')
        conversation_flow.initialise_states()
        #base.scene.flattenStrong()
        
        self.taskMgr.add(self.player.control_task, "ControlTask")
        self.taskMgr.doMethodLater(0.05, self.player.check_ray_collision, "RayTask")
        self.taskMgr.doMethodLater(0.3, manager.manage, "ManageTask")

        self.setFrameRateMeter(settings.show_fps)

        self.pos_seq = Sequence()
        self.hpr_seq = Sequence()

        self.conv_gui = conversation_gui.ConversationGUI(3)
        
  #      self.gui.update_text(('Report measurements', 'What is your name?', 'Mein Vater war ein sehr betümte Spurhhund'))
  #      self.gui.toggle_visibility()

  #      filters = CommonFilters(base.win, base.cam)
 #      filters.setBloom()

        #z = self.load_sound('piano.mp3', self.scene, 1)
        #z.play()
        PStatClient.connect()
      #  font1 = loader.loadFont('models/font.egg')
     #   font1.setPixelsPerUnit(60)
#        string = 'my text string and it gets longer and longer and you know it and we will see how long it can get here'
 #       textObject = OnscreenText(text=string, pos=(0, -0.8), scale=0.07, align=TextNode.ACenter,
 #                                 wordwrap=30, fg=(255,255,255,1), shadow=(0,0,0,0.8), mayChange=True)
    def free_mouse(self):
        settings.free_mouse = not settings.free_mouse
        props = WindowProperties()
        props.setCursorHidden(not settings.free_mouse)
        self.win.requestProperties(props)

        #Move curser to center of screen when turning off
              
    def cutscene(self, points):
        if settings.constraints != [None, None]:
            self.camera.set_h(self.camera.get_h()-360)
            settings.constraints = [None, None]
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
        self.accept('escape', app.free_mouse)
        self.accept(settings.console_btn, base.console.open_console)

        if settings.dev_control:
            self.accept(settings.fov_up_dwn[0], self.add_fov, [-10])
            self.accept(settings.fov_up_dwn[1], self.add_fov, [10])

    def add_fov(self, added):
        if settings.console_open:
            return
        settings.fov += added
        base.player.camLens.setFov(settings.fov)


    def move_camera(self):
        app.camera.setHpr(0,0,0)
        
        
app = MyApp()
m = FreeMouse()
app.run()
