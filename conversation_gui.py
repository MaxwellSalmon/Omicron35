from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText

class ConversationGUI:
    #5,30
    def __init__(self, num_buttons):
        self.shown = True
        self.buttons = []
        self.create_buttons(num_buttons)

    def create_buttons(self, number):
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

    def update_text(self, strings):
        assert len(strings) == len(self.buttons)
        
        for i in zip(self.buttons, strings):
            i[0]['text'] = i[1]

    def toggle_visibility(self):
        for btn in self.buttons:
            if self.shown:
                btn.hide()
            else:
                if btn['text']:
                    btn.show()

        self.shown = not self.shown
        


