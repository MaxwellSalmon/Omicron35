#This script manages the game progression. When to execute functions?
#The function, "manage" is executed 0.3 seconds.

from direct.task import Task
import settings, functions, voice_strings

def manage(task):

    if settings.environment[:4] == "inte":
        if not settings.g_bools['woken_up']:
            functions.d1_wake_up()
        if settings.g_bools['daily_tasks_done']:
            talk_in_radio()
            check_can_sleep()

        if settings.day == 2:
            if settings.time == 2:
                cut_power()
                open_lod_shed_door()

    if settings.environment[:4] == 'exte':
        check_work_done()
        move_snow()

        if settings.day == 2:
            force_shed_ext_door_open()

    check_triggers()
    
    return Task.again

def check_work_done():
    daily_tasks = [
        settings.g_bools['generator_refilled'],
        settings.g_bools['firewood'],
        settings.g_bools['weather_measured']
        ]

    if False not in daily_tasks:
        settings.g_bools['daily_tasks_done'] = True

def check_can_sleep():
    last_tasks = [
    settings.g_bools['has_eaten'],
    settings.g_bools['radio_used']]
    if False not in last_tasks:
        settings.g_bools['can_sleep'] = True

def move_snow():
    if settings.snow:
        base.weather.move_player_snow()

def check_triggers():
    for trigger in settings.scene.triggers:
        trigger.check()

def cut_power():
    if settings.g_bools['generator_fixed']:
        #Don't run this function, if you already fixed it.
        return
    if settings.g_bools['radio_conv_done'] and settings.g_bools['has_eaten'] and settings.g_bools['has_taken_can']:
        if not settings.g_bools['power_off']:
            settings.g_bools['power_off'] = True
            settings.g_bools['shed_door_open'] = True
            print("POWER HAS BEEN CUT")

            base.conversation.talk('power_bust')
            base.conversation.talk('power_cut')
            #Make dramatic power-off sound
            open_lod_shed_door()

def open_lod_shed_door():
    if settings.g_bools['shed_door_open']:
        door = [x for x in settings.scene.models if 'lod_gate' in x.name]
        door = door[0]
        door.model.set_y(3)
    else:
        door = [x for x in settings.scene.models if 'lod_gate' in x.name]
        door = door[0]
        door.model.set_y(0)

def force_shed_ext_door_open():
    if settings.g_bools['shed_door_open'] and settings.g_bools['power_off']:
        if not settings.g_bools['shed_door_forced']: #only force open once
            settings.g_bools['shed_door_forced'] = True

            door = [x for x in settings.scene.models if 'sheddoor' in x.name]
            bolt = [x for x in settings.scene.models if 'bolt' in x.name]
            door = door[0]
            bolt = bolt[0]
            door.model.set_pos(60,1,0.5)
            bolt.model.set_pos(59.78,0.74,0.92)
            bolt.model.set_hpr(338.5,0,90)

#Radio control function - Finite state machine, I think.
def talk_in_radio():
    is_playing = base.conversation.conv_sequence.isPlaying()

    #Check if radio is clicked, you moved to seat AND you have not reported yet.
    if settings.g_bools['radio_used'] and not base.pos_seq.isPlaying() and not settings.g_bools['radio_reported']:
        settings.g_bools['radio_reported'] = True
        if not settings.conversation_ongoing:
            settings.conversation_ongoing = True
            settings.conversation_state.manage()

    #Radio was clicked, no conversation is playing, conversation has not ended.
    elif settings.g_bools['radio_reported'] and not is_playing and settings.conversation_ongoing:
        settings.conversation_state.manage()

    #Radio conversation is not done, radio has been used and conversation is not ongoing.
    elif not settings.g_bools['radio_conv_done'] and settings.g_bools['radio_reported'] and not settings.conversation_ongoing:
        settings.g_bools['radio_conv_done'] = True
        functions.radio_cutscene('stand')            
        
