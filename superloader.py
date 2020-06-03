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

from model import *
import functions, scene_setup
import colliders

class SuperLoader():

    def load(self, scene_name, init):
        if init:
            scene_setup.create_scenes(settings.day)
        settings.environment = scene_name
        self.load_scene()
        self.load_collision()
        self.load_models()
        if init:
            self.load_mouse()
            self.load_light()
        


    def load_scene(self):
        #Sets current base.scene
        scene = settings.scenes[settings.environment]
        
        scene_model = loader.loadModel(scene.scene)
        scene_model.setDepthOffset(1)
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
        ambient_light.node().setColor((0.7, 0.7, 0.7, 1))
        base.light.lookAt(base.scene)
        render.setLight(base.light)
        render.setLight(ambient_light)
        render.setLight(dlight)

    def load_collision(self):
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
        for model in settings.scenes[settings.environment].models:
            model.model.reparent_to(render)




        
