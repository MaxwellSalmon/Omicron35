from voice import *
from direct.interval.IntervalGlobal import *
import settings

voice_strings = {}
voice_audio = {}

player_voice = None
radio_voice = None

def load_strings():
    global voice_strings, voice_audio, player_voice, radio_voice

    player_voice = Voice(base.player.camera)
    radio_voice = Voice(settings.scene.models[8].model) #Change, so it doesn't use 8

    #Have only the strings, use the file name as key
    voice_strings = {
        'report' : "Station Omicron 35 South, ready to report.",
        'hq_greet' : "Your measurements, Omicron?",
        'measurements' : "Temperature: -18C, wind speed is 8 m/s, air pressure is 988 mb.",
        'hq_delay' : "Acknowledged, Omicron 35. There is a message from HQ: The replacement observer for Omicron 35 is delayed with yet another month.",
        'whatagain' : "What!? Again? You already delayed it once...",
        'hq_noted' : "Noted, Omicron 35, over and out.",
        'bastards' : "Those god damned... bastards."
        }

    voice_audio = {
        'radio1' : player_voice
        }

conversations = {}

#Testing
def talk():

    player_voice.load_audio('report.wav')
    player_voice.load_audio('measurements.wav')
    player_voice.load_audio('whatagain.wav')
    player_voice.load_audio('bastards.wav')

    radio_voice.load_audio('hq_greet.wav')
    radio_voice.load_audio('hq_delay.wav')
    radio_voice.load_audio('hq_noted.wav')

    Sequence(Func(player_voice.play, 0),
             Func(base.text.new_text, voice_strings['report']),
             Wait(player_voice.lengths[0]),
             
             Func(radio_voice.play, 0),
             Func(base.text.new_text, voice_strings['hq_greet']),
             Wait(radio_voice.lengths[0]),

             Func(player_voice.play, 1),
             Func(base.text.new_text, voice_strings['measurements']),
             Wait(player_voice.lengths[1]),

             Func(radio_voice.play, 1),
             Func(base.text.new_text, voice_strings['hq_delay']),
             Wait(radio_voice.lengths[1]),

             Func(player_voice.play, 2),
             Func(base.text.new_text, voice_strings['whatagain']),
             Wait(player_voice.lengths[2]),

             Func(radio_voice.play, 2),
             Func(base.text.new_text, voice_strings['hq_noted']),
             Wait(radio_voice.lengths[2]),

             Func(player_voice.play, 3),
             Func(base.text.new_text, voice_strings['bastards']),
             Wait(player_voice.lengths[3]),
             Func(base.text.new_text, ""),
             ).start()

#  player_voice.load_audio('report.wav')
#  player_voice.play()
#  print(player_voice.get_length())
