from direct.interval.IntervalGlobal import SoundInterval
import voice_strings

class Voice:

    def __init__(self, emitter):
        self.emitter = emitter
        self.intervals = []
        self.subtitles = []
        self.disabled = False

    def load_audio(self, file):
        if not self.disabled:
            try:
                path = 'sounds/voices/'+file
                clip = base.superloader.load_sound(path, self.emitter)
                self.intervals.append(SoundInterval(clip))
                self.subtitles.append(voice_strings.subtitles[file[:-4]])
            except:
                print("Sound {} not found.".format(file))
                path = 'sounds/voices/default.wav'
                clip = base.superloader.load_sound(path, self.emitter)
                self.intervals.append(SoundInterval(clip))
                self.subtitles.append(voice_strings.subtitles[file[:-4]])

    def play(self, index):
        self.disable()
        if len(self.clips) >= index-1:
            self.clips[index].play()
        else:
            print("Invalid index for audio clip.")

    def clear_audio(self):
        self.intervals = []
        self.subtitles = []

    def disable(self):
        self.disabled = True

    def enable(self):
        self.clear_audio()
        self.disabled = False
        



