import settings
from conversation_state import ConversationState as CS

def initialise_states():
    states = [
        #Day 1
        #  Name     voice sequence      button strings      transitions
        CS('day1', 'radio_day1', ['What! Again?', 'Please hurry!'], ['day1_what_again', 'hurry']),
        CS('day1_what_again', 'radio_day1_2', None, 'day2', end_state=True),
        CS('hurry', 'radio_day1_3', None, 'day2', end_state=True), # End state still needs a transition.

        #Day 2
        CS('day2', 'radio_day2', ["How was your day?", "Any news about my replacement?"], ['day2_how_was_day', 'day2_replace']),
        CS('day2_how_was_day', 'radio_day2_2', None, 'day3_lone', end_state=True),  #Go to lonely day3
        CS('day2_replace', 'radio_day2_3', ["I can't believe these assholes!", "I'm so lonely..."], ['day2_assholes', 'day2_lonely']),
        CS('day2_assholes', 'radio_day2_4', None, 'day2_aggr', end_state=True),
        CS('day2_lonely', 'radio_day2_5', None, 'day2_lone', end_state=True),


    
        #Fixed to here

        

        #Day 3 - lonely
        CS('day3_lone', 'radio_day3', ["Report measurements", "One of my thermal suits is missing",
                                  "It was rather windy today. A storm might be coming up"], ['day3_meas', 'day3_thermal', 'day3_storm']),
        CS('day3_meas', 'radio_day3_1', ["Any news about my replacement?", "What is your name?"], ['day3_replace', 'day3_name']),
        CS('day3_thermal', 'radio_day3_2', ["Any news about my replacement?", "What is your name?"], ['day3_replace', 'day3_name']),
        CS('day3_storm', 'radio_day3_3', ["Any news about my replacement?", "What is your name?"], ['day3_replace', 'day3_name']),
        
        CS('day3_replace', 'radio_day3_4', None, 'temp_state', end_state=True),
        CS('day3_name', 'radio_day3_5', None, 'temp_state', end_state=True),



        # Day 3 - aggressive
        CS('day3_lone', 'radio_day3', ["Report measurements", "One of my thermal suits is missing",
                                  "It was rather windy today. A storm might be coming up"], ['day3_meas', 'day3_thermal', 'day3_storm']),
        CS('day3_meas', 'radio_day3_1', ["Any news about my replacement?", "What is your name?"], ['day3_replace', 'day3_name']),
        CS('day3_thermal', 'radio_day3_2', ["Any news about my replacement?", "What is your name?"], ['day3_replace', 'day3_name']),
        CS('day3_storm', 'radio_day3_3', ["Any news about my replacement?", "What is your name?"], ['day3_replace', 'day3_name']),
        
        CS('day3_replace', 'radio_day3_4', None, 'temp_state', end_state=True),
        CS('day3_name', 'radio_day3_5', None, 'temp_state', end_state=True),

        CS('temp_state', 'radio_day1', None, None, end_state=True), #Delete this state.

    ]

    
    settings.conversation_state = states[0]

    for i in states:
        settings.conversation_states[i.name] = i
