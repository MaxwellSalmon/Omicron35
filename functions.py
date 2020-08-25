import settings

#This script contains functions which execute when interacting with an object or entering a scene.

def get_model():
    model = [x for x in settings.scene.models if x.model == settings.picked_obj]
    if model:
        return model[0]
    print("Could not fetch model ", settings.picked_obj)

def change_scene(to_scene, **kwargs):
    kw = kwargs.get

    if 'bool' in kwargs and not settings.g_bools[kw('bool')]:
        print("Something is missing")
        return

    get_model().play_audio()
    
    #Player position
    if kw('player_pos'):
        p = kw('player_pos')
        base.player.body.set_pos(p[0], p[1], p[2])
    else:
        p = settings.scenes[to_scene].player_position
        base.player.body.set_pos(p[0], p[1], p[2])       
    
    for model in settings.scenes[settings.environment].models:
        model.model.detachNode()
    base.scene.detachNode()
    base.superloader.load(to_scene, None)
    base.scene.flattenStrong()

def take_object(g_bool, **kwargs):
    kw = kwargs.get
    if ('hide' in kwargs and kw('hide')) or 'hide' not in kwargs:
        settings.picked_obj.set_pos(0,0,-10)
    get_model().play_audio()
    settings.g_bools[g_bool] = True

def put_on_clothes(test):
    if not settings.g_bools['clothes_on']:
        take_object('clothes_on')

def take_clipboard():
    take_object('has_clipboard')

def take_jerrycan():
    take_object('has_jerrycan')

def take_fuel():
    if not settings.g_bools['has_jerrycan']:
        print("You do not have anything to carry the fuel in")
        return
    if not settings.g_bools['has_fuel']:
        print("You filled the jerry can with fuel")
        take_object('has_fuel', hide=False)
    else:
        print("I already have fuel in the jerrycan")

def split_firewood():
    if not settings.g_bools['firewood']:
        take_object('firewood', hide=False)
        print("You split the firewood")
    else:
        print("I already split enough firewood")

def refill_generator():
    if not settings.g_bools['has_fuel']:
        print("I do not have any fuel to put in the generator")
        return
    if not settings.g_bools['generator_refilled']:
        take_object('generator_refilled', hide=False)
        print("You refilled the generator")
    else:
        print("I alredy refilled the generator")

def read_measurements():
    take_object('generator', hide=False)
    print("You read the weather measurements")

        
def d1_wake_up():
    base.cutscene([{'h':0,'p':90,'r':0, 'x':-0.36, 'y':-11.36, 'z':-1.5, 'd':0},
                    {'p':0, 'y':-11,'z':-1, 'd':2},
                    {'h':85, 'p':-5, 'y':-10.5, 'd':2},
                    {'x':-2.3, 'p':-8, 'z':0, 'd':2},
                   {'h':120, 'p':-35},
                   {'x':-3.4, 'y':-11.2, 'p':-65, 'd':2.5}])
    settings.g_bools['woken_up'] = True
