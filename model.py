from panda3d.core import CollisionNode, CollisionBox

import settings

class Model():

    def __init__(self, path, **kwargs):
        
        kg = kwargs.get

        if 'models/' not in path:
            path = 'models/'+path
        model = loader.load_model(path)
        name = path[7:]
        
        if kg('parent'):
            model.reparent_to(kg('parent'))
        else:
            model.reparent_to(render)
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
            settings.object_functions[str(model)] = kg('function')
        if kg('solid'):
            bmin, bmax = model.get_tight_bounds()
            bounds = bmax-bmin
            col = model.attachNewNode(CollisionNode(name))
            col.node().add_solid(CollisionBox((0,0,0), bounds[0], bounds[1], bounds[2]))

            col.show()
