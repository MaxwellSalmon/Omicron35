import settings, voice_strings
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
    voice_index= None

    #Check if all bools are true
    if 'bools' in kwargs:
        for b in range(len(kw('bools'))):
            if kw('bools')[b][0] == '!':
                if settings.g_bools[kw('bools')[b][1:]] == True:
                    voice_index = b
                    break
            else:
                if settings.g_bools[kw('bools')[b]] == False:
                    voice_index = b
                    break

    #Play sound associated with first false bool
    if 'voices' in kwargs and voice_index != None:
        base.conversation.talk(kw('voices')[voice_index])
        return

    #If only one bool and only one voice, play those.
    elif 'bool' in kwargs and not settings.g_bools[kw('bool')]:
        if 'voice' in kwargs:
            base.conversation.talk(kw('voice'))
        return

    #Return even if no voice is associated with a false bool.
    elif voice_index != None:
        return

    base.player.setup_sound(env=to_scene)
    Sequence(Func(fade,'out',0.5), Wait(0.5), Func(change_position, to_scene, **kwargs),
             Wait(0.5), Func(fade,'in', 0.5)).start()

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
        base.conversation.talk('needcan')
        return
    if not settings.g_bools['has_fuel']:
        print("You filled the jerry can with fuel")
        take_object('has_fuel', hide=False)
    else:
        base.conversation.talk('havefuel')

def split_firewood():
    if not settings.g_bools['firewood']:
        take_object('firewood', hide=False)
        base.conversation.talk('writing')
        print("You split the firewood")
    else:
        print("I already split enough firewood")

def refill_generator():
    if not settings.g_bools['has_fuel']:
        if settings.g_bools['has_jerrycan']:
            base.conversation.talk('emptyjerrycan')
        else:
            base.conversation.talk('generatorneedsfuel')
        return
    if not settings.g_bools['generator_refilled']:
        take_object('generator_refilled', hide=False)
        base.conversation.talk('writing')
        base.conversation.talk('refueled')
    else:
        base.conversation.talk('haverefueled')

def read_measurements():
    if not settings.g_bools['weather_measured']:
        take_object('weather_measured', hide=False)
        base.conversation.talk('writing')
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
    if settings.g_bools['can_sleep'] and settings.time != 3:
        settings.time = 3
        Sequence(Func(sleep_cutscene), Wait(8), Func(fade,'out',3), Wait(3),
                 Func(base.superloader.change_textures), Wait(4), Func(fade,'in', 2), Wait(2), Func(night_wake_up)).start()
    elif settings.g_bools['can_sleep'] and settings.time == 3:
        settings.time = 1
        settings.day += 1
        reset_g_bools()
        let_it_snow()
        Sequence(Func(sleep_cutscene), Wait(8), Func(fade,'out',3), Wait(3),
                 Func(base.superloader.load, "inte_d{}_t1".format(settings.day), False, newday=True), Wait(4), Func(fade,'in', 2), Wait(2), Func(d1_wake_up)).start()
        
    else:
        print("I am not tired yet")

#This function simply activates weather in settings
def let_it_snow():
    if settings.day == 2:
        settings.sun = False
        settings.snow = 'light'
        settings.wind = () #temp

#This function resets g_bools from settings.py each day
def reset_g_bools():
    no_reset = [] #Don't reset bools in this list
    for i in settings.g_bools:
        if i  in no_reset:
            continue
        settings.g_bools[i] = False
    

def open_shed_door():
    door = [x for x in settings.scene.models if 'sheddoor' in x.name]
    door = door[0]
    bolt = get_model().model
    start_pos = (59.2,-1.3,0.5)
    end_pos = (60,1,0.5)
    bolt_start_pos = (59.04,-1.44,0.92)
    bolt_end_pos = (59.78,0.74,0.92)
    bolt = get_model().model

    if not settings.g_bools['shed_door_open']:
        Sequence(Wait(1), LerpPosInterval(door.model, 2, end_pos)).start()
        Sequence(LerpHprInterval(bolt, 1, (338.5,0,90)), LerpPosInterval(bolt, 2, bolt_end_pos)).start()
        settings.g_bools['shed_door_open'] = True
    elif base.player.body.get_x() < 58:
        Sequence(LerpPosInterval(door.model, 2, start_pos)).start()
        Sequence(LerpPosInterval(bolt, 2, bolt_start_pos), LerpHprInterval(bolt, 1, (338.5,0,0))).start()
        settings.g_bools['shed_door_open'] = False

### Cutscenes ###
    
def sleep_cutscene():
    base.cutscene([{'h':85, 'p':-5, 'y':-10.5, 'd':2},
                       {'p':0, 'y':-11,'z':-1, 'd':2},
                       {'h':0,'p':90,'r':0, 'x':-0.36, 'y':-12.36, 'z':-1.5, 'd':2}])
    settings.constraints = [0,40]
        
def d1_wake_up():
    sequence = [{'h':0,'p':90,'r':0, 'x':-0.36, 'y':-12.36, 'z':-1.5, 'd':1},
                {'p':0, 'y':-11,'z':-1, 'd':2},
                {'h':85, 'p':-5, 'y':-10.5, 'd':2},
                {'x':-2.3, 'p':-8, 'z':0, 'd':2},
                {'h':120, 'p':-35},
                {'x':-3.4, 'y':-11.2, 'p':-65, 'd':2.5}]
    if settings.day == 1:
        sequence[0]['d'] = 0
    base.cutscene(sequence)
    settings.g_bools['woken_up'] = True

def night_wake_up():
    base.cutscene([{'p':0, 'y':-12,'z':-1, 'd':2},
                   {'h':85, 'p':-5, 'y':-10.5, 'd':2},
                   {'x':-2.3, 'p':-8, 'z':0, 'd':2},])

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

### Trigger functions ###

def shed_snow():
    if settings.snow:
        base.weather.shed_snow()
