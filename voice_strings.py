from voice import *
import settings

subtitles = {
        #Conversation day 1
        'report' : "Station Omicron 35 South, ready to report.",
        'hq_greet' : "Your measurements, Omicron?",
        'measurements' : "Temperature: -18C, wind speed is 8 m/s, air pressure is 988 mb.",
        'hq_delay' : "Acknowledged, Omicron 35. There is a message from HQ: The replacement observer for Omicron 35 is delayed with yet another month.",
        'whatagain' : "What!? Again? You already delayed it once...",
        'hq_noted' : "Noted, Omicron 35, over and out.",
        'bastards' : "Those god damned... bastards.",
        'bruh' : 'bruh.',
        
        #Conversation day 2
        'hq_letyouknow' : "Uh, we'll let you know. Over and out.",
        'hq_what' : "Uh, what... It was fine. Over and out. ",
        'wait' : "Wait!",
        'hq_noise' : '*Noise*',
        'yourday' : "Uuh... How was your day?",
        'replacement' : "Any news about my replacement?",

        #Conversation day 3
        'missingsuit' : "One of my thermal suits has gone missing.",
        'hq_suit' : "Don't you have more than one? Report your measurements please.",
        'windy' : "It was quite windy today. I think a storm is coming up.",
        'hq_storm' : "Mhmm... Sure... Report your measurements, please.",
        'hq_whatnow' : "What now?",
        'yourname' : "Uh... What is your name?",
        'hq_basename' : "This is Tau One...",
        'realname' : "No, I mean what is YOUR name?",
        'hq_name' : "He is asking about my name!",
        'hq_stranger' : "Bare find på noget. Lad være med at snakke mere med ham!",
        'hq_smith' : 'Uh... Smith.',
        'someoneelse' : "Is there somebody there with you?",
        
        
        'toocold' : "It's way too cold outside. I need something to put on first.",
        'stuffouthere': "I still have stuff to do out here.",
        'needcan' : "I do not have anything to carry the fuel in.",
        'havefuel':"I already have fuel in the jerrycan.",
        'generatorneedsfuel':"The generator needs some fuel.",
        'haverefueled':"I have already refueled the generator.",
        'refueled':"There we go. Refueled.",
        'emptyjerrycan':"The jerrycan is empty. I need to refill it in the hangar.",
        'noclipboard' : "Oh! I need my clipboard.",
        'generatorgate' : "I need to close the door to the generator.",
        
        #Power cut segment
        'power_cut': "The power went off! Did I really forget to close the gate to the shed?",
        'see_from_bathroom': "I don't have to go outside right away. I can see it from the bathroom window.",
        'see_gate_damn': "It is open! Damn it! I must check on it.",
        'need_screwdriver' : "I need a screwdriver to get these screws off.",
        'wrong_screwdriver' : "This screwdriver doesn't fit the screws... Perhaps I can find one in the hangar.",
        'busted_fuse' : "The fuse is buted. Do I have a new somewhere?",
        'fuse_will_fit' : "It seems this fuse will fit the generator!",
        'fuse_fits' : "It fits! Let's hope it works. Now let's restart the generaotr.",
        'power_back' : "Yes! It worked! The power is back on.",
        'find_padlock' : "Hmm... Perhaps I should lock the door to make sure it doesn't open again. There should be a padlock somewhere in there.",
        'gate_locked' : "Now the gate won't open by itself. Back to bed!",
        'lock_gate' : "I better lock the shed gate before going inside.",
        'generator_needs_fix' : "I need to get the power on first...",
        
        #Sound effects below.
        'writing' : '',
        }

boilerplate_conv = {
    'd3_meas' : ['measurements', 'hq_noted', 'wait', 'hq_whatnow'],
    }

conversations = {'radio_day1' : ['report', 'hq_greet', 'measurements', 'hq_delay'],
                 'radio_day1_2' : ['whatagain', 'hq_noted', 'bastards'],
                 'radio_day1_3' : ['bruh'],

                 'radio_day2' : ['report', 'hq_greet', 'measurements', 'hq_noted', 'wait', 'hq_noise'],
                 'radio_day2_2' : ['yourday', 'hq_what'],
                 'radio_day2_3' : ['replacement', 'hq_letyouknow'],

                 'radio_day3' : ['report', 'hq_greet'],
                 'radio_day3_1' : boilerplate_conv['d3_meas'],
                 'radio_day3_2' : ['missingsuit', 'hq_suit']+boilerplate_conv['d3_meas'],
                 'radio_day3_3' : ['windy', 'hq_storm']+boilerplate_conv['d3_meas'],

                 'radio_day3_4' : ['replacement', 'hq_noise'],
                 'radio_day3_5' : ['yourname', 'hq_basename', 'realname', 'hq_name',
                                   'hq_stranger', 'hq_smith', 'someoneelse', 'hq_noise'],
                 
                 }


sounds = {'writing' : ['writing'],
          }

self_talk = {'shed_door_open' : ['generatorgate'],
             'not_done_with_tasks' : ['stuffouthere'],
             'no_clothes' : ['toocold'],
             'no_clipboard' : ['noclipboard'],
             'power_cut' : ['power_cut', 'see_from_bathroom'],
             'bathroom_window': ['see_gate_damn'],
             }

conversations.update(sounds)
conversations.update(self_talk)


