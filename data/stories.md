## happy path
* greet
  - utter_first_message
* main_menu
  - utter_show_menu
  
## choose travel menu path
* greet
  - utter_first_message
* main_menu
  - utter_show_menu
* travel_menu
  - utter_show_travel_menu
  
<!--####### Travel by best valued package ######-->  
  
## travel_by_best_valued_path
* travel_best_valued_packages
  - trip_plan_form
  - form{"name":"trip_plan_form"}
  - form{"name":null}
  - utter_ask_more
  - action_slot_reset
* goodbye
  - utter_goodbye
  
<!--## travel by best valued value correction path 1
* travel_best_valued_packages
  - trip_plan_form
  - form{"name":"trip_plan_form"}
* value_correction
  - action_change_value
  - form{"name":null}
  
## ## travel by best valued value correction path 2
* travel_best_valued_packages
  - trip_plan_form
  - form{"name":"trip_plan_form"}
  - form{"name":null}
* value_correction
  - action_change_value-->
  
  
## break a tripplanform when travel_menu intent occured
* travel_best_valued_packages
    - trip_plan_form
    - form{"name": "trip_plan_form"}
* travel_menu
    - action_deactivate_form
    - action_slot_reset
    - form{"name": null}
    - utter_show_travel_menu
  
## break a tripplanform when greet intent occured
* travel_best_valued_packages
    - trip_plan_form
    - form{"name": "trip_plan_form"}
* greet
    - action_deactivate_form
    - action_slot_reset
    - form{"name": null}
    - utter_first_message
    
    
<!--################# Travel by interest/activity ####################-->
  
## travel_packages_by_interest_path
* travel_packages_by_interest
  - utter_ask_activity_name
  - activity_package_search_form
  - form{"name":"activity_package_search_form"}
  - form{"name":null}
  - utter_ask_more
  - action_slot_reset
* goodbye
  - utter_goodbye
  
<!--## travel by interest correction path 1
* travel_packages_by_interest
  - utter_ask_activity_name
  - activity_package_search_form
  - form{"name":"activity_package_search_form"}
* value_correction
  - action_change_value
  - activity_package_search_form
  - form{"name":null}
  - utter_ask_more
  - action_slot_reset
  
## travel by interest correction path 2
* travel_packages_by_interest
  - utter_ask_activity_name
  - activity_package_search_form
  - form{"name":"activity_package_search_form"}
  - form{"name":null}
* value_correction
  - action_change_value
  - utter_ask_more
  - action_slot_reset-->
  
## break a ActivityPackageSearchForm when travel_menu intent occurs
* travel_packages_by_interest
    - utter_ask_activity_name
    - activity_package_search_form
    - form{"name": "activity_package_search_form"}
* travel_menu
    - action_deactivate_form
    - action_slot_reset
    - form{"name": null}
    - utter_show_travel_menu
    
## break a ActivityPackageSearchForm when greet intent occurs
* travel_packages_by_interest
    - utter_ask_activity_name
    - activity_package_search_form
    - form{"name": "activity_package_search_form"}
* greet
    - action_deactivate_form
    - action_slot_reset
    - form{"name": null}
    - utter_first_message
  
<!--################# Travel by budget ####################-->

## travel_packages_by_budget
* travel_packages_by_budget
  - utter_ask_budget
  - package_by_budget_form
  - form{"name":"package_by_budget_form"}
  - form{"name":null}
  - utter_ask_more
  - action_slot_reset
* goodbye
  - utter_goodbye

<!--## travel by budget correction path 1
* travel_packages_by_budget
  - package_by_budget_form
  - form{"name":"package_by_budget_form"}
* value_correction
  - action_change_value
  - form{"name":null}
  - utter_ask_more
  
## travel by budget correction path 2
* travel_packages_by_budget
  - package_by_budget_form
  - form{"name":"package_by_budget_form"}
  - form{"name":null}
* value_correction
  - action_change_value
  - utter_ask_more-->
  
## break a PackageByBudgetForm when travel_menu intent occurs
* travel_packages_by_budget
  - package_by_budget_form
  - form{"name": "package_by_budget_form"}
* travel_menu
  - action_deactivate_form
  - form{"name": null}
  - action_slot_reset
  - utter_show_travel_menu
    
## break a PackageByBudgetForm when greet intent occurs
* travel_packages_by_budget
  - package_by_budget_form
  - form{"name": "package_by_budget_form"}
* greet
  - action_deactivate_form
  - action_slot_reset
  - form{"name": null}
  - utter_first_message
    
<!--################# Track booking ####################-->
## track booking happy path
* track_booking
  - utter_ask_booking_ID
  - track_booking_form
  - form{"name":"track_booking_form"}
  - form{"name":null}
  - utter_ask_more
* goodbye
  - utter_goodbye
  
<!--################# Modify/cancel booking ####################-->
  
## modify_cancel_booking-cancel
* Modify_cancel_Booking
  - utter_show_cancel_booking_message
  - slot{"cancel_reschedule": "cancel"}
  - modify_cancel_booking_form
  - form{"name":"modify_cancel_booking_form"}
  - form{"name":null}
  - utter_ask_more
  - action_slot_reset
* goodbye
  - utter_goodbye
  
## modify_cancel_booking-reschedule
* Modify_cancel_Booking
  - utter_show_cancel_booking_message
  - slot{"cancel_reschedule": "reschedule"}
  - modify_cancel_booking_form
  - form{"name":"modify_cancel_booking_form"}
  - form{"name":null}
  - utter_ask_more
  - action_slot_reset
* goodbye
  - utter_goodbye
  
<!--## modify_cancel_booking correction path 1
* Modify_cancel_Booking
  - utter_show_cancel_booking_message
  - modify_cancel_booking_form
  - form{"name":"modify_cancel_booking_form"}
* value_correction
  - action_change_value
  - form{"name":null}
  - utter_ask_more
  
## modify_cancel_booking correction path 2
* Modify_cancel_Booking
  - utter_show_cancel_booking_message
  - modify_cancel_booking_form
  - form{"name":"modify_cancel_booking_form"}
  - form{"name":null}
* value_correction
  - action_change_value
  - utter_ask_more-->
  
## break a ModifyCancelBookingForm when main_menu intent occurs
* Modify_cancel_Booking
  - utter_show_cancel_booking_message
  - modify_cancel_booking_form
  - form{"name":"modify_cancel_booking_form"}
* main_menu
  - action_deactivate_form
  - form{"name": null}
  - utter_show_menu
  - action_slot_reset
  
## break a ModifyCancelBookingForm when greet intent occurs
* Modify_cancel_Booking
  - utter_show_cancel_booking_message
  - modify_cancel_booking_form
  - form{"name":"modify_cancel_booking_form"}
* greet
  - action_deactivate_form
  - form{"name": null}
  - utter_first_message
  - action_slot_reset

## go_to_live_assistant
* greet
  - utter_first_message
* main_menu
  - utter_show_menu
* get_live_assistance
  - utter_show_live_support_link
  - utter_ask_more
* goodbye
  - utter_goodbye
  
## FAQ
* greet
  - utter_first_message
* main_menu
  - utter_show_menu
* faq
  - utter_show_faq
  - utter_ask_more
* goodbye
  - utter_goodbye
  
  
