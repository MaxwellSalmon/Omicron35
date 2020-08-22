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

        setup("hang_d1_t1", os.path.join('models', 'hangar.egg'), colliders.hangar)

        setup("exte_d1_t1", os.path.join('models', 'exterior.egg'), colliders.exterior)

def create_models(scene_name):
    if scene_name[:4] == "inte": #Divide into days and time
        models = [Model('door', tag='interactive', pos=(10,0.1,0.4), scale=0.5, solid=True, audio='door.wav',
                        function=[functions.change_scene, {'to_scene':'exte_d1_t1', 'bool':'clothes_on'}]),
                  Model('interior/suit1', tag='interactive', audio='zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit1'}]),
                  Model('interior/suit2', tag='interactive', audio='zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit2'}]),
                  Model('interior/suit3', tag='interactive', audio='zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit3'}]),
                  Model('interior/showercurtain', pos=(1.65,-8.6,-1.8), solid=True, culling='both'),
                  Model('interior/clipboard', pos=(-4.1,-8.6,0.45), tag='interactive', audio='clipboard.wav', function=functions.take_clipboard),
                  Model('d1t1', scale=21, pos=(0,0,-200)),
                  ]
    elif scene_name[:4] == "exte":
        models = [Model('door', name='ext2int_door', tag='interactive', pos=(10.3,0.1,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'inte_d1_t1'}]),
                  Model('door', name='ext2hang_door', tag='interactive', pos=(77.4,40.25,0.65), hpr=(22.3,0,0), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'hang_d1_t1'}]),
                  Model('exterior/jerrycan', tag='interactive', pos=(63.8,-3,-1.65)),
                  Model('exterior/culext', culling='both'),
                  Model('d1t1', scale=21, pos=(0,0,-200)),
                  ]
    elif scene_name[:4] == "hang":
        models = [Model('door', name='hang2ext_door', tag='interactive', pos=(-16.4,-9.4,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'exte_d1_t1', 'player_pos':(76,37,-0.2)}]),
                  Model('hangar/shelves', culling='both'),
                  Model('hangar/axe', tag='interactive', pos=(-4.17,-9.62,-1.81), scale=0.5),
                  Model('hangar/lamps', culling='both'),
                  Model('d1t1', scale=21, pos=(0,0,-200)),
                  ]
    else:
        models = []
        
    return models
