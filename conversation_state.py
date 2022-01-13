import settings
import conversation_gui

class ConversationState():

    def __init__(self, name, audio_sequence, button_strings, transitions, end_state=False):
        '''string statename, voice_strings audio sequence,
        list button text strings, list transitions state strings'''
        self.name = name
        self.audio_sequence = audio_sequence
        self.button_strings = button_strings
        self.transitions = transitions
        self.end_state = end_state
        self.have_spoken = False

        self.assert_parameters()

    def create_buttons(self):
        base.conv_gui.choices(self.button_strings, self.transitions)

    def manage(self):
        #Show buttons or start speech?
        if self.have_spoken:
            if self.end_state:
                settings.conversation_ongoing = False
                settings.conversation_state = settings.conversation_states[self.transitions]
            else:
                self.create_buttons()
        else:
            self.talk()

    def talk(self):
        settings.conversation_ongoing = True
        base.conversation.talk(self.audio_sequence)
        self.have_spoken = True

    def assert_parameters(self):
        if self.transitions and self.button_strings:
            assert len(self.button_strings) == len(self.transitions), f"ConversationState {self.name}: Mismatch between numbers buttons and transitions!"
        if self.end_state and self.transitions:
            if type(self.transitions) == list:
                assert len(self.transitions)==1, f"ConversationState {self.name}: End state needs exactly one transition!"
                self.transition = self.transition[0]
        if None in self.transitions:
            print(f"ConversationState {self.name}: Warning! 'None' found in transitions.")
        if None in self.button_strings:
            print(f"ConversationState {self.name}: Warning! 'None' found in button strings.")
        
        
    
    
