#navn + day
#scene - base
#collisions - base
#models - day
#functions - day

import settings

class Scene:

    def __init__(self, name, base_scene, base_collisions):
        self.name = name
        self.scene = base_scene
        self.collisions = base_collisions
        self.models = []
        self.add_to_settings()
        self.player_position = ()
        self.triggers = []

    def add_to_settings(self):
        settings.scenes[self.name] = self

    def find_model(self, model_name):
        model = [x for x in self.models if model_name in x.name]
        if model:
            if len(model) > 1:
                print("More models called {}.".format(model_name))
            model = model[0]
        return model
