from panda3d.core import (
    KeyboardButton,
    )

#This script contains settings as well as variables exchanged between scripts.

object_functions = {}
g_bools = {
    'clothes_on' : False,
    'woken_up' : False,
    'has_clipboard' : False}

#Environmental variables
environment = 'inte_d1_t1'
day = 1
time = 1

#Player variables
player_speed = 0.08 * 50
forward_btn = KeyboardButton.ascii_key('w')
strafe_left_btn = KeyboardButton.ascii_key('a')
backward_btn = KeyboardButton.ascii_key('s')
strafe_right_btn = KeyboardButton.ascii_key('d')
sprint_btn = 'lshift'
inventory_btn = 'tab'
sensitivity = 0.21

free_mouse = False
ui_open = False

#Interaction variables
picked_obj = None

#Developer variables
show_fps = True
show_col = False
dev_control = True

#Functionality variables
dt = 0

#Scenes
scenes = {}
scene = None
