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
import functions

class SuperLoader():

    def __init__(self):
        self.load_scene()
        self.load_mouse()
        self.load_light()
        self.load_collision()
        self.load_models()

    def load_scene(self): #Make individual methods for each scene
        scene = loader.loadModel("models/interior.egg")
        scene.setDepthOffset(1)
        scene.reparentTo(render)
        scene.setScale(0.5)
        scene.setPos(0,0,-1.8)
        base.scene = scene
        
        outside = loader.loadModel("models/exterior.egg")
        outside.setDepthOffset(1)
        outside.setScale(0.5)
        outside.setPos(-3,0,-1.8)
        base.outside = outside
        

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

        #Eksempler
        #Skab
##        skab = base.skab.attachNewNode(CollisionNode('skab'))
##        skab.node().addSolid(CollisionSphere(0,0,0.1,0.15))
##
##        #Lampe
##        lampe = base.lampe.attachNewNode(CollisionNode('lampe'))
##        lampe.node().addSolid(CollisionSphere(0,0,0.1,0.2))

    def load_models(self): #perhaps make into a loop taking info from another file.
        base.door = Model('door', parent=render, tag='interactive',
                          function=functions.door_function, pos=(10,1.35,0.4), scale=0.5, solid=True)
        base.clothes = Model('clothes', parent=base.scene, tag='interactive',
                             function=[functions.put_on_clothes, {'test' : 'Her er en string'}])


#---------------Put these functions into a file on its own-----------------------------
    






        
