import settings

#Disse funktioner bør følge et state-system, så jeg undgår utallige
#if-statements. F.eks. state start er uden tøj og indenfor. Brug kun tid på
#det, hvis det kan spare nok tid. 

def door_function():
    if settings.clothes_on: #Lav evt om til en change_Scene funktion
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

def change_scene(to_scene):
    print(to_scene)
    for model in settings.scenes[settings.environment].models:
        model.model.detachNode()
    base.scene.detachNode()
    base.superloader.load(to_scene, None)
    base.scene.flattenStrong()

def put_on_clothes(test):
    settings.clothes_on = True
    base.clothes.model.set_z(10)
    print("Jeg har taget tøjet på")
    print(test)

    base.cutscene([{'h':0,'p':90,'r':0, 'x':-0.36, 'y':-11.36, 'z':-1.5, 'd':0},
                    {'p':0, 'y':-11,'z':-1, 'd':2},
                    {'h':85, 'p':-5, 'y':-10.5, 'd':2},
                    {'x':-2.3, 'p':-8, 'z':0, 'd':2}])
