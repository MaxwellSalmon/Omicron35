from direct.gui.DirectGui import *
from panda3d.core import WindowProperties
from direct.gui.OnscreenText import OnscreenText
import settings
import random

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

    def update_text(self, strings, transition_states):
        assert len(strings) == len(self.buttons)
        
        for index, i in enumerate(zip(self.buttons, strings)):
            i[0]['text'] = i[1]
            #i[0]['command'] = self.set_p
            i[0]['command'] = self.transition

            #Choose button index as p value
            #i[0]['extraArgs'] = [index, prog[index]]
            i[0]['extraArgs'] = [transition_states[index]]

    def toggle_visibility(self):
        for btn in self.buttons:
            if self.shown:
                btn.hide()
            else:
                if btn['text']:
                    btn.show()

        self.shown = not self.shown
        base.free_mouse()

    def shuffle_buttons(self, strings, transitions):
        temp = list(zip(strings, transitions))
        random.shuffle(temp)
        strings, transitions = zip(*temp)
        return strings, transitions

    def transition(self, state):
        settings.conversation_state = settings.conversation_states[state]
        self.toggle_visibility()
        

##    def set_p(self, p, prog): #p is not used.
##        settings.conversation_path += 1
##        settings.conversation_progress = prog
##        conversation_manager.talk_new_path()
##        self.toggle_visibility()
        
    #Strings are shown on button, transition states show which state they go to.
    def choices(self, strings, transition_states):
        strings, transition_states = self.shuffle_buttons(strings, transition_states)
        if not self.shown:
            self.create_buttons(len(strings))
            self.update_text(strings, transition_states)


        
        
        


