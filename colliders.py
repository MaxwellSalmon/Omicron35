#This script contains information about colliders.
#Everything is strings, as the code will be executed in superloader.py
from panda3d.core import CollisionNode, CollisionBox, CollisionSphere, CollisionCapsule

def house_interior(show):
    #Standard house interior
    kitchen = base.scene.attachNewNode(CollisionNode('kitchen'))
    kitchen.node().addSolid(CollisionCapsule(0,16.4,0, 10,16.4,0,2.5))
    kitchenwall = base.scene.attachNewNode(CollisionNode('kitchenwall'))
    kitchenwall.node().addSolid(CollisionCapsule(-12,17.5,0.4, -2,17.5,0.4, 1))
    radiowall = base.scene.attachNewNode(CollisionNode('radiowall'))
    radiowall.node().addSolid(CollisionCapsule(-12,17.75,0.5, -12,-22.5,0.5,1))
    bedroomwall = base.scene.attachNewNode(CollisionNode('bedroomwall'))
    bedroomwall.node().addSolid(CollisionCapsule(-12,-22.5,0.5, 12,-22.5, 0.5,1))
    wcwall = base.scene.attachNewNode(CollisionNode('wcwall'))
    wcwall.node().addSolid(CollisionCapsule(12,-22.5,0.5, 12,-5,0.5,1))
    furnacewall = base.scene.attachNewNode(CollisionNode('furnacewall'))
    furnacewall.node().addSolid(CollisionCapsule(12,3,0.5, 12,17.5,0.5,1))
    broomdivider = base.scene.attachNewNode(CollisionNode('broomdivider'))
    broomdivider.node().addSolid(CollisionCapsule(-3.25,-6.1,0.5,3.8,-6.1,0.5,1))
    broomdivider2 = base.scene.attachNewNode(CollisionNode('broomdivider2'))
    broomdivider2.node().addSolid(CollisionCapsule(-12,-6.1,0.5, -8.2,-6.1,0.5,1))
    wcdivider = base.scene.attachNewNode(CollisionNode('wcdivider'))
    wcdivider.node().addSolid(CollisionCapsule(12,-6.1,0.5, 9,-6.1,0.5,1))
    bed = base.scene.attachNewNode(CollisionNode('bed'))
    bed.node().addSolid(CollisionCapsule(0,-8.5,1, 0,-22,1,3))
    table = base.scene.attachNewNode(CollisionNode('table'))
    table.node().addSolid(CollisionCapsule(-9,4.5,0.5, -9,7.5,0.5,2.5))
    dresser = base.scene.attachNewNode(CollisionNode('dresser'))
    dresser.node().addSolid(CollisionCapsule(-10,10,0.5, -10,17,0.5,1))
    bookshelf = base.scene.attachNewNode(CollisionNode('bookshelf'))
    bookshelf.node().addSolid(CollisionCapsule(-0.7,-5,0.5, 2.4,-5,0.5,1))
    entwall1 = base.scene.attachNewNode(CollisionNode('entwall1'))
    entwall1.node().addSolid(CollisionCapsule(12,5.5,0.5, 20,5.5,0.5,1))
    entwall2 = base.scene.attachNewNode(CollisionNode('entwall2'))
    entwall2.node().addSolid(CollisionCapsule(12,-6,0.5, 20,-6,0.5,1))
    entwall3 = base.scene.attachNewNode(CollisionNode('entwall3'))
    entwall3.node().addSolid(CollisionCapsule(20,5.5,0.5, 20,-6,0.5,1))
    broomarchives = base.scene.attachNewNode(CollisionNode('broomarchives'))
    broomarchives.node().addSolid(CollisionCapsule(-10.8,-6.5,0.5,-10.8,-10,0.5,1.5))
    broomtable = base.scene.attachNewNode(CollisionNode('broomtable'))
    broomtable.node().addSolid(CollisionCapsule(-9.4,-17.5,0.5, -9.4,-20,0.5,2))
    wcarchives = base.scene.attachNewNode(CollisionNode('wcarchives'))
    wcarchives.node().addSolid(CollisionCapsule(10.5,-7.5,0.5,10.5,-9,0.5,1.5))
    
    if show:
        kitchenwall.show()
        kitchen.show()
        radiowall.show()
        bedroomwall.show()
        wcwall.show()
        furnacewall.show()
        broomdivider.show()
        broomdivider2.show()
        wcdivider.show()
        bed.show()
        table.show()
        dresser.show()
        bookshelf.show()
        entwall1.show()
        entwall2.show()
        entwall3.show()
        broomarchives.show()
        broomtable.show()
        wcarchives.show()
    
