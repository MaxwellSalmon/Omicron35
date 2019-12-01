from panda3d.core import (
    KeyboardButton,
    )

object_functions = {}

#Environmental variables
environment = 'inside'

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
