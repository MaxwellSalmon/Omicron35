from panda3d.core import (
    KeyboardButton,
    )

#This script contains settings as well as variables exchanged between scripts.

object_functions = {}

#Environmental variables
environment = 'inte_d1_t1'
day = 1
time = 1

#Player variables
player_speed = 0.08
forward_btn = KeyboardButton.ascii_key('w')
strafe_left_btn = KeyboardButton.ascii_key('a')
backward_btn = KeyboardButton.ascii_key('s')
strafe_right_btn = KeyboardButton.ascii_key('d')
free_mouse = False
sensitivity = 0.21

#Interaction variables
picked_obj = None

#Game booleans
clothes_on = False

#Developer variables
show_fps = True
show_col = False

#Scenes
scenes = {}
