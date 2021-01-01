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


def talk_new_path():
    p = settings.conversation_progress
    
    if settings.day == 1:
        if p == 1:
            base.conversation.talk('radio_day1_2')

    if settings.day == 2:
        if p == 1:
            base.conversation.talk('radio_day2_2')
        elif p == 2:
            base.conversation.talk('radio_day2_3')
