import scenes, settings, colliders, functions
import os
from model import *

def setup(name, base_scene, base_colliders):
    temp_scene = scenes.Scene(name, base_scene, base_colliders)
    temp_scene.models = create_models(name)   
    
    settings.scenes[name] = temp_scene

def create_scenes(day):
    if day == 1:
        #Day 1, morning
        setup("inte_d1_t1", os.path.join('models', 'interior.egg'), colliders.house_interior)

        setup("hang_d1_t1", os.path.join('models', 'hangar.egg'), None)

        setup("exte_d1_t1", os.path.join('models', 'exterior.egg'), None)

def create_models(scene_name):
    if scene_name == 'inte_d1_t1':
        models = [Model('door', tag='interactive', pos=(10,1.35,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'exte_d1_t1'}]),
                  Model('clothes', tag='interactive',
                        function=[functions.put_on_clothes, {'test' : 'Her er en string'}]),
                  ]
    elif scene_name == 'exte_d1_t1':
        models = [Model('door', name='ext_door', tag='interactive', pos=(14,1.35,0.4), scale=0.5, solid=True,
                        function=[functions.change_scene, {'to_scene':'inte_d1_t1'}]),]
    else:
        models = []
        
    return models
