from panda3d.core import (
    WindowProperties,
    DirectionalLight,
    OrthographicLens,
    AmbientLight,
    CollisionNode,
    CollisionBox,
    CollisionTraverser,
    CollisionHandlerPusher,
    CollisionHandlerQueue,
    GeomNode,
    CollisionRay,
    CollisionSphere,)

from direct.showbase import Audio3DManager
from direct.showbase.Transitions import Transitions
from direct.interval.IntervalGlobal import *
from model import *
import functions, scene_setup
import colliders, conversation
import text
import os, time

class SuperLoader():

    def __init__(self):
        self.audio3d_queue = []
        base.transition = Transitions(loader)
        self.txt = text.Text()

    def load(self, scene_name, init, newday=False):
        settings.envloading = True
        self.init = init
        if init:
            render.attach_new_node("audioemitters")
            scene_setup.create_scenes(settings.day)
            
        elif newday:
            self.destroy_models()
            self.destroy_scene()
            base.conversation.delete_voices()
            scene_setup.create_scenes(settings.day)
            
        self.stop_ambience()
        settings.environment = scene_name
        settings.scene = settings.scenes[scene_name]
        self.load_scene()
        self.load_collision(init)
        self.load_models()
        functions.let_it_snow()
        base.weather.stop_window_snow()
        base.weather.player_snow.disable()
        base.weather.control_all()
        if init:
            self.load_mouse()
            self.load_light()
            self.change_textures()
        if newday:
            self.load_audio3d()            
        
        self.start_ambience()
        self.show_env()

        self.init_functions()
        settings.envloading = False
        

    def load_scene(self):
        #Sets current base.scene
        scene = settings.scenes[settings.environment]
      
        scene_model = loader.loadModel(scene.scene)
        scene_model.setDepthOffset(0)
        scene_model.reparentTo(render)
        scene_model.setScale(0.5)
        scene_model.setPos(0,0,-1.8)
        base.scene = scene_model

    def destroy_scene(self):
        #unloads scene when changing day
        base.scene.remove_node()
        del base.scene

    def load_mouse(self):
        base.disableMouse()
        props = WindowProperties()
        props.setCursorHidden(True)
        base.win.requestProperties(props)

    def load_light(self): #Must be redone
        render.setShaderAuto()
        base.light = render.attachNewNode(DirectionalLight("dlight"))
        dlight = render.attachNewNode(DirectionalLight("dlight2"))
        dlight.setH(317)
        dlight.node().setColor((0.1, 0.1, 0.1, 1))
        lens = OrthographicLens()
        lens.setFov(45)
        lens.setNearFar(7.5, 20)
        lens.setFilmSize(12)
        base.light.node().setLens(lens)
        base.light.node().setShadowCaster(True, 1024, 1024)
        ambient_light = render.attachNewNode(AmbientLight("alight"))
        ambient_light.node().setColor((1, 1, 1, 1))
        base.light.lookAt(base.scene)
        #render.setLight(base.light)
        render.setLight(ambient_light)
        #render.setLight(dlight)

    def load_collision(self, init):
        if init:
            base.cTrav = CollisionTraverser()
            base.pusher = CollisionHandlerPusher()
            base.queue = CollisionHandlerQueue()

            #Camera
            pickerNode = CollisionNode('mouseRay')
            pickerNP = base.camera.attachNewNode(pickerNode)
            pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
            base.pickerRay = CollisionRay()
            pickerNode.addSolid(base.pickerRay)
            base.cTrav.addCollider(pickerNP, base.queue)
            
        self.load_collision_scene()

    def load_collision_scene(self):
        if settings.scenes[settings.environment].collisions:
            settings.scenes[settings.environment].collisions()

    def load_models(self):
        for model in settings.scene.models:
            if model.model.getTag('interactive'):
                model.model.reparent_to(base.interactive_objects)
            else:
                model.model.reparent_to(render)

    def destroy_models(self):
        print("Destroying models!")
        for model in settings.scene.models:
            model.model.removeNode()
            del model

    def init_functions(self):
        [x() for x in settings.start_functions]

    def show_env(self):
        if settings.show_env:
            self.txt.new_text(settings.environment)
            self.txt.new_pos(-1.2,1.43)
            self.txt.new_size(0.6)
            

    def load_audio3d(self):
        base.audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], base.player.camera)
        base.audio3d.attachListener(base.player.camera)
        base.sfxManagerList[0].setVolume(1)

        for a in self.audio3d_queue:
            sound = self.load_sound(a[0], a[1], a[2])
            sound.set_volume(a[4])
            if 'ambience' in a:
                a[3].ambience = sound
                a[3].ambience.setLoop(True)
            if 'player' in a:
                a[5].append(sound)
            else:
                a[3].audio = sound
            
        self.audio3d_queue = []

        base.conversation = conversation.Conversation()

    def stop_ambience(self):
        if not settings.scene:
            return
        for model in settings.scene.models:
            if model.ambience:
                model.ambience.stop()

    def start_ambience(self):
        for model in settings.scene.models:
            if model.ambience:
                if model.stop_ambience_condition():
                    continue
                    
                model.ambience.play()

    def load_sound_queue(self, arguments):
        #Arguments: sound, emitter, dropoff, object, volume
        #Audio3D may not be initialised at this point. Add sounds to loading queue.
        self.audio3d_queue.append(arguments)

    def load_sound(self, path, obj, *args):
        #Args[0] is dropoff factor
        if 'sounds/' not in path:
            path = 'sounds/'+path
        
        sound = base.audio3d.loadSfx(path)
        if str(sound)[:14] == 'NullAudioSound':
            if settings.report_load:
                print(f"Audio file {path} is not found")
            sound = base.audio3d.loadSfx('sounds/voices/default.wav')
            
        elif str(obj) == '**removed**':
            print("Oof! The object has beed removed!")

        if args:
            base.audio3d.setDropOffFactor(args[0])
        
        base.audio3d.attachSoundToObject(sound, obj)
        
        return sound

    def determine_texture_time(self):
        #Extract time from a texture path
        path = str(base.scene.find('**/+GeomNode').findTexture('*').filename)
        path = path.split('/')
        ind = path.index('textures')
        return path[ind+1]

    def change_texture_colour(self, model, r,g,b):
        #Model is model object - alpha is always 1
        if model:
            model.model.setColorScale(r,g,b,1)
        else:
            if settings.report_load:
                print("Could not change colour on", model)

    def get_geoms(self):
        time.sleep(1) #Not ideal, but needs to wait for base scene to change.
        geoms = base.scene.findAllMatches('**/+GeomNode')
        model_geoms = [x.model.findAllMatches('**/+GeomNode') for x in settings.scene.models]

        for m in model_geoms:
            for g in m:
                geoms.append(g)
        return geoms

    def change_textures(self, lightsout=False):      
        settings.texloading = True
        if settings.g_bools['power_off']:
            lightsout = True
            print("Lights out!")
        print("Changing textures")
        #Replace textures in scene accoring to settings time
        times = [None, 'Day', 'Evening', 'Night']
        time = times[settings.time]
        old_time = self.determine_texture_time()

        geoms = self.get_geoms()
        
        #Don't run function if not necessary
        if old_time == time and not self.init:
            if settings.sun: #Hmm
                print("No changes in textures.")
                settings.texloading = False
                return

        #Change texture for all geoms
        for geom in geoms:
            texture = geom.findTexture('*')
            
            if not texture:
                continue
            
            #Get file path as string
            path = str(texture.filename)
            cut = path.find('textures')
            path = path[cut:]

            list_path = path.split('/')
            list_path[1] = time
            new_path = '/'.join(list_path)            

            if geom.name == 'skydome':
                new_path = self.skybox_path()

            if lightsout:
                new_path = self.lights_out_path(new_path)
            
            elif not settings.sun and settings.time == 1:
                new_path = self.overcast_path(new_path)
            elif settings.time != 1:
                #Remove overcast - only used for day textures
                new_path = self.remove_overcast(new_path)
            
            try:
                t = loader.loadTexture(new_path)
                geom.setTexture(t, 1)
            except:
                if settings.report_load:
                    print("No new texture for %s found." % geom.name)
        
        if len(geoms) == 1:
            print("Scene is probably flattenedStrong. Cannot change textures.")
        if settings.sun != settings.change_sun:
            settings.change_sun = settings.sun
        settings.texloading = False

    def lights_out_path(self, path):
        #Find out whether or not path has overcast texture
        if os.path.isfile(path[:-4]+'LightsOut.png'):
            return path[:-4]+'LightsOut.png'
        return path        

    def overcast_path(self, path):
        #Find out whether or not path has overcast texture
        if os.path.isfile(path[:-4]+'Overcast.png'):
            return path[:-4]+'Overcast.png'
        return path

    def remove_overcast(self, path):
        #Remove "Overcast" from texture
        if 'Overcast' in path:
            return path[:-12]+'.png'
        return path

    def skybox_path(self):
        #Perhaps return different files, depending on day.
        path = 'overcast.png'
        if settings.time == 1 and settings.sun:
            path = 'd1t1.png'
        elif settings.time == 2:
            self.change_texture_colour(functions.find_model('skybox'), 0.4, 0.4, 0.4)
            self.change_texture_colour(functions.find_model('windows'), 0.5, 0.5, 0.5)
        elif settings.time == 3:
            self.change_texture_colour(functions.find_model('skybox'), 0.05, 0.05, 0.1)
            self.change_texture_colour(functions.find_model('windows'), 0.2, 0.2, 0.2)
        return 'textures/skymaps/'+path
