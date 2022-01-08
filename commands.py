import settings

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

commands_dict = {
    'help' : help_func,
    '?' : help_func,
    'ff' : complete_tasks,
    'gb' : g_bool,
    'open_the_pod_bay_doors' : HAL9000,
    'noclip' : toggle_noclip,
    'devc' : toggle_dev,
    'center' : center_hpr,
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
    }
