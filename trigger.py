
import settings

class Trigger:

    def __init__(self, x,y,z, radius, function):
        self.radius = radius
        self.function = function

        self.node = base.triggers.attachNewNode('trigger')
        self.node.set_pos(x,y,z)

        if settings.show_col:
            show = base.loader.load_model('models/dev/sphere.egg')
            show.set_scale(radius)
            show.reparent_to(self.node)

        self.active = False

    def check(self):
        dist = self.node.get_distance(base.player.body)
        if dist < self.radius:
            if not self.active:
                self.function()
            self.active = True
        else:
            self.active = False
