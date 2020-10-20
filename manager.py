#This script manages the game progression. When to execute functions?
#The function, "manage" is executed 0.3 seconds.

from direct.task import Task
import settings, functions, voice_strings

def manage(task):

    if settings.environment[:4] == "inte":
        if not settings.g_bools['woken_up']:
            functions.d1_wake_up()
        if settings.g_bools['daily_tasks_done']:
            report_radio()
            radio_conv_done()
            check_can_sleep()

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
    

def report_radio():
    if settings.g_bools['radio_used'] and not base.pos_seq.isPlaying() and not settings.g_bools['radio_reported']:
        if settings.day == 1:
            settings.g_bools['radio_reported'] = True
            voice_strings.talk('radio_day1')

def radio_conv_done():
    if settings.g_bools['radio_reported'] and not voice_strings.conv_sequence.isPlaying():
        if not settings.g_bools['radio_conv_done']:
            settings.g_bools['radio_conv_done'] = True
            functions.radio_cutscene("stand")
            
            
        
