import settings

#This script contains functions which execute when interacting with an object or entering a scene.

def get_model():
    model = [x for x in settings.scene.models if x.model == settings.picked_obj]
    if model:
        return model[0]
    print("Could not fetch model ", settings.picked_obj)

def change_scene(to_scene, **kwargs):
    kw = kwargs.get
    get_model().play_audio()

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

def take_clipboard():
    settings.picked_obj.set_pos(0,0,-10)
    get_model().play_audio()
    settings.g_bools['has_clipboard'] = True

        
def d1_wake_up():
    base.cutscene([{'h':0,'p':90,'r':0, 'x':-0.36, 'y':-11.36, 'z':-1.5, 'd':0},
                    {'p':0, 'y':-11,'z':-1, 'd':2},
                    {'h':85, 'p':-5, 'y':-10.5, 'd':2},
                    {'x':-2.3, 'p':-8, 'z':0, 'd':2},
                   {'h':120, 'p':-35},
                   {'x':-3.4, 'y':-11.2, 'p':-65, 'd':2.5}])
    settings.g_bools['woken_up'] = True
