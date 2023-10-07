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

        #Conversation day 3 aggresive
        'day3_agg/send_fucking_replacement' : "I'm going crazy here, send that fucking replacement!",
        'day3_agg/sarcastic' : "No, no, Omicron. You can sit out there all by yourself. We will send you a batch of buiscuits in a year. Fuck those guys...",
        'day3_agg/please_send_replacement' : "I beg you, can you please send a replacement soon?",
        'day3_agg/hq_measure_omicron' : "The measurements, Omicron...",
        'day3_agg/hq_about_your_tone' : "Thank you, Omicron. About your tone the last few days...",
        'day3_agg/fuck_off' : "Fuck you! Fuck off! Fuck, fuck, FUCK!",
        'day3_agg/hq_let_you_stay' : "Omicron, we can let you stay out there one more month, if you'd like that!",
        'day3_agg/hq_not_happen_again' : "Do not let it happen again!",
        'day3_agg/fuckyou' : "Fuck you!",
        'day3_agg/hq_onemoretime' : "I think we'll try that one more time, Omicron.",
        'day3_agg/hq_tolerate' :  "That's much better, Omicron. We don't tolerate such a tone in this environment, okay? Same time tomorrow.",
        'day3_agg/goodbye' : "Alright. Goodbye.",
        'day3_agg/emotionless' : "Are you completely emotionless? It's like speaking to a brick wall!",
        'day3_agg/hq_sure': "Hm. Sure. Goodbye.",
        'day3_agg/loneliness': "It's just that- the loneliness is tearing on me!",
        'day3_agg/hq_ofcourseitis': "Of course it is. Goodbye.",
        'day3_agg/something_is_fucking_head': "I think something is fucking with my head out here!",
        'day3_agg/hq_notimeforthis': "I don't have time for this. Goodbye.",
        'day3_agg/fuck_you_bymyself' : "Fuck you! I'm sitting out here all by myself!",
        'day3_agg/hq_cooldown' : "You know what, Omicron? I think you have to cool down. Your service won't be needed the next few days. Goodbye!",
        'day3_agg/no_wait' : "No, no... Uh... Wait!",
        'day3_agg/wait_sorry' : "I'm so sorry! Uh... Please wait.",
        'day3_agg/true_sorry' : "I'm so sorry about that. It's just, I'm sitting out here all by myself, I'm getting... I'm getting agitated.",
        'day3_agg/hq_what' : "What is it?",
        

        #Conversation day 3 lonely
        'day3_lone/suit_missing' : "One of my suits has gone missing. And I mean, it's a bit weird, because they are really big, so...",
        'day3_lone/hq_have_more_than_one' : "I believe you have more than one suit. Please report the measurements.",
        'day3_lone/shed_gate_opens' : "I don't know why, but the gate to the shed keeps opening by itself. And I'm sure I am closing it so it's... it's a bit weird.",
        'day3_lone/hq_because_wind' : "It's because of the wind. Measurements, please.",
        'day3_lone/am_i_alone' : "Are you certain I'm- I'm all alone out here? I- there's some weird things going on, I think.",
        'day3_lone/hq_100_km' : "There's over a hundred kilometers to the nearest settlement. You are alone!",
        'day3_lone/storm' : "It was quite windy today. I think a storm is coming up.",
        'day3_lone/hq_still_needs_record' : "You still need to measure the weather. Please report your current measurements.",
        'day3_lone/replacement_again' : "Is there anything new about the replacement? It's... it's been a while.",
        'day3_lone/yourname' : "Uh... What is your name?",
        'day3_lone/hq_basename' : "This is Tau One...",
        'day3_lone/realname' : "No, I mean what is YOUR name?",
        'day3_lone/hq_name' : "He is asking about my name!",
        'day3_lone/hq_stranger' : "Bare find på noget. Lad være med at snakke mere med ham!",
        'day3_lone/hq_smith' : 'Uh... Smith.',
        'day3_lone/someoneelse' : "Is there somebody there with you?",
        'day3_lone/hq_talk_tomorrow' : "... Uh... I'll talk to you tomorrow. Goodbye!",
        'day3_lone/nice_to_meet_you' : "Nice to meet you, John. I can't believe, I didn't know your name... Untill now.",


        #Conversation day 4 aggressive
        'day4_agg/apologize' : "I want to apologize for my tone.",
        'day4_agg/hq_fine' : "It's fine, Omicron. Give the measurements, please.",
        'day4_agg/hq_message' : "Sigh... I have a message from HQ. Despite numerous delays... *NOISE* current worker *NOISE* stay put... *NOISE*",
        'day4_agg/cant_hear' : "What? I can't hear you!",
        'day4_agg/emotional' : "I think most people would get really emotional from such isolation.",
        'day4_agg/hq_angry' : "I swear to fucking God! We can let you stay out there untill you freeze to death! We've done it before and we sure as hell can do it again. Not a single soul would miss your pathetic criminal asshole! I'm getting paid enough to talk to this piece of... shit!",
        'day4_agg/because_lonely' : "I mean, it's probably because I'm so lonely out here.",
        'day4_agg/refuse' : "I refuse to give any measurements!",
        'day4_agg/appropriate' : "It would be appropriate if you also gave me an apology.",

        #Conversation day 4 lonely
        'day4_lone/family' : "Do you have any family?",
        'day4_lone/hq_not_really' : "Uh... We- well, yes. But not really.",
        'day4_lone/what_you_mean' : "What do you mean?",
        'day4_lone/hq_wife' : "I had a wife and daughter back in Europe. But, I haven't talked to them in a long time.",
        'day4_lone/i_see' : "I see...",
        'day4_lone/hq_4_years' : "I was sent here four years ago. I am not sure my daughter would recognize me.",
        'day4_lone/why_sent' : "Why were you sent out there in the first place?",
        'day4_lone/hq_critical' : "Well... I was critical of the war and how civil lives were wasted. Certain powerful people could not...",
        'day4_lone/hq_stranger_talk1' : "Hvad snakker du om? Giv ham beskeden!",
        'day4_lone/tough' : "Must be tough.",
        'day4_lone/hq_stuck' : "Yeah, now I'm stuck at Tau 1 with this guy who keeps trying to get into my head.",
        'day4_lone/hq_stranger_talk' : "Har du givet ham beskeden? Hallo? Giv ham beskeden!",
        'day4_lone/who_is_that' : "Who is that?",
        'day4_lone/feel_same' : "Yeah, I'm feeling the same way. I'm getting really lonely out here.",
        'day4_lone/hq_stop_complain' : "Stop complaining.",
        'day4_lone/why_not' : "Why not?",
        'day4_lone/hq_why_you_think' : "Why do you think? It's the same reason you keep bothering only me. They are too far away for the radio.",
        'day4_lone/cold' : "It's freezing out here. Is it also cold where you are?",
        'day4_lone/hq_sure_meas_pls' : "Sure. Measurements, please.",
        'day4_lone/clean' : "This place is getting messy! I really need to clean up the house.",
        'day4_lone/hq_dont_care' : "Frankly, Omicron. I do not care. Give me the measurements.",
        
        #Conversation day 4 paranoid
        'day4_para/swear_alone' : "I swear I'm not alone out here!",
        'day4_para/hq_nearest_settle' : "I can assure you there are nobody. You would die if you tried to walk to the nearest settlement.",
        'day4_para/polar_bears' : "Are there any polar bears out here?",
        'day4_para/hq_polar_bear' : "You are at the Antarctic... There are no polar bears.",
        'day4_para/hq_storm' : "Hm. Seems like a pretty bad storm.",
        'day4_para/hearing_things' : "I am hearing things at night.",
        'day4_para/hq_nuts' : "You wouldn't be the first. A prior observer went nuts. Don't do that as well.",
        'day4_para/paranoid' : "Am I just paranoid?",
        'day4_para/how_happen' : "How did that happen?",
        'day4_para/hq_maybe_it_could_be' : "I don't know. Cabin fever? Or maybe it could be *NOISE*. Measurements please.",
        'day4_para/last_part' : "What was that? W- what was that last part?",
        'day4_para/what_didnt_tell' : "What?! Why didn't you tell me?",
        'day4_para/hq_cursed' : "Why would I? It's not like Omicron is cursed or anything.",
        'day4_para/cursed' : "Uh... What? Is- is it cursed?",
        

        #Self talk
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
        'self/fuse_fits' : "It fits! Let's hope it works. Now let's restart the generator.",
        'self/power_back' : "Yes! It worked! The power is back on.",
        'self/find_padlock' : "Hmm... Perhaps I should lock the door to make sure it doesn't open again. There should be a padlock somewhere in there.",
        'self/gate_locked' : "Now the gate won't open by itself. Back to bed!",
        'self/lock_gate' : "I better lock the shed gate before going inside.",
        'self/generator_needs_fix' : "I need to get the power on first...",
        
        #Sound effects below.
        'self/writing' : '',
        'self/Electricity_Spark' : '',
        }


conversations = {'radio_day1' : ['day1/report', 'day1/hq_greet', 'day1/measurements', 'day1/hq_delay'],
                 'radio_day1_2' : ['day1/whatagain', 'day1/hq_noted', 'day1/bastards'],
                 'radio_day1_3' : ['day1/please_hurry', 'day1/hq_noted', 'day1/goddamnit'],

                 'radio_day2' : ['day1/report', 'day1/hq_greet', 'day1/measurements', 'day2/hq_noted', 'day2/wait', 'day2/hq_noise'],
                 'radio_day2_2' : ['day2/yourday', 'day2/hq_what', 'day2/today_i', 'day2/hq_turn_off'],
                 'radio_day2_3' : ['day2/replacement', 'day2/hq_letyouknow'],
                 'radio_day2_4' : ['day2/cant_believe', 'day2/hq_turn_off', 'day2/did_they_hear_that'],
                 'radio_day2_5' : ['day2/im_lonely', 'day2/hq_turn_off'],

                 'radio_d3_agg_1' : ['day1/report', 'day1/hq_greet'],
                 'radio_d3_agg_2' : ['day3_agg/fuckyou', 'day2/hq_turn_off'],
                 'radio_d3_agg_3' : ['day1/goddamnit'],
                 'radio_d3_agg_4' : ['day3_agg/sarcastic'],
                 'radio_d3_agg_5' : ['day3_agg/please_send_replacement', 'day3_agg/hq_measure_omicron'],
                 'radio_d3_agg_6' : ['day1/measurements', 'day3_agg/hq_about_your_tone'],
                 'radio_d3_agg_7' : ['day3_agg/fuck_you_bymyself', 'day3_agg/hq_cooldown'],
                 'radio_d3_agg_8' : ['day3_agg/wait_sorry', 'day3_agg/hq_what'],
                 'radio_d3_agg_9' : ['day3_agg/fuck_off', 'day2/hq_turn_off'],
                 'radio_d3_agg_10' : ['day3_agg/true_sorry', 'day3_agg/hq_not_happen_again'],
                 'radio_d3_agg_11' : ['day3_agg/send_fucking_replacement', 'day3_agg/hq_onemoretime'],
                 'radio_d3_agg_12' : ['day3_agg/fuck_you_bymyself', 'day3_agg/hq_onemoretime'],
                 'radio_d3_agg_13' : ['day1/measurements', 'day3_agg/hq_tolerate'],
                 'radio_d3_agg_14' : ['day3_agg/no_wait', 'day3_agg/hq_what'],
                 'radio_d3_agg_15' : ['day3_agg/goodbye', 'day2/hq_turn_off'],
                 'radio_d3_agg_16' : ['day3_agg/emotionless', 'day3_agg/hq_sure'],
                 'radio_d3_agg_17' : ['day3_agg/loneliness', 'day3_agg/hq_ofcourseitis'],
                 'radio_d3_agg_18' : ['day3_agg/something_is_fucking_head', 'day3_agg/hq_notimeforthis'],

                 'radio_d3_lone_1' : ['day1/report', 'day1/hq_greet'],
                 'radio_d3_lone_2' : ['day3_lone/suit_missing', 'day3_lone/hq_have_more_than_one'],
                 'radio_d3_lone_3' : ['day3_lone/shed_gate_opens', 'day3_lone/hq_because_wind', 'day1/measurements', 'day2/hq_noted', 'day2/wait'],
                 'radio_d3_lone_4' : ['day1/measurements', 'day2/hq_noted', 'day2/wait'],
                 'radio_d3_lone_5' : ['day3_lone/am_i_alone', 'day3_lone/hq_100_km'],
                 'radio_d3_lone_6' : ['day3_lone/replacement_again', 'day2/hq_turn_off'],
                 'radio_d3_lone_7' : ['day3_lone/storm', 'day3_lone/hq_still_needs_record'],
                 'radio_d3_lone_8' : ['day3_lone/yourname', 'day3_lone/hq_basename', 'day3_lone/realname', 'day3_lone/hq_name', 'day3_lone/hq_stranger', 'day3_lone/hq_smith'],
                 'radio_d3_lone_9' : ['day3_lone/someoneelse', 'day2/hq_turn_off'],
                 'radio_d3_lone_10' : ['day3_lone/nice_to_meet_you', 'day3_lone/hq_talk_tomorrow'],

                 'radio_d4_agg_1' : ['day1/report', 'day1/hq_greet'],
                 'radio_d4_agg_2' : ['day4_agg/apologize', 'day4_agg/hq_fine'],
                 'radio_d4_agg_3' : ['day1/measurements', 'day2/hq_noted', 'day4_agg/hq_message', 'day4_agg/cant_hear', 'day2/hq_turn_off'], #standard turn off with noise
                 'radio_d4_agg_4' : ['day4_agg/appropriate', 'day4_agg/hq_message', 'day4_agg/cant_hear', 'day2/hq_turn_off'], #standard turn off with noise
                 'radio_d4_agg_5' : ['day4_agg/because_lonely', 'day3_agg/hq_measure_omicron'],
                 'radio_d4_agg_6' : ['day4_agg/emotional', 'day4_agg/hq_message', 'day4_agg/cant_hear', 'day2/hq_turn_off'], #standard turn off with noise
                 'radio_d4_agg_7' : ['day4_agg/refuse', 'day4_agg/hq_angry', 'day4_agg/hq_message', 'day4_agg/cant_hear', 'day2/hq_turn_off'], #standard turn off with noise

                 'radio_d4_lone_1' : ['day1/report', 'day1/hq_greet'],
                 'radio_d4_lone_2' : ['day4_lone/family', 'day4_lone/hq_not_really'],
                 'radio_d4_lone_3' : ['day4_lone/what_you_mean', 'day4_lone/hq_wife'],
                 'radio_d4_lone_4' : ['day4_lone/hq_wife'], #Don't say anything first
                 'radio_d4_lone_5' : ['day4_lone/i_see', 'day4_lone/hq_4_years'],
                 'radio_d4_lone_6' : ['day4_lone/why_sent', 'day4_lone/hq_critical', 'day4_lone/hq_stranger_talk1', 'day4_agg/hq_message'], #may revise - Do we need to talk after?
                 'radio_d4_lone_7' : ['day4_lone/tough', 'day4_lone/hq_stuck'],
                 'radio_d4_lone_8' : ['day4_lone/what_you_mean', 'day4_lone/hq_stranger_talk', 'day4_agg/hq_message'],
                 'radio_d4_lone_9' : ['day4_lone/who_is_that', 'day4_lone/hq_stranger_talk', 'day4_agg/hq_message'],
                 'radio_d4_lone_10' : ['day4_lone/feel_same', 'day4_lone/hq_stop_complain', 'day4_agg/hq_message'],
                 'radio_d4_lone_11' : ['day4_lone/why_not', 'day4_lone/hq_why_you_think', 'day4_agg/hq_message'],
                 'radio_d4_lone_12' : ['day4_lone/cold', 'day4_lone/hq_sure_meas_pls', 'day1/measurements', 'day4_agg/hq_message'],
                 'radio_d4_lone_13' : ['day4_lone/clean', 'day4_lone/hq_dont_care', 'day1/measurements', 'day4_agg/hq_message'],

                 'radio_d4_para_1' : ['day1/report', 'day1/hq_greet'],
                 'radio_d4_para_2' : ['day4_para/swear_alone', 'day4_para/hq_nearest_settle', 'day3_agg/hq_measure_omicron'],
                 'radio_d4_para_3' : ['day4_para/polar_bears', 'day4_para/hq_polar_bear', 'day3_agg/hq_measure_omicron'],
                 'radio_d4_para_4' : ['day1/measurements', 'day4_para/hq_storm', 'day4_agg/hq_message'],
                 'radio_d4_para_5' : ['day4_para/hearing_things', 'day4_para/hq_nuts'],
                 'radio_d4_para_6' : ['day4_para/paranoid', 'day4_para/hq_nuts'],
                 'radio_d4_para_7' : ['day4_para/how_happen', 'day4_para/hq_maybe_it_could_be', 'day4_para/last_part', 'day3_agg/hq_measure_omicron'],
                 'radio_d4_para_8' : ['day4_para/what_didnt_tell', 'day4_para/hq_cursed', 'day4_para/cursed', 'day3_agg/hq_measure_omicron'],
                 }


sounds = {'writing' : ['self/writing'],
          'power_bust' : ['self/Electricity_Spark'],
          }

self_talk = {'shed_door_open' : ['self/generatorgate'],
             'not_done_with_tasks' : ['self/stuffouthere'],
             'no_clothes' : ['self/toocold'],
             'no_clipboard' : ['self/noclipboard'],
             'power_cut' : ['self/power_cut', 'self/see_from_bathroom'],
             'bathroom_window': ['self/see_gate_damn'],
             }

conversations.update(sounds)
conversations.update(self_talk)


