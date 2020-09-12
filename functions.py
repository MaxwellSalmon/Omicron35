import settings
from direct.showbase.Transitions import Transitions
from direct.interval.IntervalGlobal import *

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

    Sequence(Func(fade,'out',0.5), Wait(0.5), Func(change_position, to_scene, **kwargs), Wait(0.5), Func(fade,'in', 0.5)).start()

def change_position(to_scene, **kwargs):
    kw = kwargs.get
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

    if 'time' in kwargs and settings.time != kw('time'):
        settings.time = kw('time')
        base.superloader.change_textures()

    base.scene.flattenStrong()
    

def fade(direction, time):
    base.transition.setFadeColor(0,0,0)
    if direction == 'out':
        base.transition.fadeOut(time)
    elif direction == 'in':
        base.transition.fadeIn(time)

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
    if not settings.g_bools['weather_measure']:
        take_object('weather_measured', hide=False)
        print("You read the weather measurements")
    else:
        print("You already measured the weather")

def use_radio():
    if settings.g_bools['daily_tasks_done']:
        if not settings.g_bools['radio_used']:
            #Special function
            take_object('radio_used', hide=False)
            radio_cutscene('sit')
            settings.constraints = [90,0]
            print("You used the radio")
        else:
            print("You already used the radio")
    else:
        print("It is not time to report yet.")

def make_food():
    if settings.g_bools['daily_tasks_done']:
        if not settings.g_bools['has_eaten']:
            #special function
            take_object('has_eaten', hide=False)
            food_cutscene('to_cans')
            settings.constraints = [0,0]
        else:
            print("I have already eaten")
    else:
        print("I am not hungry right now")

def take_can():
    if settings.g_bools['has_eaten'] and not settings.g_bools['has_taken_can']:
        take_object('has_taken_can')
        food_cutscene('to_pot')
        #settings.constraints = [0,-20]
        print("I made food")
    else:
        make_food()

def sleep():
    if settings.g_bools['can_sleep']:
        base.cutscene([{'h':85, 'p':-5, 'y':-10.5, 'd':2},
                       {'p':0, 'y':-11,'z':-1, 'd':2},
                       {'h':0,'p':90,'r':0, 'x':-0.36, 'y':-11.36, 'z':-1.5, 'd':2}])
        settings.constraints = [0,40]
    else:
        print("I am not tired yet")
        
def d1_wake_up():
    base.cutscene([{'h':0,'p':90,'r':0, 'x':-0.36, 'y':-11.36, 'z':-1.5, 'd':0},
                    {'p':0, 'y':-11,'z':-1, 'd':2},
                    {'h':85, 'p':-5, 'y':-10.5, 'd':2},
                    {'x':-2.3, 'p':-8, 'z':0, 'd':2},
                   {'h':120, 'p':-35},
                   {'x':-3.4, 'y':-11.2, 'p':-65, 'd':2.5}])
    settings.g_bools['woken_up'] = True

def radio_cutscene(direction):
    if direction=='sit':
        base.cutscene([{'x':-3, 'y':0, 'z':-0.6},
                       {'h':100, 'p':-20, 'd':2}])
    elif direction == 'stand':
        base.cutscene([{'x':-3, 'y':3, 'z':0}])

def food_cutscene(direction):
    if direction == 'to_cans':
        base.cutscene([{'x':1.3, 'y':4.2, 'z':0.5, 'h':0, 'p':0},
                       {'d':1}])
    elif direction == 'to_pot':
        base.cutscene([{'x':0.2, 'y':3.8, 'z':0, 'h':0.8, 'p':-60, 'd':2}])
