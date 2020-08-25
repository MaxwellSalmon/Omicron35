#This script manages the game progression. When to execute functions?
#The function, "manage" is executed 0.3 seconds.

from direct.task import Task
import settings, functions

def manage(task):

    if settings.environment == "inte_d1_t1":
        if not settings.g_bools['woken_up']:
            functions.d1_wake_up()

    check_work_done()
    
    return Task.again

def check_work_done():
    daily_tasks = [
        settings.g_bools['generator_refilled'],
        settings.g_bools['firewood'],
        settings.g_bools['weather_measured']
        ]

    if False not in daily_tasks:
        settings.g_bools['daily_tasks_done'] = True
