from math import radians, sin, cos
from direct.showbase import DirectObject
from direct.task import Task
from panda3d.core import (
    CollisionNode,
    CollisionCapsule,
    )


import settings


class Player(DirectObject.DirectObject):

    def __init__(self):
        self.body = render.attachNewNode("player")
        self.camera = base.camera
        self.camLens = base.camLens
        self.camera.reparent_to(self.body)
        self.camera.set_pos(0,3,2)
        self.camLens.setFov(80)
        self.camLens.setNear(0.2)
        pos = settings.scenes[settings.environment].player_position
        self.body.set_pos(pos[0], pos[1], pos[2])

        self.speed = settings.player_speed
        self.load_collision()
        
    def load_collision(self):
        self.col = self.body.attachNewNode(CollisionNode('cnode'))
        self.col.node().addSolid(CollisionCapsule(0,3,-1,0,3,2,0.5))
        if settings.show_col:
            self.col.show()
        # Why is 0,0,0 not center of player??
        base.pusher.setHorizontal(True)
        base.cTrav.addCollider(self.col, base.pusher)
        base.pusher.addCollider(self.col, self.body)

    def control_task(self, task):
        if self.check_cutscene():
            return Task.cont
        
        old_pos = self.body.getPos()
        new_pos = old_pos
        add_pos = [0,0,0]
        is_down = base.mouseWatcherNode.is_button_down

        h = radians(self.camera.getH())
        add_pos = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        if is_down(settings.forward_btn):
            add_pos[0] = [-sin(h)*self.speed,cos(h)*self.speed,0]
        if is_down(settings.backward_btn):
            add_pos[1] = [-sin(h)*-self.speed,cos(h)*-self.speed,0]
        if is_down(settings.strafe_right_btn):
            add_pos[2] = [cos(h)*self.speed,sin(h)*self.speed,0]
        if is_down(settings.strafe_left_btn):
            add_pos[3] = [cos(h)*-self.speed,sin(h)*-self.speed,0]

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

        return Task.cont

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

    def click_mouse(self, obj):
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

    def check_ray_collision(self, task):
        if settings.picked_obj:
            settings.picked_obj.clear_color()
            self.accept("mouse1", self.click_mouse, [settings.picked_obj])
            settings.picked_obj = None
        else:
            self.ignore("mouse1")
            
        #Set ray from center of screen (0,0)
        base.pickerRay.setFromLens(base.camNode, 0,0)

        base.cTrav.traverse(base.render)
        #Get all objects that are collinding with the ray.
        if base.queue.getNumEntries() > 0:
            #Sort by distance.
            base.queue.sortEntries()
            pickedObj = base.queue.getEntry(0).getIntoNodePath()
            pickedObj = pickedObj.findNetTag('interactive')
            if not pickedObj.isEmpty():
                dist = base.queue.getEntry(0).getSurfacePoint(self.camera).lengthSquared()
                if dist <= 10:
                    pickedObj.set_color(1,1,0)
                    settings.picked_obj = pickedObj
                
        return Task.cont

    def check_cutscene(self):
        if base.pos_seq.isPlaying():
            self.col.detachNode()
            return True
        elif not self.col.parent:
            self.col.reparentTo(self.body)
        return False