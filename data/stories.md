## happy path
* greet
  - utter_first_message
* main_menu
  - utter_show_menu
  
## travel_by_best_valued_path
* greet
  - utter_first_message
* main_menu
  - utter_show_menu
* travel_menu
  - utter_show_travel_menu
* travel_best_valued_packages
  - trip_plan_form
  - form{"name":"trip_plan_form"}
  - form{"name":"null"}
  - utter_ask_more
  
## travel_packages_by_interest_path
* greet
  - utter_first_message
* main_menu
  - utter_show_menu
* travel_menu
  - utter_show_travel_menu
* travel_packages_by_interest
  - utter_ask_activity_name
  - activity_package_search_form
  - form{"name":"activity_package_search_form"}
  - form{"name":"null"}
  - utter_ask_more

## travel_packages_by_budget
* greet
  - utter_first_message
* main_menu
  - utter_show_menu
* travel_menu
  - utter_show_travel_menu
* travel_packages_by_budget
  - utter_ask_budget
  - package_by_budget_form
  - form{"name":"package_by_budget_form"}
  - form{"name":"null"}
  - utter_ask_more
  
## modify_cancel_booking
* greet
  - utter_first_message
* main_menu
  - utter_show_menu
* Modify_cancel_Booking
  - utter_show_cancel_booking_message
  - modify_cancel_booking_form
  - form{"name":"modify_cancel_booking_form"}
  - form{"name":"null"}
  - utter_ask_more

## go_to_live_assistant
* greet
  - utter_first_message
* main_menu
  - utter_show_menu
* get_live_assistance
  - utter_show_live_support_link
  
## FAQ
* greet
  - utter_first_message
* main_menu
  - utter_show_menu
* faq
  - utter_show_faq