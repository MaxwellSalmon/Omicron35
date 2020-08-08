#This script contains information about colliders.
#Each function is tied to a scene.
from panda3d.core import CollisionNode, CollisionBox, CollisionSphere, CollisionCapsule
import settings

def house_interior():
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
    
    if settings.show_col:
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

def exterior():
    #Standard exterior
    houseback = base.scene.attachNewNode(CollisionNode('houseback'))
    houseback.node().addSolid(CollisionCapsule(-12,17.75,0.5, -12,-22.5,0.5,1))
    kitchenwall = base.scene.attachNewNode(CollisionNode('kitchenwall'))
    kitchenwall.node().addSolid(CollisionCapsule(-11.8,17.5,0.4, 12,17.5,0.4, 1))
    bedroomwall = base.scene.attachNewNode(CollisionNode('bedroomwall'))
    bedroomwall.node().addSolid(CollisionCapsule(-12,-22.5,0.5, 12,-22.5, 0.5,1))
    wcwall = base.scene.attachNewNode(CollisionNode('wcwall'))
    wcwall.node().addSolid(CollisionCapsule(12,-22.5,0.5, 12,-5,0.5,1))
    furnacewall = base.scene.attachNewNode(CollisionNode('furnacewall'))
    furnacewall.node().addSolid(CollisionCapsule(12,3,0.5, 12,17.5,0.5,1))
    entwall1 = base.scene.attachNewNode(CollisionNode('entwall1'))
    entwall1.node().addSolid(CollisionCapsule(12,5.5,0.5, 20,5.5,0.5,1))
    entwall2 = base.scene.attachNewNode(CollisionNode('entwall2'))
    entwall2.node().addSolid(CollisionCapsule(12,-7.5,0.5, 20,-7.5,0.5,1))
    entwall3 = base.scene.attachNewNode(CollisionNode('entwall3'))
    entwall3.node().addSolid(CollisionCapsule(20,5.5,0.5, 20,-7,0.5,1))
    antenna = base.scene.attachNewNode(CollisionNode('antenna'))
    antenna.node().addSolid(CollisionSphere(-13.2,49.8,0.5,3.5))
    shedwall1 = base.scene.attachNewNode(CollisionNode('shedwall1'))
    shedwall1.node().addSolid(CollisionCapsule(116,-13.5,0.5, 134.5,-20.8,0.5, 1))
    shedwall2 = base.scene.attachNewNode(CollisionNode('shedwall2'))
    shedwall2.node().addSolid(CollisionCapsule(134.5,-20.8,0.5, 142.6,0.7,0.5, 1))
    shedwall3 = base.scene.attachNewNode(CollisionNode('shedwall3'))
    shedwall3.node().addSolid(CollisionCapsule(142.6,0.7,0.5, 124,7.7,0.5, 1))
    shedwall4 = base.scene.attachNewNode(CollisionNode('shedwall4'))
    shedwall4.node().addSolid(CollisionCapsule(124,7.7,0.5, 120.5,-0.5,0.5, 1))
    shedwall5 = base.scene.attachNewNode(CollisionNode('shedwall5'))
    shedwall5.node().addSolid(CollisionCapsule(116,-13.5,0.5, 118,-7.8,0.5, 1))
    generator = base.scene.attachNewNode(CollisionNode('generator'))
    generator.node().addSolid(CollisionCapsule(129.8,-6.8,0.5, 136,-9,0.5, 2.5))
    shedstuff = base.scene.attachNewNode(CollisionNode('shedstuff'))
    shedstuff.node().addSolid(CollisionCapsule(140.6,0,0.5, 124,5.5,0.5, 1.2))
    shedstuff2 = base.scene.attachNewNode(CollisionNode('shedstuff2'))
    shedstuff2.node().addSolid(CollisionCapsule(140.6,0,0.5, 139,-4.4,0.5, 1.2))
    shedbox = base.scene.attachNewNode(CollisionNode('shedbox'))
    shedbox.node().addSolid(CollisionSphere(133,-18,0.5,1.5))
    shedshelves = base.scene.attachNewNode(CollisionNode('shedshelves'))
    shedshelves.node().addSolid(CollisionCapsule(126,-16,0.5, 118,-13,0.5, 1))
    hangarwall1 = base.scene.attachNewNode(CollisionNode('hangarwall1'))
    hangarwall1.node().addSolid(CollisionCapsule(158,72,0.5, 220,97.2,0.5, 2))
    hangarwall2 = base.scene.attachNewNode(CollisionNode('hangarwall2'))
    hangarwall2.node().addSolid(CollisionCapsule(220,97.2,0.5, 198,150,0.5, 2))
    hangarwall3 = base.scene.attachNewNode(CollisionNode('hangarwall3'))
    hangarwall3.node().addSolid(CollisionCapsule(198,150,0.5, 136,125,0.5, 2))
    hangarwall4 = base.scene.attachNewNode(CollisionNode('hangarwall4'))
    hangarwall4.node().addSolid(CollisionCapsule(158,72,0.5, 136,125,0.5, 2))

    if settings.show_col:
        houseback.show()
        kitchenwall.show()
        bedroomwall.show()
        wcwall.show()
        furnacewall.show()
        entwall1.show()
        entwall2.show()
        entwall3.show()
        antenna.show()
        shedwall1.show()
        shedwall2.show()
        shedwall3.show()
        shedwall4.show()
        shedwall5.show()
        generator.show()
        shedstuff.show()
        shedstuff2.show()
        shedbox.show()
        shedshelves.show()
        hangarwall1.show()
        hangarwall2.show()
        hangarwall3.show()
        hangarwall4.show()
    
def hangar():
    pass

    if settings.show_col:
        pass
