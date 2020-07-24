#This script manages the game progression. When to execute functions?
#The function, "manage" is executed 0.3 seconds.

from direct.task import Task
import settings, functions

def manage(task):

    if settings.environment == "inte_d1_t1":
        if not settings.g_bools['woken_up']:
            functions.d1_wake_up()
    
    return Task.again


