from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText

#Use a DirectFrame
#Find out hot to make a prettier button
class ConversationGUI:

    def __init__(self):
        maps = loader.loadModel('textures/ui/button_maps')
        self.b = DirectButton(text=("  OK  ", "click!", "rolling over", "disabled"),
                 scale=0.1, pos=(0,0,-0.5), pressEffect = 0,
                    geom=(maps.find('**/test'),
                       maps.find('**/click'),
                       maps.find('**/hover'),
                       maps.find('**/click')))

