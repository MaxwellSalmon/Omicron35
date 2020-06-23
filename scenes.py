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

    def add_to_settings(self):
        settings.scenes[self.name] = self
