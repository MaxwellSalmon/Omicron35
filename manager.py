#This script manages the game progression. When to execute functions?
#The function, "manage" is executed 0.3 seconds.

from direct.task import Task
import settings, functions, voice_strings
import conversation_manager

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
    if settings.g_bools['radio_conv_done'] and settings.g_bools['has_eaten'] and settings.g_bools['has_taken_can']:
        if not settings.g_bools['power_off']:
            settings.g_bools['power_off'] = True
            settings.g_bools['shed_door_open'] = True
            print("POWER HAS BEEN CUT")
            base.conversation.talk('power_cut')
            #Make dramatic power-off sound
            functions.open_lod_shed_door()

def open_lod_shed_door():
    if settings.g_bools['shed_door_open']:
        door = [x for x in settings.scene.models if 'lod_gate' in x.name]
        door = door[0]
        door.model.set_y(3)
    else:
        door = [x for x in settings.scene.models if 'lod_gate' in x.name]
        door = door[0]
        door.model.set_y(0)
        

#Which conversation should be started?
def determine_conversation():
    return 'radio_day' + str(settings.day)

#Radio control function - Finite state machine, I think.
def talk_in_radio():
    path = settings.conversation_path
    prog = settings.conversation_progress
    is_playing = base.conversation.conv_sequence.isPlaying()

    #Start the conversation after having moved to radio
    if settings.g_bools['radio_used'] and not base.pos_seq.isPlaying() and not settings.g_bools['radio_reported']:
        settings.g_bools['radio_reported'] = True
        sound = determine_conversation()
        base.conversation.talk(sound)

    elif settings.g_bools['radio_reported'] and not is_playing:
        conversation_manager.gui_choices(path)

        #Stand up when conversation is over.
        if not settings.g_bools['radio_conv_done'] and not base.conv_gui.shown:
            settings.g_bools['radio_conv_done'] = True
            functions.radio_cutscene('stand')            
        
