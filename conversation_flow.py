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
        CS('day2_how_was_day', 'radio_day2_2', None, 'day3_lone', end_state=True),
        CS('day2_replace', 'radio_day2_3', ["I can't believe these assholes!", "I'm so lonely..."], ['day2_assholes', 'day2_lonely']),
        CS('day2_assholes', 'radio_day2_4', None, 'day3_agg', end_state=True),
        CS('day2_lonely', 'radio_day2_5', None, 'day3_lone', end_state=True),

        # Day 3 - aggressive
        CS('day3_agg', 'radio_d3_agg_1', ["Send that fucking replacement", "Please send the replacement"], ['day3_agg_tryagain', 'day3_agg_pls_repl']),
        CS('day3_agg_tryagain', 'radio_d3_agg_11', ["Fuck you!", "Give measurements"], ['day3_agg_fuck_repl', 'day3_agg_meas2']),
        CS('day3_agg_tryagain2', 'radio_d3_agg_12', ["Fuck you!", "Give measurements"], ['day3_agg_fuck_repl', 'day3_agg_meas2']), #Slightly different player dialogue
        CS('day3_agg_fuck_repl', 'radio_d3_agg_2', ['God damnit', 'Mock Tau 1'], ['day3_agg_damn', 'day3_agg_mock']),
        CS('day3_agg_damn', 'radio_d3_agg_3', None, 'day4_agg', end_state=True), 
        CS('day3_agg_mock', 'radio_d3_agg_4', None, 'day4_agg', end_state=True),
        CS('day3_agg_pls_repl', 'radio_d3_agg_5', ["Give measurements", "Fuck you! I'm all alone!"], ['day3_agg_meas1', 'day3_agg_tryagain2']),
        CS('day3_agg_meas1', 'radio_d3_agg_6', ["Fuck you! I'm all alone!", "I am sorry"], ['day3_agg_fuck_alone', 'day3_agg_so_sorry']),
        CS('day3_agg_meas2', 'radio_d3_agg_13', ["Fuck you!", "No, wait!"], ['day3_agg_fuck_repl', 'day3_agg_nowait']),
        CS('day3_agg_so_sorry', 'radio_d3_agg_10', ["Goodbye", "Wait!"], ['day3_agg_bye', 'day3_agg_nowait']),
        CS('day3_agg_fuck_alone', 'radio_d3_agg_7', ["Wait, I'm sorry!", 'Fuck off!'], ['day3_agg_sorrywait', 'day3_agg_fuckoff']),
        CS('day3_agg_nowait', 'radio_d3_agg_14', ["Are you emotionless?", "I am just lonely", "My head is fucked"], ['day3_agg_brick', 'day3_agg_lonely', 'day3_agg_head']), #make them
        CS('day3_agg_sorrywait', 'radio_d3_agg_8',["Are you emotionless?", "I am just lonely", "My head is fucked"], ['day3_agg_brick', 'day3_agg_lonely', 'day3_agg_head']),
        CS('day3_agg_brick', 'radio_d3_agg_16', None, 'day4_agg', end_state=True),
        CS('day3_agg_lonely', 'radio_d3_agg_17', None, 'day4_lone', end_state=True),
        CS('day3_agg_head', 'radio_d3_agg_18', None, 'day4_para', end_state=True),
        CS('day3_agg_fuckoff', 'radio_d3_agg_9', None, 'day4_agg', end_state=True),
        CS('day3_agg_bye', 'radio_d3_agg_15', None, 'day4_lone', end_state=True),
        

        #Day 3 - lonely
        CS('day3_lone', 'radio_d3_lone_1', ["One of my thermal suits is missing", "A storm might be coming up"], ['day3_lone_thermal', 'day3_lone_storm']),
        CS('day3_lone_thermal', 'radio_d3_lone_2', ["The shed gate keeps opening", "Report measurements"], ['day3_lone_gate', 'day3_lone_meas']),
        CS('day3_lone_gate', 'radio_d3_lone_3', ['Any news about the replacement?', "Are you sure I'm alone here?"], ['day3_lone_replace', 'day3_lone_alone']), #Jumps to same state as "give measurements"
        CS('day3_lone_meas', 'radio_d3_lone_4', ['Any news about the replacement?', "Are you sure I'm alone here?"], ['day3_lone_replace', 'day3_lone_alone']),
        CS('day3_lone_alone', 'radio_d3_lone_5', None, 'day4_para', end_state=True),
        CS('day3_lone_replace', 'radio_d3_lone_6', None, 'day4_lone', end_state=True),
        CS('day3_lone_storm', 'radio_d3_lone_7', ['Report measurements'], ['day3_lone_meas2']),
        CS('day3_lone_meas2', 'radio_d3_lone_4', ['Any news about the replacement?', "What is your name?"], ['day3_lone_replace', 'day3_lone_name']),
        CS('day3_lone_name', 'radio_d3_lone_8', ['Is someone there with you?', 'Nice to meet you John!'], ['day3_lone_stranger', 'day3_lone_john']),
        CS('day3_lone_stranger', 'radio_d3_lone_9', None, 'day4_para', end_state=True),
        CS('day3_lone_john', 'radio_d3_lone_10', None, 'day4_lone', end_state=True),
        
        #Day 4 - aggressive
        CS('day4_agg', 'radio_d4_agg_1', ['I am sorry about my tone', 'Refuse to report'], ['day4_agg_sorry', 'day4_agg_refuse']),
        CS('day4_agg_sorry', 'radio_d4_agg_2', ['Give measurements', 'Ask for an apology', "It's because of the loneliness"], ['day4_agg_meas','day4_agg_apology', 'day4_agg_lone']),
        CS('day4_agg_meas', 'radio_d4_agg_3', None, 'day4_night', end_state=True), #night
        CS('day4_agg_apology', 'radio_d4_agg_4', None, 'day4_night', end_state=True), #night
        CS('day4_agg_lone', 'radio_d4_agg_5', ['Report measurements', 'I can get a bit emotional'], ['day4_agg_meas', 'day4_agg_emo']),
        CS('day4_agg_emo', 'radio_d4_agg_6', None, 'day4_night', end_state=True), #night
        CS('day4_agg_refuse', 'radio_d4_agg_7', None, 'day4_night', end_state=True), #night

        #Day 4 - lonely
        CS('day4_lone', 'radio_d4_lone_1', ["Do you have a family?", "Is it also cold where you are?", "I really need to clean the house"], ['day4_lone_family', 'day4_lone_cold', 'day4_lone_clean']),
        CS('day4_lone_family', 'radio_d4_lone_2', ["Say nothing", "What do you mean?"], ['day4_lone_family3', 'day4_lone_family2']),
        CS('day4_lone_family2', 'radio_d4_lone_3', ["I see", "I feel the same", "Why not?"], ['day4_lone_isee', 'day4_lone_same', 'day4_lone_why']),
        CS('day4_lone_family3', 'radio_d4_lone_4', ["I see", "I feel the same", "Why not?"], ['day4_lone_isee', 'day4_lone_same', 'day4_lone_why']), #Same, just not asking
        CS('day4_lone_isee', 'radio_d4_lone_5', ["Why were you sent here?", "Must be tough"], ['day4_lone_sent', 'day4_lone_tough']),
        CS('day4_lone_sent', 'radio_d4_lone_6', None, 'day4_night', end_state=True), #night
        CS('day4_lone_tough', 'radio_d4_lone_7', ['What do you mean?', 'Who is that?'], ['day4_lone_mean', 'day4_lone_who']),
        CS('day4_lone_mean', 'radio_d4_lone_8', None, 'day4_night', end_state=True), #night
        CS('day4_lone_who', 'radio_d4_lone_9', None, 'day4_night', end_state=True), #night
        CS('day4_lone_same', 'radio_d4_lone_10', None, 'day4_night', end_state=True), #night
        CS('day4_lone_why', 'radio_d4_lone_11', None, 'day4_night', end_state=True), #night
        CS('day4_lone_cold', 'radio_d4_lone_12', None, 'day4_night', end_state=True), #May want some choices to not report here?
        CS('day4_lone_clean', 'radio_d4_lone_13', None, 'day4_night', end_state=True), #As well as here

        #Day 4 - paranoia
        CS('day4_para', 'radio_d4_para_1', ['I swear I am not alone', 'Are there any polar bears here?'], ['day4_para_nalone', 'day4_para_bears']),
        CS('day4_para_nalone', 'radio_d4_para_2', ['Give measurements', 'I am hearing things at night', 'Am I just paranoid?'], ['day4_para_meas', 'day4_para_hearing', 'day4_para_para']),
        CS('day4_para_bears', 'radio_d4_para_3', ['Give measurements', 'I am hearing things at night', 'Am I just paranoid?'], ['day4_para_meas', 'day4_para_hearing', 'day4_para_para']),
        CS('day4_para_meas', 'radio_d4_para_4', None, 'day4_night', end_state=True), #night
        CS('day4_para_hearing', 'radio_d4_para_5', ['How did that happen?', "Why didn't you tell me?"], ['day4_para_how', 'day4_para_tell']),
        CS('day4_para_para', 'radio_d4_para_6', ['How did that happen?', "Why didn't you tell me?"], ['day4_para_how', 'day4_para_tell']),
        CS('day4_para_how', 'radio_d4_para_7', ['Give measurements'], ['day4_para_meas']), #night
        CS('day4_para_tell', 'radio_d4_para_8', ['Give measurements'], ['day4_para_meas']), #night
        
        #Day 4 night state
        CS('day4_night', 'radio_d4_night_1', ['Who is this?', "What's going on?"], ['day4_night_2', 'day4_night_3']),
        CS('day4_night_2', 'radio_d4_night_2', ['Who the fuck is this?', "Is somebody coming?"], ['day4_night_4', 'day4_night_5']),
        CS('day4_night_3', 'radio_d4_night_3', ['Who the fuck is this?', "Is somebody coming?"], ['day4_night_4', 'day4_night_5']),
        CS('day4_night_4', 'radio_d4_night_4', None, 'temp_state', end_state=True),
        CS('day4_night_5', 'radio_d4_night_5', None, 'temp_state', end_state=True),
        
        
        CS('temp_state', 'radio_day1', None, None, end_state=True), #Delete this state.

    ]

    
    settings.conversation_state = states[0]

    for i in states:
        settings.conversation_states[i.name] = i
