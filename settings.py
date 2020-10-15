from panda3d.core import (
    KeyboardButton,
    )

#This script contains settings as well as variables exchanged between scripts.

object_functions = {}
g_bools = {
    'clothes_on' : False,
    'woken_up' : False,
    'has_clipboard' : False,
    'has_jerrycan' : False,
    'has_fuel' : False,
    'firewood' : False,
    'generator_refilled' : False,
    'weather_measured' : False,
    'daily_tasks_done': False,
    'has_eaten' : False,
    'radio_used' : False,
    'radio_reported': False,
    'can_sleep' : True,
    'has_taken_can': False,
    }

#Environmental variables
environment = 'exte_d1_t1'
day = 1
time = 1
sun = False
#light, medium, heavy
snow = "heavy"

#Player variables
player_speed = 0.08 * 50
forward_btn = KeyboardButton.ascii_key('w')
strafe_left_btn = KeyboardButton.ascii_key('a')
backward_btn = KeyboardButton.ascii_key('s')
strafe_right_btn = KeyboardButton.ascii_key('d')
sprint_btn = 'lshift'
fov_up_dwn = ('arrow_up', 'arrow_down')
fly_up_dwn = ('space', 'c')
inventory_btn = 'tab'
sensitivity = 0.21
fov = 120

constraints = [None,None]
free_mouse = False
ui_open = False

#Game variables
#free/paid/pirated/source
game_version = "free"

#Interaction variables
picked_obj = None

#Developer variables
show_fps = True
show_col = True
dev_control = True
noclip = False

#Functionality variables
dt = 0

#Scenes
scenes = {}
scene = None
