#A script for controlling which dialogues should be played and
#which buttons should be showed and when.

import settings

#Which choices should appear on the GUI? Will get messy.
def gui_choices(prog):
    if settings.day == 1:
        if prog == 0:
            base.conv_gui.choice([("First choice", 1), ("Second choice", 2)])
    elif settings.day == 2:
        if prog == 0:
            base.conv_gui.choice([("How was your day?", 1), ("Any news about my replacement?", 2)])
    elif settings.day == 3:
        if prog == 0:
            base.conv_gui.choice([("Report measurements", 1), ("One of my thermal suits is missing", 2),
                                  ("It was rather windy today. A storm might be coming up",3)])
        elif prog == 1:
            base.conv_gui.choice([("Any news about my replacements?", 4), ("What is your name?", 5)])



def talk_new_path():
    p = settings.conversation_progress
    
    if settings.day == 1:
        if p == 1:
            base.conversation.talk('radio_day1_2')

    elif settings.day == 2:
        if p == 1:
            base.conversation.talk('radio_day2_2')
        elif p == 2:
            base.conversation.talk('radio_day2_3')
            
    elif settings.day == 3:
        if p == 1:
            base.conversation.talk('radio_day3_1')
        elif p == 2:
            base.conversation.talk('radio_day3_2')
        elif p == 3:
            base.conversation.talk('radio_day3_3')
        elif p == 4:
            base.conversation.talk('radio_day3_4')
        elif p == 5:
            base.conversation.talk('radio_day3_5')
