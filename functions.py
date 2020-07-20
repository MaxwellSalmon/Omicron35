import settings

def get_model():
    #Does not take custon model names into account. Perhaps it needs attention later.
    obj_name = str(settings.picked_obj).split('/')[-1][:-4]
    model = [x for x in settings.scenes[settings.environment].models if str(x.name).split('/')[-1] == obj_name]
    if model:
        return model[0]

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
    if not settings.g_bools['clothes_on']:
        settings.g_bools['clothes_on'] = True
        settings.picked_obj.set_pos(0,0,-10)
        print("You put on your clothes")
        get_model().play_audio()

        #base.cutscene([{'h':0,'p':90,'r':0, 'x':-0.36, 'y':-11.36, 'z':-1.5, 'd':0},
        #                {'p':0, 'y':-11,'z':-1, 'd':2},
        #                {'h':85, 'p':-5, 'y':-10.5, 'd':2},
        #                {'x':-2.3, 'p':-8, 'z':0, 'd':2}])
