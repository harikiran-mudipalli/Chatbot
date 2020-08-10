# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, EventType

#from rasa_core.events import AllSlotsReset

entity_dic = {"change_destination": "destination",
              "change_origin": "origin",
              "change_adults_count": "adults_count",
              "change_children_count": "child_count",
              "change_travel_date": "travel_date",
              "change_travel_period": "travel_period",
              "change_budget": "budget",
              }


class ChangeSlotValue(Action):
    def name(self):
        return "action_change_value"

    def run(self, dispatcher, tracker, domain):
        if tracker.latest_message['intent'].get('name') == "value_correction":
            key_ent = tracker.latest_message['entities'][0]['entity']
            print("key ent", key_ent)
            val_ent = entity_dic[key_ent]
            print("val ent", val_ent)
            if key_ent in list(entity_dic):
                defined_slot = tracker.get_slot(val_ent)
                print("defined slot", defined_slot)
                if defined_slot is not None:
                    defined_slot = None
                    slot_value = tracker.latest_message['entities'][1]['value']
                    print("slot value:", slot_value, "\nentity:", val_ent)
                    dispatcher.utter_message("The value is changed!")
                    return [SlotSet(val_ent, slot_value)]


class TripplanForm(FormAction):
    def name(self):
        return "trip_plan_form"

    def required_slots(self, tracker) -> List[Text]:
        if tracker.get_slot("amenities") == True:
            return ["destination",
                    "origin",
                    "adults_count",
                    "child_count",
                    "pets",
                    "travel_date",
                    "travel_period",
                    "budget",
                    "amenities",
                    "property_type",
                    "facilities"]
        else:
            return ["destination",
                    "origin",
                    "adults_count",
                    "child_count",
                    "pets",
                    "travel_date",
                    "travel_period",
                    "budget",
                    "amenities"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "travel_date": [self.from_text(not_intent=["travel_menu", "greet", "stop"])],
            "travel_period": [self.from_text(not_intent=["travel_menu", "greet", "stop"])],
            "pets": [self.from_entity(entity="pets"),
                     self.from_intent(intent='affirm', value=True),
                     self.from_intent(intent='deny', value=False)],
            "adults_count": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ],
            "child_count": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ],
            "budget": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ],
            "destination": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ],
            "origin": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ],
            "amenities": [self.from_intent(intent='affirm', value=True),
                          self.from_intent(intent='deny', value=False)],
            "property_type": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ],
            "facilities": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ]
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        ''' buttons = ["Destination: {}".format(tracker.get_slot("destination")),
                    "Boarding Point: {}".format(tracker.get_slot("origin")),
                    "Number of Adults: {}".format(tracker.get_slot("adults_count")),
                    "Number of Children: {}".format(tracker.get_slot("child_count")),
                    "Pets: {}".format("No" if tracker.get_slot("pets") is False else "Yes"),
                    "Traveling Date: {}".format(tracker.get_slot("travel_date")),
                    "Length of Trip: {}".format(tracker.get_slot("travel_period")),
                    "Budget: {}".format(tracker.get_slot("budget"))]
        message = "Do you want to make any changes?"'''
        dispatcher.utter_message("Form Filled!")
        return []



class ActivityPackageSearchForm(FormAction):
    def name(self):
        return "activity_package_search_form"

    def required_slots(self, tracker) -> List[Text]:
        return ["activity_name", "activity_date"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "activity_name": [self.from_text(), ],
            "activity_date": [self.from_text(), ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Need to show list of properties available w.r.t. given event")
        return []


class PackageByBudgetForm(FormAction):
    def name(self):
        return "package_by_budget_form"

    def required_slots(self, tracker) -> List[Text]:
        return ["budget", "destination"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "budget": [self.from_text(), ],
            "destination": [self.from_text(), ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Show available packages")
        return []


class ModifyCancelBookingForm(FormAction):
    def name(self):
          return "modify_cancel_booking_form"

    def required_slots(self, tracker) -> List[Text]:
        return ["booking_ID", "cancel_reschedule"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "booking_ID": [self.from_text(), ],
            "cancel_reschedule": [self.from_text(), ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Respective Modify/Cancel action acknowledgement")
        return []

class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'
    def run(self, dispatcher, tracker, domain):
        if tracker.latest_message['intent'].get('name') == "greet":
            dispatcher.utter_template('utter_greet', tracker)
        return[AllSlotsReset()]
