from voice import *
import settings

subtitles = {
        #Conversation day 1
        'day1/report' : "Station Omicron 35 South, ready to report.",
        'day1/hq_greet' : "Your measurements, Omicron?",
        'day1/measurements' : "Temperature: -18C, wind speed is 8 m/s, air pressure is 988 mb.",
        'day1/hq_delay' : "Acknowledged, Omicron 35. There is a message from HQ: The replacement observer for Omicron 35 is delayed with yet another month.",
        'day1/whatagain' : "What!? Again? You already delayed it once...",
        'day1/hq_noted' : "Noted, Omicron 35, over and out.",
        'day1/bastards' : "Those god damned... bastards.",
        'day1/please_hurry' : 'But it has already been delayed once... Can you please hurry up?',
        'day1/goddamnit' : 'Goddamnit...',
        
        #Conversation day 2
        'day2/hq_letyouknow' : "Uh, we'll let you know. Over and out.",
        'day2/hq_what' : "Uh, what... It was fine. Over and out. ",
        'day2/hq_noted' : "Noted, Omicron. Same time tomorrow.",
        'day2/wait' : "Wait!",
        'day2/hq_noise' : '*Noise*',
        'day2/yourday' : "Uuh... How was your day?",
        'day2/today_i' : "You wouldn't believe what happended tod-",
        'day2/hq_turn_off' : '*Disconnect Noise*',
        'day2/replacement' : "Any news about my replacement?",
        'day2/cant_believe' : "I can't believe these fucking assholes!",
        'day2/did_they_hear_that' : "Shit, they weren't supposed to hear that!",
        'day2/im_lonely' : "I'm lonely...",
        
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
        
        
        'self/toocold' : "It's way too cold outside. I need something to put on first.",
        'self/stuffouthere': "I still have stuff to do out here.",
        'self/needcan' : "I do not have anything to carry the fuel in.",
        'self/havefuel':"I already have fuel in the jerrycan.",
        'self/generatorneedsfuel':"The generator needs some fuel.",
        'self/haverefueled':"I have already refueled the generator.",
        'self/refueled':"There we go. Refueled.",
        'self/emptyjerrycan':"The jerrycan is empty. I need to refill it in the hangar.",
        'self/noclipboard' : "Oh! I need my clipboard.",
        'self/generatorgate' : "I need to close the door to the generator.",
        
        #Power cut segment
        'self/power_cut': "The power went off! Did I really forget to close the gate to the shed?",
        'self/see_from_bathroom': "I don't have to go outside right away. I can see it from the bathroom window.",
        'self/see_gate_damn': "It is open! Damn it! I must check on it.",
        'self/generator_off_think': "The generator has turned off. I hope it will just start again.",
        'self/need_screwdriver' : "I need a screwdriver to get these screws off.",
        'self/wrong_screwdriver' : "This screwdriver doesn't fit the screws... Perhaps I can find one in the hangar.",
        'self/busted_fuse' : "The fuse is buted. Do I have a new somewhere?",
        'self/fuse_will_fit' : "It seems this fuse will fit the generator!",
        'self/fuse_fits' : "It fits! Let's hope it works. Now let's restart the generaotr.",
        'self/power_back' : "Yes! It worked! The power is back on.",
        'self/find_padlock' : "Hmm... Perhaps I should lock the door to make sure it doesn't open again. There should be a padlock somewhere in there.",
        'self/gate_locked' : "Now the gate won't open by itself. Back to bed!",
        'self/lock_gate' : "I better lock the shed gate before going inside.",
        'self/generator_needs_fix' : "I need to get the power on first...",
        
        #Sound effects below.
        'writing' : '',
        'Electricity_Spark' : '',
        }

boilerplate_conv = {
    'd3_meas' : ['day1/measurements', 'day1/hq_noted', 'wait', 'hq_whatnow'],
    }

conversations = {'radio_day1' : ['day1/report', 'day1/hq_greet', 'day1/measurements', 'day1/hq_delay'],
                 'radio_day1_2' : ['day1/whatagain', 'day1/hq_noted', 'day1/bastards'],
                 'radio_day1_3' : ['day1/please_hurry', 'day1/hq_noted', 'day1/goddamnit'],

                 'radio_day2' : ['day1/report', 'day1/hq_greet', 'day1/measurements', 'day2/hq_noted', 'day2/wait', 'day2/hq_noise'],
                 'radio_day2_2' : ['day2/yourday', 'day2/hq_what', 'day2/today_i', 'day2/hq_turn_off'],
                 'radio_day2_3' : ['day2/replacement', 'day2/hq_letyouknow'],
                 'radio_day2_4' : ['day2/cant_believe', 'day2/hq_turn_off', 'day2/did_they_hear_that'],
                 'radio_day2_5' : ['day2/im_lonely', 'day2/hq_turn_off'],

                 'radio_day3' : ['day1/report', 'day1/hq_greet'],
                 'radio_day3_1' : boilerplate_conv['d3_meas'],
                 'radio_day3_2' : ['missingsuit', 'hq_suit']+boilerplate_conv['d3_meas'],
                 'radio_day3_3' : ['windy', 'hq_storm']+boilerplate_conv['d3_meas'],

                 'radio_day3_4' : ['replacement', 'hq_noise'],
                 'radio_day3_5' : ['yourname', 'hq_basename', 'realname', 'hq_name',
                                   'hq_stranger', 'hq_smith', 'someoneelse', 'hq_noise'],
                 
                 }


sounds = {'writing' : ['writing'],
          'power_bust' : ['Electricity_Spark'],
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


