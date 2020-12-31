from direct.gui.DirectGui import *
from panda3d.core import WindowProperties
from direct.gui.OnscreenText import OnscreenText
import settings
import functions

class ConversationGUI:
    #5,30
    def __init__(self, num_buttons):
        self.shown = True
        self.buttons = []
        self.create_buttons(num_buttons)

    def create_buttons(self, number):
        self.buttons = []
        maps = loader.loadModel('textures/ui/button')
        for i in range(number):
            self.buttons.append(DirectButton(text="Placeholder",
                                  scale=0.1, pos=(0,0,-0.5-(i*0.12)), pressEffect = 0, relief=None,
                                  text_fg=(255,255,255,1), text_shadow=(0,0,0,0.8),
                                  text_scale=0.8, text_pos=(0,-0.2),
                                  geom=(maps.find('**/btn1'), maps.find('**/btn3'),
                                        maps.find('**/btn2'),maps.find('**/btn1'))
                                  ))
        self.toggle_visibility()

    def update_text(self, strings, p_vals=None):
        assert len(strings) == len(self.buttons)
        
        for index, i in enumerate(zip(self.buttons, strings)):
            i[0]['text'] = i[1]
            i[0]['command'] = self.set_p

            #Choose button index as p value if not told otherwise.
            if not p_vals:
                i[0]['extraArgs'] = [index]
            else:
                i[0]['extraArgs'] = p_vals[index]

    def toggle_visibility(self):
        for btn in self.buttons:
            if self.shown:
                btn.hide()
            else:
                if btn['text']:
                    btn.show()

        self.shown = not self.shown
        base.free_mouse()

    def set_p(self, p):
        settings.conversation_p = p
        settings.conversation_progress += 1
        functions.talk_new_path()
        self.toggle_visibility()
        

    def choice(self, strings):
        if not self.shown:
            self.create_buttons(len(strings))
            self.update_text(strings)


        
        
        


