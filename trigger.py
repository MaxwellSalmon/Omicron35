
import settings

class Trigger:

    def __init__(self, x,y,z, radius, function, **kwargs):
        kg = kwargs.get
        self.radius = radius
        self.function = function

        self.node = base.triggers.attachNewNode('trigger')

        if settings.show_col:
            show = base.loader.load_model('models/dev/sphere.egg')
            show.set_scale(radius)
            show.reparent_to(self.node)
            show.set_pos(0,3,0)
            #Slightly offset for some reason.

        self.node.set_pos(x,y,z)

        self.active = False

        self.mode = 'enter'
        self.name = 'UNNAMED'
        if kg('mode'):
            self.mode = kg('mode')
        if kg('name'):
            self.name = kg('name')

    def enter(self, dist):
        if dist < self.radius:
            if not self.active:
                self.function()
            self.active = True
        else:
            self.active = False

    def enter_leave(self, dist):
        if dist < self.radius:
            if not self.active:
                self.function()
            self.active = True
        else:
            if self.active:
                self.function()
            self.active = False

    def enter_once(self, dist):
        if dist < self.radius:
            if not self.active:
                self.function()
            self.active = True
            

    def check(self):
        dist = self.node.get_distance(base.player.body)
        if self.mode == 'enter':
            self.enter(dist)
        elif self.mode == 'enterleave':
            self.enter_leave(dist)
        elif self.mode == 'enter_once':
            self.enter_once(dist)
        else:
            print("Trigger {} has unknown mode.".format(self.name))
            
