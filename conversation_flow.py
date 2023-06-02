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
        CS('day2_assholes', 'radio_day2_4', None, 'day3_aggr', end_state=True),
        CS('day2_lonely', 'radio_day2_5', None, 'day3_lone', end_state=True),


    
        # Day 3 - aggressive
        CS('day3_aggr', 'radio_d3_agg_1', ["Report measurements", "Send that fucking replacement", "Please send the replacement"], ['day3_agg_meas', 'day3_agg_fuck_repl', 'day3_agg_pls_repl']),
        CS('day3_agg_fuck_repl', 'radio_d3_agg_2', ['God damnit', 'Mock Tau 1'], ['day3_agg_damn', 'day3_agg_mock']),
        CS('day3_agg_damn', 'radio_d3_agg_3', None, 'temp_state', end_state=True), #go to day4_aggr
        CS('day3_agg_mock', 'radio_d3_agg_4', None, 'temp_state', end_state=True), #go to day4_aggr
        CS('day3_agg_pls_repl', 'radio_d3_agg_5', ["Give measurements", "Send that fucking replacement!"], ['day3_agg_meas', 'day3_agg_fuck_repl']),
        CS('day3_agg_meas', 'radio_d3_agg_6', ["Fuck you!", "I am sorry"], ['day3_agg_fuck_u', 'day3_agg_so_sorry']),
        CS('day3_agg_fuck_u', 'radio_d3_agg_7', ['I am sorry about that', 'I have a contract!'], ['day3_agg_fake_sorry', 'day3_agg_contract']),
        CS('day3_agg_fake_sorry', 'radio_d3_agg_8', None, 'temp_state', end_state=True), #Go to day4_lone
        CS('day3_agg_contract', 'radio_d3_agg_9', None, 'temp_state', end_state=True), #Go to day4_aggr
        CS('day3_agg_so_sorry', 'radio_d3_agg_10', None, 'temp_state', end_state=True), #Go to day4_lone

        
        
        

        #Day 3 - lonely - not done.
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
