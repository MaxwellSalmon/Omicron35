import settings
from direct.interval.IntervalGlobal import *
import functions

def help_func(*args):

    if not args:
        keys = sorted(commands_dict.keys())
        keys.remove('open_the_pod_bay_doors')
        help_list = ', '.join(keys)
        return help_list

    return help_strings[args[0]]


def complete_tasks():
    settings.g_bools['daily_tasks_done'] = True
    settings.g_bools['can_sleep'] = True
    settings.g_bools['has_clipboard'] = True
    settings.g_bools['clothes_on'] = True
    
    return "Tasks done, sleep tight."

def g_bool(g_bool):
    if g_bool not in settings.g_bools:
        return f"{g_bool} not in g_bools"
    settings.g_bools[g_bool] = not settings.g_bools[g_bool]
    return f"Toggled {g_bool} to {settings.g_bools[g_bool]}"

def HAL9000():
    return "I'm sorry Dave. I'm afraid I can't do that."

def toggle_noclip():
    settings.noclip = not settings.noclip
    player = base.player
    base.cTrav.removeCollider(player.col)
    base.pusher.removeCollider(player.col)
    player.load_collision()
    return f"Noclip set to {settings.noclip}"

def toggle_dev():
    settings.dev_control = not settings.dev_control
    return f"Dev control set to {settings.dev_control}"

def center_hpr():
    base.camera.setHpr(0,0,0)
    return "Camera HPR set to (0,0,0)"

def show_cols():
    settings.show_col = not settings.show_col
    base.superloader.load_collision_scene()
    return f"Toggling show collisions to {settings.show_col}"

def get_pos():
    pos = base.player.body.get_pos()
    hpr = base.player.camera.get_hpr()
    return f"Player position: ({pos[0]:.2f}, {pos[1]:.2f}, {pos[2]:.2f})\n\tPlayer HPR:({hpr[0]:.2f}, {hpr[1]:.2f}, {hpr[2]:.2f})"

def get_state():
    state_name = settings.conversation_state.name
    return f"State: {state_name}"

def skip_conv():
    settings.skip_convs = not settings.skip_convs
    return f"Skip conversations set to {settings.skip_convs}"

def movobj(model, pos=()):
    m = functions.find_model(model).model
    if not pos:
        return m.get_pos()
    interval = m.posInterval(2.0, eval(pos))
    interval.start()
    return f"Moved to {pos}"

def next_day():
    settings.time = 1
    settings.day += 1

    functions.reset_g_bools()
    functions.let_it_snow()
    base.superloader.load("inte_d{}_t1".format(settings.day), False, newday=True)
    base.superloader.change_textures()
    return f"Set day to {settings.day}, remember radio."

def set_conv(name):
    settings.conversation_state = settings.conversation_states[name]
    return f"Set conversation state to {name}."

commands_dict = {
    'help' : help_func,
    '?' : help_func,
    'ff' : complete_tasks,
    'gb' : g_bool,
    'open_the_pod_bay_doors' : HAL9000,
    'noclip' : toggle_noclip,
    'devc' : toggle_dev,
    'center' : center_hpr,
    'showcol' : show_cols,
    'pos' : get_pos,
    'cstate' : get_state,
    'skipconv' : skip_conv,
    'nextday' : next_day,
    'movobj' : movobj,
    'setconv' : set_conv,
    }

help_strings = {
    'help' : "It is this function...",
    '?' : "It shows this very list...",
    'ff' : "fastforward - finished up daily tasks and allows sleep.",
    'gb' : "gb <g_bool> - toggles values of a g_bool.",
    'open_the_pod_bay_doors' : "Kindly asks HAL 9000 if it can open the pod bay doors.",
    'noclip' : "Toggles noclip. Space to fly up, 'c' to fly down.",
    'devc' : "Toggles dev control. (Skips cutscenes, allow sprint with lshift)",
    'center' : "Sets camera hpr to (0,0,0)",
    'showcol' : "Turn on visible collider primitives",
    'pos' : "Prints player position and camera HPR",
    'cstate' : "Prints the name of the current conversation state.",
    'skipconv' : "Toggles option to skip conversations.",
    'nextday' : "Changes the time to the morning, next day",
    'movobj' : "Move object to position. movobj <model> <(x,y,z)>",
    'setconv' : "Sets conversation state. setconv <state name>",
    }
