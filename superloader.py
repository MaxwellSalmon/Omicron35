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
                          function=self.door_function, pos=(10,1.35,0.4), scale=0.5, solid=True)
        base.clothes = Model('clothes', parent=base.scene, tag='interactive',
                             function=[self.put_on_clothes, {'test' : 'Her er en string'}])


#---------------Put these functions into a file on its own-----------------------------
    def door_function(self):
        if settings.clothes_on:
            if settings.environment == "inside":
                self.outside.reparentTo(self.render)
                self.scene.detachNode()
                settings.environment = "outside"
                self.door.setPos(6.5,1.2,0.4)
            else:
                self.outside.detachNode()
                self.scene.reparentTo(self.render)
                settings.environment = "inside"
                self.door.setX(0)
        else:
            print("Jeg skal have tøj på først")

    def put_on_clothes(self, test):
        settings.clothes_on = True
        self.clothes.set_z(10)
        print("Jeg har taget tøjet på")
        print(test)

        self.cutscene([{'h':0,'p':90,'r':0, 'x':-0.36, 'y':-11.36, 'z':-1.5, 'd':0},
                        {'p':0, 'y':-11,'z':-1, 'd':2},
                        {'h':85, 'p':-5, 'y':-10.5, 'd':2},
                        {'x':-2.3, 'p':-8, 'z':0, 'd':2}])






        
