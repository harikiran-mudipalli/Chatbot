## happy path 1 (/var/folders/sq/5q6mnj1d4mj7qln38686pq0w0000gn/T/tmpb6i8sbuv/783357bda6b747c19ea5b6787d563074_conversation_tests.md)
* greet: hello there!
    - utter_greet   <!-- predicted: utter_bot_greet -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_book -->


## happy path 2 (/var/folders/sq/5q6mnj1d4mj7qln38686pq0w0000gn/T/tmpb6i8sbuv/783357bda6b747c19ea5b6787d563074_conversation_tests.md)
* greet: hello there!
    - utter_greet   <!-- predicted: utter_bot_greet -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_book -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (/var/folders/sq/5q6mnj1d4mj7qln38686pq0w0000gn/T/tmpb6i8sbuv/783357bda6b747c19ea5b6787d563074_conversation_tests.md)
* greet: hello
    - utter_greet   <!-- predicted: utter_bot_greet -->
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_ask_origin -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_book -->


## sad path 2 (/var/folders/sq/5q6mnj1d4mj7qln38686pq0w0000gn/T/tmpb6i8sbuv/783357bda6b747c19ea5b6787d563074_conversation_tests.md)
* greet: hello
    - utter_greet   <!-- predicted: utter_bot_greet -->
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_ask_origin -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye   <!-- predicted: utter_ask_origin -->


## sad path 3 (/var/folders/sq/5q6mnj1d4mj7qln38686pq0w0000gn/T/tmpb6i8sbuv/783357bda6b747c19ea5b6787d563074_conversation_tests.md)
* greet: hi
    - utter_greet   <!-- predicted: utter_bot_greet -->
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: utter_ask_origin -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: utter_ask_origin -->


## bot challenge (/var/folders/sq/5q6mnj1d4mj7qln38686pq0w0000gn/T/tmpb6i8sbuv/783357bda6b747c19ea5b6787d563074_conversation_tests.md)
* bot_challenge: are you a bot?
    - utter_iamabot   <!-- predicted: utter_ask_origin -->


