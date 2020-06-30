import settings

def door_function(): #Redundant
    if settings.clothes_on:
        if settings.environment == "inside":
            self.outside.reparentTo(self.render)
            self.scene.detachNode()
            settings.environment = "outside"
            self.door.setPos(6.5,1.2,0.4)
        else:
            self.outside.detachNode()
            self.scene.reparentTo(self.render)
            settings.environment = "inside"
            self.door.setX(0)
    else:
        print("Jeg skal have tøj på først")

def change_scene(to_scene, **kwargs):
    kw = kwargs.get

    if 'bool' in kwargs and not settings.g_bools[kw('bool')]:
        print("Something is missing")
        return
    
    #Player position
    if kw('player_pos'):
        p = kw('player_pos')
        base.player.body.set_pos(p[0], p[1], p[2])
    else:
        print(to_scene)
        p = settings.scenes[to_scene].player_position
        base.player.body.set_pos(p[0], p[1], p[2])       
    
    for model in settings.scenes[settings.environment].models:
        model.model.detachNode()
    base.scene.detachNode()
    base.superloader.load(to_scene, None)
    base.scene.flattenStrong()

def put_on_clothes(test):
    settings.g_bools['clothes_on'] = True
    clothes_model = [x for x in settings.scenes[settings.environment].models if x.name == 'clothes']
    if not clothes_model:
        print("Clothes not found in scene models!")
        return
    clothes_model[0].model.set_pos(0,0,-10)
    print("Jeg har taget tøjet på")
    print(test)

    base.cutscene([{'h':0,'p':90,'r':0, 'x':-0.36, 'y':-11.36, 'z':-1.5, 'd':0},
                    {'p':0, 'y':-11,'z':-1, 'd':2},
                    {'h':85, 'p':-5, 'y':-10.5, 'd':2},
                    {'x':-2.3, 'p':-8, 'z':0, 'd':2}])
