from math import radians, sin, cos
from direct.showbase import DirectObject
from direct.gui.OnscreenImage import OnscreenImage
from direct.task import Task
from panda3d.core import (
    CollisionNode,
    CollisionCapsule,
    TransparencyAttrib,
    )


import settings, clipboard_ui


class Player(DirectObject.DirectObject):

    def __init__(self):
        self.body = render.attachNewNode("player")
        self.camera = base.camera
        self.camLens = base.camLens
        self.camera.reparent_to(self.body)
        self.camera.set_pos(0,3,2)
        self.camLens.setFov(settings.fov)
        self.camLens.setNear(0.2)
        pos = settings.scenes[settings.environment].player_position
        self.body.set_pos(pos[0], pos[1], pos[2])

        self.speed = settings.player_speed
        self.load_collision()

        self.clipboard = clipboard_ui.ClipboardUI()

        self.hand_ui = None
        self.ring_ui = None
        self.crosshair = ':-)'
        
    def load_collision(self):
        self.col = self.body.attachNewNode(CollisionNode('cnode'))
        self.col.node().addSolid(CollisionCapsule(0,3,-1,0,3,2,0.5))
        # Why is 0,0,0 not center of player??
        base.pusher.setHorizontal(True)
        if not settings.noclip:
            base.cTrav.addCollider(self.col, base.pusher)
            base.pusher.addCollider(self.col, self.body)

    def control_task(self, task):
        settings.dt = globalClock.getDt()

        #Do not allow movement during cutscenes or constrained scenes
        if self.check_cutscene():
            return Task.cont
        if self.check_constraint():
            return Task.cont
        if settings.ui_open:
            return Task.cont
        
        old_pos = self.body.getPos()
        new_pos = old_pos
        add_pos = [0,0,0]
        is_down = base.mouseWatcherNode.is_button_down

        h = radians(self.camera.getH())
        add_pos = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        
        speed = self.speed * settings.dt

        if settings.noclip:
            if is_down(settings.fly_up_dwn[0]):
                add_pos[4] = [0,0,speed]
            elif is_down(settings.fly_up_dwn[1]):
                add_pos[4] = [0,0,-speed]

        if is_down(settings.forward_btn):
            add_pos[0] = [-sin(h)*speed,cos(h)*speed,0]
        if is_down(settings.backward_btn):
            add_pos[1] = [-sin(h)*-speed,cos(h)*-speed,0]
        if is_down(settings.strafe_right_btn):
            add_pos[2] = [cos(h)*speed,sin(h)*speed,0]
        if is_down(settings.strafe_left_btn):
            add_pos[3] = [cos(h)*-speed,sin(h)*-speed,0]

        move_pos = [0,0,0]
        for i in add_pos:
            move_pos[0] += i[0]
            move_pos[1] += i[1]
            move_pos[2] += i[2]


        new_pos[0] = old_pos[0] + move_pos[0]
        new_pos[1] = old_pos[1] + move_pos[1]
        new_pos[2] = old_pos[2] + move_pos[2]
        self.body.setPos(new_pos)

        mpos = [0,0]
        if not settings.free_mouse:
            mpos = self.control_mouse()

        self.fps_camera(mpos)

        base.accept(settings.inventory_btn, self.clipboard.open_ui)
        base.accept(settings.sprint_btn, self.speed_multiplier)
        

        return Task.cont

    def speed_multiplier(self):
        if settings.dev_control:
            if self.speed == settings.player_speed:
                self.speed = settings.player_speed * 3
            else:
                self.speed = settings.player_speed

    def show_crosshair(self):
        if settings.picked_obj:
            if self.crosshair != 'hand':
                if self.ring_ui:
                    self.ring_ui.destroy()
                self.hand_ui = OnscreenImage(image='textures/ui/hand3.png', pos=(0,0,0), scale=(0.03,1,0.04))
                self.hand_ui.setTransparency(TransparencyAttrib.MAlpha)
            self.crosshair = 'hand'
        else:
            if self.crosshair != 'ring':
                if self.hand_ui:
                    self.hand_ui.destroy()
                self.ring_ui = OnscreenImage(image='textures/ui/ring3.png', pos=(0,0,0), scale=(0.03,1,0.04))
                self.ring_ui.setTransparency(TransparencyAttrib.MAlpha)
            self.crosshair = 'ring'
            

    def control_mouse(self):
        #Relative mouse does not work with Windows, has to be done manually.
        md = base.win.getPointer(0)
        x, y = md.get_x(), md.get_y()
        props = base.win.getProperties()
        
        #Move mouse to the center of the screen
        center = [int(props.getXSize() / 2), int(props.getYSize() / 2)]
        if base.win.movePointer(0, center[0], center[1]):
            return [x-center[0], center[1]-y]
        return [0,0]

    def fps_camera(self, mpos):
        x, y = mpos
        hpr = self.camera.getHpr()
        h = hpr[0] - x * settings.sensitivity
        p = hpr[1] + y * settings.sensitivity
        r = hpr[2]

        if settings.constraints[0] != None or settings.constraints[1] != None:
            con_h = settings.constraints[0]
            con_p = settings.constraints[1]

            if con_h - 50 < 0:
                settings.constraints[0] += 360
                con_h = settings.constraints[0]
                h = settings.constraints[0]

            h = max(con_h - 50, min(h, con_h + 50))
            p = max(con_p - 50, min(p, con_p + 50))

        else:
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

        


            #How the fuck do I do this?
##            if not 0<h<50 and not 310<h<360:
##                if h > 180:
##                    if h < 310:
##                        h = 310
##                else:
##                    if h > 50:
##                        h = 50
##
##            h += con_h
            
        
        self.camera.set_h(h)
        self.camera.set_p(p)

    def click_mouse(self, obj):
        if settings.ui_open:
            return
        if self.check_cutscene():
            return
        
        s = self.get_model_string(obj)
        if s not in settings.object_functions:
            print(f"player.py: '{s}' is not a keyword!")
            return
        else:
            v = settings.object_functions[s]

        if callable(v):
            #Is v just a function?
            v()
        elif type(v) is list:
            #It is a list with v and parameters.
            v[0](**v[1])

    def get_model_string(self, obj):
        #Get the name of the model being clicked on.
        s = [x for x in settings.scenes[settings.environment].models if x.model == obj]
        if s:
            return s[0].name

    def check_ray_collision(self, task): #Improve this function!
        self.show_crosshair()
        if settings.picked_obj:
            self.accept("mouse1", self.click_mouse, [settings.picked_obj])
            settings.picked_obj = None
        else:
            self.ignore("mouse1")
            
        #Set ray from center of screen (0,0)
        base.pickerRay.setFromLens(base.camNode, 0,0)

        base.cTrav.traverse(base.interactive_objects)
        #Get all objects that are collinding with the ray.
        if base.queue.getNumEntries() > 0:

            #Sort by distance.
            base.queue.sortEntries()
            pickedObj = base.queue.getEntry(0).getIntoNodePath()
            pickedObj = pickedObj.findNetTag('interactive')
            if not pickedObj.isEmpty():
                dist = base.queue.getEntry(0).getSurfacePoint(self.camera).lengthSquared()
                if dist <= 10:
                    settings.picked_obj = pickedObj
                
        return Task.again

    def check_cutscene(self):
        if base.pos_seq.isPlaying():
            self.col.detachNode()
            return True
        elif not self.col.parent:
            self.col.reparentTo(self.body)
        return False

    def check_constraint(self):
        if None not in settings.constraints:
            self.col.detachNode()

            mpos = [0,0]
            if not settings.free_mouse:
                mpos = self.control_mouse()

            self.fps_camera(mpos)
            return True
        
        elif not self.col.parent:
            self.col.reparentTo(self.body)
        return False
