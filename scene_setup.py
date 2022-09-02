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
    print("creating", name)

def create_scenes(day):    
    if day == 1:
        #Day 1, morning
        setup("inte_d1_t1", os.path.join('models', 'interior.egg'), colliders.house_interior)

        setup("hang_d1_t1", os.path.join('models', 'hangar.egg'), colliders.hangar)

        setup("exte_d1_t1", os.path.join('models', 'exterior.egg'), colliders.exterior)

    elif day == 2:
        setup("inte_d2_t1", os.path.join('models', 'interior.egg'), colliders.house_interior)

        setup("exte_d2_t1", os.path.join('models', 'exterior.egg'), colliders.exterior)

        setup("exte_d2_t2", os.path.join('models', 'exterior.egg'), colliders.exterior)

        setup("hang_d2_t1", os.path.join('models', 'hangar.egg'), colliders.hangar)

    elif day == 3:
        setup("inte_d3_t1", os.path.join('models', 'interior.egg'), colliders.house_interior)

        setup("exte_d3_t1", os.path.join('models', 'exterior.egg'), colliders.exterior)

        setup("hang_d3_t1", os.path.join('models', 'hangar.egg'), colliders.hangar)

def create_base_models(scene_name):
    if scene_name[:4] == "inte":
        models = [Model('interior/suit1', tag='interactive', audio='sfx/zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit1'}]),
                  Model('interior/suit2', tag='interactive', audio='sfx/zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit2'}]),
                  Model('interior/suit3', tag='interactive', audio='sfx/zipper.wav', function=[functions.put_on_clothes, {'test' : 'Here is suit3'}]),
                  Model('interior/bed', tag='interactive', audio='default.wav', function=functions.sleep),
                  Model('interior/showercurtain', pos=(1.65,-8.6,-1.8), solid=True, culling='both'),
                  Model('interior/clipboard', pos=(-4.1,-8.6,0.45), tag='interactive', audio='sfx/clipboard.wav', function=functions.take_clipboard, vol=1, tight_emitter=True),
                  Model('interior/paper.egg', culling='both'),
                  Model('interior/towels.egg', culling='both'),
                  Model('interior/radio', tag='interactive', audio='default.wav', function=functions.use_radio),
                  Model('interior/pot', tag='interactive', audio='default.wav', function=functions.make_food),
                  Model('interior/can1', tag='interactive', audio='sfx/Can_Open_And_Boil.wav', function=functions.take_can),
                  Model('interior/can2', tag='interactive', audio='sfx/Can_Open_And_Boil.wav', function=functions.take_can),
                  Model('interior/can3', tag='interactive', audio='sfx/Can_Open_And_Boil.wav', function=functions.take_can),
                  Model('interior/can4', tag='interactive', audio='sfx/Can_Open_And_Boil.wav', function=functions.take_can),
                  Model('interior/can5', tag='interactive', audio='sfx/Can_Open_And_Boil.wav', function=functions.take_can),
                  Model('interior/can6', tag='interactive', audio='sfx/Can_Open_And_Boil.wav', function=functions.take_can),
                  Model('interior/can7', tag='interactive', audio='sfx/Can_Open_And_Boil.wav', function=functions.take_can),
                  Model('interior/can8', tag='interactive', audio='sfx/Can_Open_And_Boil.wav', function=functions.take_can),
                  Model('interior/lod_gate'),
                  Model('interior/plates'),
                  Model('skybox', scale=21, pos=(0,0,-200)),
                  ]
    elif scene_name[:4] == "exte":
        models = [Model('exterior/jerrycan', tag='interactive', pos=(63.6,-3,-1.7), scale=0.6, function=functions.take_jerrycan, audio='sfx/jerrycan.wav'),
                  Model('exterior/culext', culling='both'),
                  Model('exterior/generatortank', tag='interactive', function=functions.refill_generator, audio='sfx/generatortank.wav'),
                  Model('dev/sphere', scale=0.1, pos=(66,-4,-1), ambience='amb/generator_motor.wav', stop_ambience_on=['power_off']),
                  Model('dev/sphere', scale=0.01, pos=(63,-3, 4), ambience='amb/buzz.wav', stop_ambience_on=['power_off']),
                  Model('exterior/box', tag='interactive', culling='both', function=functions.read_measurements, audio='default.wav'),
                  Model('exterior/sheddoor', solid=True, pos=(59.2,-1.3,0.5), hpr=(339,0,0), audio=['sfx/Door_Open_Only.wav', 'sfx/Door_Open_Only.wav']),
                  Model('exterior/bolt', tag='interactive', pos=(59.04,-1.44,0.92), hpr=(338.5,0,0), function=functions.open_shed_door),
                  Model('exterior/junk'),
                  Model('skybox', scale=21, pos=(0,0,-200)),
                  ]
    elif scene_name[:4] == "hang":
        models = [Model('hangar/shelves', culling='both'),
                  Model('hangar/axe', tag='interactive', pos=(-4.17,-9.62,-1.81), scale=0.5, function=functions.split_firewood, audio='sfx/Wood_Chop.wav'),
                  Model('hangar/lamps', culling='both'),
                  Model('hangar/dispenser', tag='interactive', pos=(8.05,-3.37,-1.78), scale=0.5, function=functions.take_fuel, audio='sfx/filling_jerrycan.wav'),
                  Model('skybox', scale=21, pos=(0,0,-200)),
                  ]
    else:
        print(scene_name, "not recognized as a base scene")
        models = []
        
    return models

def create_specific_models(scene_name):
    #Interior
    if scene_name[:-3] == 'inte_d1':
        models = [Model('interior/door', tag='interactive', pos=(10,0.1,0.4), scale=0.5, solid=True, audio='sfx/door.wav',
                        function=[functions.change_scene, {'to_scene':'exte_d1_t1', 'bools':['clothes_on', 'has_clipboard'], 'voices':['no_clothes','no_clipboard']}]),
                  ]
    elif scene_name[:-3] == 'inte_d2':
        models = [Model('interior/door', tag='interactive', pos=(10,0.1,0.4), scale=0.5, solid=True, audio='sfx/door.wav',
                        function=[functions.change_scene, {'to_scene':'exte_d2_t1', 'bools':['clothes_on', 'has_clipboard'], 'voices':['no_clothes','no_clipboard']}]),
                  Model('interior/mess_d2'),
                  ]

    #Exterior
    elif scene_name[:-3] == 'exte_d1':
        models = [Model('interior/door', name='ext2int_door', tag='interactive', pos=(10.3,0.1,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'inte_d1_t1', 'bools' : ['daily_tasks_done', '!shed_door_open'], 'time': 2, 'voices':['not_done_with_tasks', 'shed_door_open']}], audio='sfx/door.wav',),
                  Model('interior/door', name='ext2hang_door', tag='interactive', pos=(77.4,40.25,0.65), hpr=(202.3,0,0), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'hang_d1_t1'}], audio='sfx/door.wav'),
                  Model('exterior/screw1', name='screw1', tag='not_interactive'),
                  Model('exterior/screw2', name='screw2', tag='not_interactive'),
                  Model('exterior/screw3', name='screw3', tag='not_interactive'),
                  Model('exterior/screw4', name='screw4', tag='not_interactive'),
                  Model('exterior/plate', name='plate', tag='not_interactive',),
                  Model('exterior/padlock', name='padlock', pos=(62.83,-8.26,1.05), hpr=(250,0,90), tag='not_interactive'),
                  Model('exterior/screwdriver', name="screwdriver3", tag='not_interactive'),
                  ]
        
    elif scene_name == 'exte_d2_t1':
        models = [Model('interior/door', name='ext2int_door_nopadlock', tag='interactive', pos=(10.3,0.1,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'inte_d2_t1', 'bools' : ['daily_tasks_done', '!shed_door_open'], 'time': 2, 'voices':['not_done_with_tasks', 'shed_door_open']}], audio='sfx/door.wav',),
                  Model('interior/door', name='ext2hang_door', tag='interactive', pos=(77.4,40.25,0.65), hpr=(202.3,0,0), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'hang_d2_t1'}], audio='sfx/door.wav'),
                  Model('exterior/screw1', name='screw1', tag='not_interactive'),
                  Model('exterior/screw2', name='screw2', tag='not_interactive'),
                  Model('exterior/screw3', name='screw3', tag='not_interactive'),
                  Model('exterior/screw4', name='screw4', tag='not_interactive'),
                  Model('exterior/plate', name='plate', tag='not_interactive',),
                  Model('exterior/padlock', name='padlock', pos=(62.83,-8.26,1.05), hpr=(250,0,90), tag='not_interactive'),
                  Model('exterior/screwdriver', name="screwdriver3", tag='not_interactive'),
                  ]
        
    elif scene_name[:-3] == 'exte_d2':
        models = [Model('interior/door', name='ext2int_door', tag='interactive', pos=(10.3,0.1,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'inte_d2_t1', 'bools' : ['daily_tasks_done', '!shed_door_open', 'has_padlock', 'generator_fixed'], 'time': 2, 'voices':['not_done_with_tasks', 'shed_door_open', 'lock_gate', 'generator_needs_fix']}], audio='sfx/door.wav',),
                  Model('interior/door', name='ext2hang_door', tag='interactive', pos=(77.4,40.25,0.65), hpr=(202.3,0,0), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'hang_d2_t1'}], audio='sfx/door.wav'),
                  Model('exterior/screw1', name='screw1', tag='interactive', function=[functions.take_screw, {'screw_type':'shed'}]),
                  Model('exterior/screw2', name='screw2', tag='interactive', function=[functions.take_screw, {'screw_type':'shed'}]),
                  Model('exterior/screw3', name='screw3', tag='interactive', function=[functions.take_screw, {'screw_type':'shed'}]),
                  Model('exterior/screw4', name='screw4', tag='interactive', function=[functions.take_screw, {'screw_type':'shed'}]),
                  Model('exterior/plate', name='plate', tag='interactive', function=functions.click_plate),
                  Model('exterior/fuse', name='fuse', tag='interactive', function=functions.take_fuse),
                  Model('exterior/fusebox', name='fusebox', tag='interactive', function=functions.click_fusebox),
                  Model('exterior/padlock', name='padlock', pos=(62.83,-8.26,1.05), hpr=(250,0,90), tag='interactive', function=functions.take_padlock),
                  Model('exterior/screwdriver', name="screwdriver3", tag='interactive', function=[functions.take_screwdriver, {'g_bool':'has_screwdriver'}], audio='sfx/screwdriver.wav'),
                  ]

    #Hangar    
    elif scene_name[:-3] == 'hang_d1':
        models = [Model('interior/door', name='hang2ext_door', tag='interactive', pos=(-16.4,-9.4,0.4), hpr=(180,0,0), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'exte_d1_t1', 'player_pos':(76,37,-0.2)}], audio='sfx/door.wav'),
                  Model('hangar/screwdriver1', name="stardriver", tag='not_interactive'),
                  Model('hangar/screwdriver2', name="screwdriver2", tag='not_interactive'),
                  Model('hangar/snowcat_plate', name="plate", tag='not_interactive'),
                  Model('hangar/hscrew1', name="screw1", tag='not_interactive'),
                  Model('hangar/hscrew2', name="screw2", tag='not_interactive'),
                  Model('hangar/hscrew3', name="screw3", tag='not_interactive'),
                  Model('hangar/hscrew4', name="screw4", tag='not_interactive'),
                  ]
    elif scene_name[:-3] == 'hang_d2':
        models = [Model('interior/door', name='hang2ext_door', tag='interactive', pos=(-16.4,-9.4,0.4), hpr=(180,0,0), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'exte_d2_t1', 'player_pos':(76,37,-0.2)}], audio='sfx/door.wav'),
                  Model('hangar/screwdriver1', name="stardriver", tag='interactive', function=[functions.take_screwdriver, {'g_bool':'has_stardriver'}], audio='sfx/screwdriver.wav'),
                  Model('hangar/screwdriver2', name="screwdriver2", tag='interactive', function=[functions.take_screwdriver, {'g_bool':'has_screwdriver'}], audio='sfx/screwdriver.wav'),
                  Model('hangar/snowcat_plate', name="snowcat_plate", tag='interactive', function=functions.click_snowcat_plate),
                  Model('hangar/hscrew1', name="hscrew1", tag='interactive', function=[functions.take_screw, {'screw_type':'hang'}]),
                  Model('hangar/hscrew2', name="hscrew2", tag='interactive', function=[functions.take_screw, {'screw_type':'hang'}]),
                  Model('hangar/hscrew3', name="hscrew3", tag='interactive', function=[functions.take_screw, {'screw_type':'hang'}]),
                  Model('hangar/hscrew4', name="hscrew4", tag='interactive', function=[functions.take_screw, {'screw_type':'hang'}]),
                  Model('hangar/fuse', name='fuse', tag='interactive', function=functions.take_fuse),
                  ]
        
    else:
        models = []
    return models

def create_triggers(scene_name):
    triggers = []
    if scene_name[:4] == 'exte':
        triggers = [Trigger(65,-7,-1.65,10,functions.shed_snow, mode='enterleave')]
    if scene_name[:7]=='inte_d2':
        triggers = [Trigger(5,-9.5,0.1,1,functions.bathroom_window_trigger, mode='enter_once', name="BathroomWindowTrigger")]

    return triggers
