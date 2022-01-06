from direct.interval.IntervalGlobal import *
import voice_strings, voice
import settings

class Conversation:

    def __init__(self):
        self.player_voice = None
        self.radio_voice = None
        self.conv_sequence = Sequence()
        self.load_voices()

    def delete_voices(self):
        del self.player_voice
        del self.radio_voice

    def load_voices(self):
        self.player_voice = voice.Voice(base.player.camera)
        if settings.environment[:4] == 'inte': #Should fix this
            radio = [x for x in settings.scene.models if "radio" in x.name]
            if radio:
                self.radio_voice = voice.Voice(radio[0].model)
            else:
                print("Conversation.py: Oops! Radio model could not be fetched.")

    def ready_lines(self, conversation):
        if conversation not in voice_strings.conversations:
            lines = [conversation]
        else:
            lines = voice_strings.conversations[conversation]

        return lines
        

    def talk(self, conversation): #Has to be redone, perhaps.
        if settings.skip_convs:
            return
        if self.conv_sequence.isPlaying():
            return
        self.conv_sequence = Sequence()

        lines = self.ready_lines(conversation)

        for string in lines:
            if string[:3] == 'hq_':
                self.radio_voice.load_audio(string+'.wav')
                self.conv_sequence.append(Func(base.text.new_colour, (0.2,0.8,0.1,1)))
                self.conv_sequence.append(Func(base.text.new_text, self.radio_voice.subtitles[-1]))
                self.conv_sequence.append(self.radio_voice.intervals[-1])
            else:
                self.player_voice.load_audio(string+'.wav')
                self.conv_sequence.append(Func(base.text.new_colour, (1,1,1,1)))
                self.conv_sequence.append(Func(base.text.new_text, self.player_voice.subtitles[-1]))
                self.conv_sequence.append(self.player_voice.intervals[-1])

        self.conv_sequence.append(Func(base.text.new_text, ''))
        self.conv_sequence.append(Func(self.player_voice.enable))
        self.conv_sequence.start()
