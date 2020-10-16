
class Voice:

    def __init__(self, emitter):
        self.clips = []
        self.lengths = []
        self.emitter = emitter

    def load_audio(self, file):
        path = 'sounds/voices/'+file
        self.clips.append(base.superloader.load_sound(path, self.emitter))
        self.lengths.append(self.clips[-1].length())

    def play(self, index):
        if len(self.clips) >= index-1:
            self.clips[index].play()
        else:
            print("Invalid index for audio clip.")

    def clear_audio(self):
        self.clips = []
        self.lengths = []



