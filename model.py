from panda3d.core import CollisionNode, CollisionBox, TransparencyAttrib

import settings

class Model():

    def __init__(self, path, **kwargs):
        
        kg = kwargs.get

        if 'models/' not in path:
            path = 'models/'+path
        model = loader.load_model(path)
        name = path[7:]

        model.set_scale(0.5) #default scale
        model.set_pos(0, 0, -1.8)

        self.audio = None
        self.audio_emitter = None
        self.ambience = None
        self.stop_ambience_on = []
        self.audio_volume = 0.5
        self.tight_emitter = False
        self.tag = 'default'
        
        if kg('name'):
            #If interactive objects share the model, differentiate between them with custom name
            name = kg('name')
        if kg('pos'):
            p = kg('pos')
            model.set_pos(p[0], p[1], p[2])
        if kg('hpr'):
            hpr = kg('hpr')
            model.set_hpr(hpr[0], hpr[1], hpr[2])
        if kg('tag'):
            model.set_tag(kg('tag'), '1')
            if kg('tag') == 'place':
                model.place()
            self.tag = kg('tag')
        if kg('scale'):
            model.set_scale(kg('scale'))
        if kg('function'):
            settings.object_functions[str(name)] = kg('function')
        if kg('alpha'):
            model.setTransparency(TransparencyAttrib.MAlpha)
            model.setAlphaScale(kg('alpha'))
        
        #Sound
        if kg('tight_emitter'):
            self.tight_emitter = True
        if kg('audio'):
            #Attach audio source to model. Use audio emitter is model is not centered.
            self.create_audio_emitter(model)
            if self.audio_emitter:
                self.audio = base.superloader.load_sound_queue((kg('audio'), self.audio_emitter, 1, self, self.audio_volume))
            else:
                self.audio = base.superloader.load_sound_queue((kg('audio'), model, 1, self, self.audio_volume))
        if kg('ambience'):
            self.create_audio_emitter(model)
            if self.audio_emitter:
                self.ambience = base.superloader.load_sound_queue((kg('ambience'), self.audio_emitter, 1, self, self.audio_volume, 'ambience'))
            else:
                self.ambience = base.superloader.load_sound_queue((kg('ambience'), model, 1, self, self.audio_volume, 'ambience'))

        #Prevents ambience from playing at load - doesn't stop. 
        if kg('stop_ambience_on'):
            self.stop_ambience_on = kg('stop_ambience_on')
                
        if kg('culling'):
            if kg('culling') == 'both':
                model.setTwoSided(True)
        if kg('solid'):
            bmin, bmax = model.get_tight_bounds()
            bounds = bmax-bmin
            col = model.attachNewNode(CollisionNode(name))
            col.node().add_solid(CollisionBox((0,0,0), bounds[0], bounds[1], bounds[2]))

            if settings.show_col:
                col.show()

        self.model = model
        self.name = name

    def stop_ambience_condition(self):
        bools = [settings.g_bools[x] for x in self.stop_ambience_on]
        if True in bools:
            return True
        return False

    def set_tag(self, tag):
        if self.name=="fuse":
            print("old tag:", self.tag)
            print("new tag:", tag)
        self.model.clear_tag(self.tag)
        self.model.set_tag(tag, '1')
        self.tag = tag


    def create_audio_emitter(self, model):
        if not self.audio_emitter:
            pos = model.get_pos()
            if pos[0] == pos[1] == 0 or self.tight_emitter:
                audio_node = render.find('audioemitters')
                emitter = audio_node.attachNewNode('audioemitter')
                epos = self.get_tight_pos(model)
                emitter.set_pos(epos[0], epos[1], epos[2])
                self.audio_emitter = emitter

    def get_tight_pos(self, model):
        bmin, bmax = model.get_tight_bounds()
        avg = []
        
        for i in range(3):
            avg.append((bmin[i] + bmax[i]) / 2)
        return avg 

    def play_audio(self):
        if self.audio:
            self.audio.play()
