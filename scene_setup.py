import scenes, settings, colliders, functions
import os
from model import *

def setup(name, base_scene, base_colliders):
    player_pos = {
        "inte" : (9,-3,0),
        "hang" : (-15,-12.5,0),
        "exte" : (11,-3,-0.2)}
    temp_scene = scenes.Scene(name, base_scene, base_colliders)
    temp_scene.models = create_models(name)
    temp_scene.player_position = player_pos[name[:4]]
    
    settings.scenes[name] = temp_scene

def create_scenes(day):    
    if day == 1:
        #Day 1, morning
        setup("inte_d1_t1", os.path.join('models', 'interior.egg'), colliders.house_interior)

        setup("hang_d1_t1", os.path.join('models', 'hangar.egg'), None)

        setup("exte_d1_t1", os.path.join('models', 'exterior.egg'), colliders.exterior)

def create_models(scene_name):
    if scene_name[:4] == "inte":
        models = [Model('door', tag='interactive', pos=(10,0.1,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'exte_d1_t1'}]),
                  Model('clothes', tag='interactive',
                        function=[functions.put_on_clothes, {'test' : 'Her er en string'}]),
                  ]
    elif scene_name[:4] == "exte":
        models = [Model('door', name='ext2int_door', tag='interactive', pos=(10.3,0.1,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'inte_d1_t1'}]),
                  Model('door', name='ext2hang_door', tag='interactive', pos=(77.4,40.25,0.65), hpr=(22.3,0,0), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'hang_d1_t1'}]),
                  Model('skydome', scale=21, hpr=(240,0,0)),
                  ]
    elif scene_name[:4] == "hang":
        models = [Model('door', name='hang2ext_door', tag='interactive', pos=(-16.4,-9.4,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'exte_d1_t1', 'player_pos':(76,37,0.3)}]),
                  ]
    else:
        models = []
        
    return models
