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
    'can_sleep' : False,
    'has_taken_can': False,
    'radio_conv_done' : False,
    'shed_door_open' : False,
    'shed_door_forced' : False,
    'power_off' : True,
    'generator_plate_removed' : False,
    'has_stardriver' : False,
    'has_screwdriver' : False,
    'has_bad_fuse' : False,
    'has_fuse' : False,
    'generator_fixed': False,
    'has_padlock' : False
    }

#Environmental variables
environment = 'exte_d2_t2'
day = 2
time = 2
sun = True
#light, medium, heavy
snow = ""

#Player variables
player_speed = 0.08 * 50
forward_btn = KeyboardButton.ascii_key('w')
strafe_left_btn = KeyboardButton.ascii_key('a')
backward_btn = KeyboardButton.ascii_key('s')
strafe_right_btn = KeyboardButton.ascii_key('d')
sprint_btn = 'lshift'
console_btn = 'f1'
fov_up_dwn = ('arrow_up', 'arrow_down')
fly_up_dwn = ('space', 'c')
inventory_btn = 'tab'
sensitivity = 0.21
fov = 120

constraints = [None,None]
free_mouse = False
ui_open = False
console_open = False
conversation_ongoing = False

#Game variables
#free/paid/pirated/source
game_version = "free"

#Interaction variables
picked_obj = None
conversation_state = None #State object
shed_screws = 0
hang_screws = 0

#Developer variables
show_env = True
show_fps = True
show_col = False
dev_control = True
skip_convs = False
noclip = False

#Functionality variables
dt = 0
change_sun = False
loading = False
envloading = False
texloading = False

#Scenes
scenes = {}
scene = None

#Conversation states
conversation_states = {}
