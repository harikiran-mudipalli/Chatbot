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


class TripplanForm(FormAction):
    def name(self):
        return "trip_plan_form"

    def required_slots(self, tracker) -> List[Text]:
        return ["destination",
                "origin",
                "adults",
                "child",
                "pets",
                "travel_date",
                "travel_period",
                "budget",
                "amenities",
                "property_type",
                "facilities"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "travel_date": [self.from_text(), ],
            "travel_period": [self.from_text(), ],
            "pets": [self.from_entity(entity="pets"),
                     self.from_intent(intent='affirm',value=True),
                     self.from_intent(intent='deny',value=False)],
            "adults": [self.from_text(), ],
            "child": [self.from_text(), ],
            "budget": [self.from_text(), ],
            "destination": [self.from_text(), ],
            "origin": [self.from_text(), ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dest = tracker.get_slot('destination')
        print(dest)
        dispatcher.utter_message("❤️❤️❤️Thank you so much for showing your interest in traveling with us")
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