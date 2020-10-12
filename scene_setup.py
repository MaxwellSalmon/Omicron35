import scenes, settings, colliders, functions
import os
from model import *

def setup(name, base_scene, base_colliders):
    player_pos = {
        "inte" : (9,-3,0),
        "hang" : (-15,-12.5,0),
        "exte" : (11,-3,-0.2)}
    temp_scene = scenes.Scene(name, base_scene, base_colliders)
    temp_scene.models = create_base_models(name) + create_specific_models(name)
    temp_scene.player_position = player_pos[name[:4]]
    
    settings.scenes[name] = temp_scene

def create_scenes(day):    
    if day == 1:
        #Day 1, morning
        setup("inte_d1_t1", os.path.join('models', 'interior.egg'), colliders.house_interior)

        setup("hang_d1_t1", os.path.join('models', 'hangar.egg'), colliders.hangar)

        setup("exte_d1_t1", os.path.join('models', 'exterior.egg'), colliders.exterior)

def create_base_models(scene_name):
    if scene_name[:4] == "inte":
        models = [Model('door', tag='interactive', pos=(10,0.1,0.4), scale=0.5, solid=True, audio='door.wav',
                        function=[functions.change_scene, {'to_scene':'exte_d1_t1', 'bool':'clothes_on'}]),
                  Model('interior/suit1', tag='interactive', audio='zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit1'}]),
                  Model('interior/suit2', tag='interactive', audio='zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit2'}]),
                  Model('interior/suit3', tag='interactive', audio='zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit3'}]),
                  Model('interior/showercurtain', pos=(1.65,-8.6,-1.8), solid=True, culling='both'),
                  Model('interior/clipboard', pos=(-4.1,-8.6,0.45), tag='interactive', audio='clipboard.wav', function=functions.take_clipboard),
                  Model('interior/paper.egg', culling='both'),
                  Model('interior/towels.egg', culling='both'),
                  Model('interior/radio', tag='interactive', audio='default.wav', function=functions.use_radio),
                  Model('interior/bed', tag='interactive', audio='default.wav', function=functions.sleep),
                  Model('interior/pot', tag='interactive', audio='default.wav', function=functions.make_food),
                  Model('interior/can1', tag='interactive', audio='default.wav', function=functions.take_can),
                  Model('interior/can2', tag='interactive', audio='default.wav', function=functions.take_can),
                  Model('interior/can3', tag='interactive', audio='default.wav', function=functions.take_can),
                  Model('interior/can4', tag='interactive', audio='default.wav', function=functions.take_can),
                  Model('interior/can5', tag='interactive', audio='default.wav', function=functions.take_can),
                  Model('interior/can6', tag='interactive', audio='default.wav', function=functions.take_can),
                  Model('interior/can7', tag='interactive', audio='default.wav', function=functions.take_can),
                  Model('interior/can8', tag='interactive', audio='default.wav', function=functions.take_can),
                  Model('interior/plates'),
                  Model('skybox', scale=21, pos=(0,0,-200)),
                  ]
    elif scene_name[:4] == "exte":
        models = [Model('door', name='ext2int_door', tag='interactive', pos=(10.3,0.1,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'inte_d1_t1', 'bool' : 'daily_tasks_done', 'time': 3}], audio='door.wav',),
                  Model('door', name='ext2hang_door', tag='interactive', pos=(77.4,40.25,0.65), hpr=(22.3,0,0), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'hang_d1_t1'}], audio='door.wav'),
                  Model('exterior/jerrycan', tag='interactive', pos=(63.8,-3,-1.65), scale=0.6, function=functions.take_jerrycan, audio='jerrycan.wav'),
                  Model('exterior/culext', culling='both'),
                  Model('exterior/generatortank', tag='interactive', function=functions.refill_generator, audio='generatortank.wav'),
                  Model('exterior/box', tag='interactive', culling='both', function=functions.read_measurements, audio='default.wav'),
                  Model('skybox', scale=21, pos=(0,0,-200)),
                  ]
    elif scene_name[:4] == "hang":
        models = [Model('door', name='hang2ext_door', tag='interactive', pos=(-16.4,-9.4,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'exte_d1_t1', 'player_pos':(76,37,-0.2)}], audio='door.wav'),
                  Model('hangar/shelves', culling='both'),
                  Model('hangar/axe', tag='interactive', pos=(-4.17,-9.62,-1.81), scale=0.5, function=functions.split_firewood, audio='default.wav'),
                  Model('hangar/lamps', culling='both'),
                  Model('hangar/dispenser', tag='interactive', pos=(8.05,-3.37,-1.78), scale=0.5, function=functions.take_fuel, audio='filling_jerrycan.wav'),
                  Model('skybox', scale=21, pos=(0,0,-200)),
                  ]
    else:
        print(scene_name, " not recognized in models")
        models = []
        
    return models

def create_specific_models(scene_name):
   return []
