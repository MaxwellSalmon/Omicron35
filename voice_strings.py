from voice import *
from direct.interval.IntervalGlobal import *
import settings

player_voice = None
radio_voice = None
conv_sequence = Sequence()

subtitles = {
        'report' : "Station Omicron 35 South, ready to report.",
        'hq_greet' : "Your measurements, Omicron?",
        'measurements' : "Temperature: -18C, wind speed is 8 m/s, air pressure is 988 mb.",
        'hq_delay' : "Acknowledged, Omicron 35. There is a message from HQ: The replacement observer for Omicron 35 is delayed with yet another month.",
        'whatagain' : "What!? Again? You already delayed it once...",
        'hq_noted' : "Noted, Omicron 35, over and out.",
        'bastards' : "Those god damned... bastards.",
        'toocold' : "It's way too cold outside. I need something to put on first.",
        'stuffouthere': "I still have stuff to do out here.",
        'needcan' : "I do not have anything to carry the fuel in.",
        'havefuel':"I already have fuel in the jerrycan.",
        'generatorneedsfuel':"The generator needs some fuel.",
        'haverefueled':"I have already refueled the generator.",
        'refueled':"There we go. Refueled.",
        'emptyjerrycan':"The jerrycan is empty. I need to refill it in the hangar.",
        
        #Sound effects below.
        'writing' : '',
        }

conversations = {'radio_day1' : ['report', 'hq_greet', 'measurements',
                                 'hq_delay', 'whatagain', 'hq_noted', 'bastards'],
                 'no_clothes' : ['toocold'],
                 'no_clipboard' : ['refueled'], #Placeholder for not having clipboard
                 'not_done_with_tasks' : ['stuffouthere'],
                 'shed_door_open' : ['refueled'], #Placeholder

                 #Just sound effects emitted from player below here. Not actual voices.
                 'writing' : ['writing'],
                 }

def load_voices():
    global player_voice, radio_voice

    player_voice = Voice(base.player.camera)
    radio_voice = Voice(settings.scene.models[8].model) #Change, so it doesn't use 8

def talk(conversation):
    global conv_sequence

    if conv_sequence.isPlaying():
        return

    conv_sequence = Sequence()

    if conversation not in conversations:
        lines = [conversation]
    else:
        lines = conversations[conversation]

    for string in lines:
        if string[:3] == 'hq_':
            radio_voice.load_audio(string+'.wav')
            conv_sequence.append(Func(base.text.new_colour, (0.2,0.8,0.1,1)))
            conv_sequence.append(Func(base.text.new_text, radio_voice.subtitles[-1]))
            conv_sequence.append(radio_voice.intervals[-1])
        else:
            player_voice.load_audio(string+'.wav')
            conv_sequence.append(Func(base.text.new_colour, (1,1,1,1)))
            conv_sequence.append(Func(base.text.new_text, player_voice.subtitles[-1]))
            conv_sequence.append(player_voice.intervals[-1])

    conv_sequence.append(Func(base.text.new_text, ''))
    conv_sequence.append(Func(player_voice.enable))
    conv_sequence.start()
        
