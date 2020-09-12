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

from model import *
import functions, scene_setup
import colliders
import os

class SuperLoader():

    def __init__(self):
        self.audio3d_queue = []
        base.transition = Transitions(loader)

    def load(self, scene_name, init):
        if init:
            render.attach_new_node("audioemitters")
            scene_setup.create_scenes(settings.day)
        settings.environment = scene_name
        settings.scene = settings.scenes[scene_name]
        self.load_scene()
        self.load_collision(init)
        self.load_models()
        if init:
            self.load_mouse()
            self.load_light()
        

    def load_scene(self):
        #Sets current base.scene
        scene = settings.scenes[settings.environment]
        
        scene_model = loader.loadModel(scene.scene)
        scene_model.setDepthOffset(0)
        scene_model.reparentTo(render)
        scene_model.setScale(0.5)
        scene_model.setPos(0,0,-1.8)
        base.scene = scene_model
        

       # mat = Material()
       # mat.setAmbient((1,1,1,1))
       # main.scene.setMaterial(mat)

    def load_mouse(self):
        base.disableMouse()
        props = WindowProperties()
        props.setCursorHidden(True)
        base.win.requestProperties(props)

    def load_light(self): #Must be redone
        #Nødvendig for skygger og sådan.
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

    def load_models(self): #perhaps make into a loop taking info from another file.
        for model in settings.scene.models:
            if model.model.getTag('interactive'):
                model.model.reparent_to(base.interactive_objects)
            else:
                model.model.reparent_to(render)

    def load_audio3d(self):
        base.audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], base.player.camera)
        base.audio3d.attachListener(base.player.camera)

        for a in self.audio3d_queue:
            sound = self.load_sound(a[0], a[1], a[2])
            a[-1].audio = sound

        self.audio3d_queue = []

    def load_sound_queue(self, arguments):
        #Audio3D may not be initialised at this point. Add sounds to loading queue.
        self.audio3d_queue.append(arguments)

    def load_sound(self, path, obj, *args):
        #Args[0] is dropoff factor
        if 'sounds/' not in path:
            path = 'sounds/'+path
        
        sound = base.audio3d.loadSfx(path)
        if str(sound)[:14] == 'NullAudioSound':
            print(f"Audio file {path} is not found")
        base.audio3d.attachSoundToObject(sound, obj)

        if args:
            base.audio3d.setDropOffFactor(args[0])
        
        return sound

    def change_textures(self):
        #Replace textures in scene accoring to settings time
        times = [None, 'Day', 'Evening', 'Night']
        time = times[settings.time]
        old_time = ''
        geoms = base.scene.findAllMatches('**/+GeomNode')
        for geom in geoms:
            texture = geom.findTexture('*')
            if not texture:
                continue
            #I think strings are easier to work with, okay?
            path = str(texture.filename)
            cut = path.find('textures')
            path = path[cut:]
            
            if not old_time:
                for i in times[1:]:
                    if i in path:
                        old_time = i

            replace_index = path.find(old_time)
            replace_word = path[replace_index:replace_index+len(old_time)]
            new_path = path.replace(replace_word, time)

            try:
                t = loader.loadTexture(new_path)
                geom.setTexture(t, 1)
            except:
                print("There is no texture with filepath: ", new_path)
        if len(geoms) == 1:
            print("Scene is probably flattenedStrong. Cannot change textures.")






            
