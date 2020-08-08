from panda3d.core import CollisionNode, CollisionBox

import settings

class Model():

    def __init__(self, path, **kwargs):
        
        kg = kwargs.get

        if 'models/' not in path:
            path = 'models/'+path
        model = loader.load_model(path)
        name = path[7:]

        model.set_scale(0.5) #default scale
        model.set_pos(0, 0, -1.8)

        self.audio = None
        
        if kg('name'):
            #If interactive objects share the model, differentiate between them with custom name
            name = kg('name')
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
            settings.object_functions[str(name)] = kg('function')
        if kg('audio'):
            self.audio = base.superloader.load_sound_queue((kg('audio'), model, 1, self))
        if kg('culling'):
            if kg('culling') == 'both':
                model.setTwoSided(True)
        if kg('solid'):
            bmin, bmax = model.get_tight_bounds()
            bounds = bmax-bmin
            col = model.attachNewNode(CollisionNode(name))
            col.node().add_solid(CollisionBox((0,0,0), bounds[0], bounds[1], bounds[2]))

            if settings.show_col:
                col.show()

        self.model = model
        self.name = name

    def play_audio(self):
        if self.audio:
            self.audio.play()
