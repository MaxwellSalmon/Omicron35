import scenes, settings, colliders, functions
import os
from model import *
from trigger import *

def setup(name, base_scene, base_colliders):
    player_pos = {
        "inte" : (9,-3,0),
        "hang" : (-15,-12.5,0),
        "exte" : (11,-3,-0.2)}
    temp_scene = scenes.Scene(name, base_scene, base_colliders)
    temp_scene.models = create_base_models(name) + create_specific_models(name)
    temp_scene.player_position = player_pos[name[:4]]
    temp_scene.triggers = create_triggers(name)
    
    settings.scenes[name] = temp_scene

def create_scenes(day):    
    if day == 1:
        #Day 1, morning
        setup("inte_d1_t1", os.path.join('models', 'interior.egg'), colliders.house_interior)

        setup("hang_d1_t1", os.path.join('models', 'hangar.egg'), colliders.hangar)

        setup("exte_d1_t1", os.path.join('models', 'exterior.egg'), colliders.exterior)

    elif day == 2:
        setup("inte_d2_t1", os.path.join('models', 'interior.egg'), colliders.house_interior)

def create_base_models(scene_name):
    if scene_name[:4] == "inte":
        models = [Model('interior/door', tag='interactive', pos=(10,0.1,0.4), scale=0.5, solid=True, audio='door.wav',
                        function=[functions.change_scene, {'to_scene':'exte_d1_t1', 'bools':['clothes_on', 'has_clipboard'], 'voices':['no_clothes','no_clipboard']}]),
                  Model('interior/suit1', tag='interactive', audio='zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit1'}]),
                  Model('interior/suit2', tag='interactive', audio='zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit2'}]),
                  Model('interior/suit3', tag='interactive', audio='zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit3'}]),
                  Model('interior/bed', tag='interactive', audio='default.wav', function=functions.sleep),
                  Model('interior/showercurtain', pos=(1.65,-8.6,-1.8), solid=True, culling='both'),
                  Model('interior/clipboard', pos=(-4.1,-8.6,0.45), tag='interactive', audio='clipboard.wav', function=functions.take_clipboard, vol=1, tight_emitter=True),
                  Model('interior/paper.egg', culling='both'),
                  Model('interior/towels.egg', culling='both'),
                  Model('interior/radio', tag='interactive', audio='default.wav', function=functions.use_radio),
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
        models = [Model('interior/door', name='ext2int_door', tag='interactive', pos=(10.3,0.1,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'inte_d1_t1', 'bools' : ['daily_tasks_done', '!shed_door_open'], 'time': 2, 'voices':['not_done_with_tasks', 'shed_door_open']}], audio='door.wav',),
                  Model('interior/door', name='ext2hang_door', tag='interactive', pos=(77.4,40.25,0.65), hpr=(202.3,0,0), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'hang_d1_t1'}], audio='door.wav'),
                  Model('exterior/jerrycan', tag='interactive', pos=(63.8,-3,-1.65), scale=0.6, function=functions.take_jerrycan, audio='jerrycan.wav'),
                  Model('exterior/culext', culling='both', ambience='buzz.wav'),
                  Model('exterior/generatortank', tag='interactive', function=functions.refill_generator, audio='generatortank.wav', ambience='generator_motor.wav'),
                  Model('exterior/box', tag='interactive', culling='both', function=functions.read_measurements, audio='default.wav'),
                  Model('exterior/sheddoor', solid=True, pos=(59.2,-1.3,0.5), hpr=(339,0,0)),
                  Model('exterior/bolt', tag='interactive', pos=(59.04,-1.44,0.92), hpr=(338.5,0,0), function=functions.open_shed_door),
                  Model('exterior/junk'),
                  Model('skybox', scale=21, pos=(0,0,-200)),
                  ]
    elif scene_name[:4] == "hang":
        models = [Model('interior/door', name='hang2ext_door', tag='interactive', pos=(-16.4,-9.4,0.4), hpr=(180,0,0), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'exte_d1_t1', 'player_pos':(76,37,-0.2)}], audio='door.wav'),
                  Model('hangar/shelves', culling='both'),
                  Model('hangar/axe', tag='interactive', pos=(-4.17,-9.62,-1.81), scale=0.5, function=functions.split_firewood, audio='default.wav'),
                  Model('hangar/lamps', culling='both'),
                  Model('hangar/dispenser', tag='interactive', pos=(8.05,-3.37,-1.78), scale=0.5, function=functions.take_fuel, audio='filling_jerrycan.wav'),
                  Model('skybox', scale=21, pos=(0,0,-200)),
                  ]
    else:
        print(scene_name, "not recognized as a base scene")
        models = []
        
    return models

def create_specific_models(scene_name):
    if scene_name == 'inte_d1_t1':
        models = []
    elif scene_name == 'inte_d2_t1':
        models = [Model('interior/mess_d1'),
                  Model('interior/mug', alpha=0.3, culling='both'),
                  ]
    else:
        models = []
    return models

def create_triggers(scene_name):
    triggers = []
    if scene_name[:4] == 'exte':
        triggers = [Trigger(65,-7,-1.65,10,functions.shed_snow, mode='enterleave')]

    return triggers
