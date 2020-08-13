# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional
#from flask_cors import CORS, cross_origin
from rasa_sdk import Action, Tracker
from flask import Flask, redirect, url_for, request, render_template
import requests
import json
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import requests
#from flask import Flask, request
from rasa_sdk.events import SlotSet, AllSlotsReset
#from flask_restful import Resource, Api
#from flask_cors import CORS, cross_origin
# app = Flask(__name__)
# api = Api(app)
# CORS(app)
entity_dic = {"change_destination":"destination",
              "change_origin":"origin",
              "change_adults_count":"adults_count",
              "change_children_count":"child_count",
              "change_travel_date":"travel_date",
              "change_budget":"budget",
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
        # print("helloo")
        return "trip_plan_form"
    # def getUserdata(self,tracker):
    #     userObj={
    #         destination:tracker.latest_message.text
    #     }

    def required_slots(self, tracker) -> List[Text]:
        if tracker.get_slot("amenities") == True:
            return ["destination",
                    "origin",
                    "adults_count",
                    "child_count",
                    "travel_date",
                    "budget",
                    "amenities",
                    "property_type",
                    "facilities",
                    "packages"]
        else:
            return ["destination",
                    "origin",
                    "adults_count",
                    "child_count",
                    "travel_date",
                    "budget",
                    "amenities",
                    "packages"]

    # # @app.route('', methods=['POST'])
    # @cross_origin()
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "travel_date": [self.from_text(not_intent=["travel_menu", "greet", "stop"]),],
            "adults_count": [self.from_text(not_intent=["travel_menu", "greet", "stop"]),  ],
            "child_count": [self.from_text(not_intent=["travel_menu", "greet", "stop"]),  ],
            "budget": [self.from_text(not_intent=["travel_menu", "greet", "stop"]),  ],
            "destination": [self.from_text(not_intent=["travel_menu", "greet", "stop"]),  ],
            "origin": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ],
            "amenities": [self.from_intent(intent='affirm', value=True),
                          self.from_intent(intent='deny', value=False)],
            "property_type": [self.from_text(not_intent=["travel_menu", "greet", "stop"]),  ],
            "facilities": [self.from_text(not_intent=["travel_menu", "greet", "stop"]),  ],
            "packages": [self.from_intent(intent='affirm',value=True),
                          self.from_intent(intent='deny',value=False)]
           
        }
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        senddata={
            "destination": tracker.get_slot('destination') ,
            "origin" : tracker.get_slot('origin'),
            "adults": tracker.get_slot('adults'),
            "children": tracker.get_slot('child'),
            "travelstart":tracker.get_slot('travel_date'),
            "budgetrange":tracker.get_slot('budget'),
            "property_type":tracker.get_slot('property_type'),
            "facilities": tracker.get_slot('facilities'),
            'form_action_name':'trip_plan_form'

        }
        print(senddata)
        # print(self.lates)
        # data={
        #     tracker: tracker
        # }
        # x = requests.post('http://localhost:3456/chatbot',json=senddata)
        # print(x,x.text)
        print(tracker.get_slot('packages'))
        button_resp=[
                  {
                      "title": "yes",
                      "payload": "Yes"
                  },
                  {
                      "title": "no",
                      "payload": "No"
                  }
              ]
        custom_payload={
                "payload":"packages",
                "question":"display_packages"
            }
        custom_payload1={
                "payload":"properties",
                "question": "display_properties"
            }
              
    
        if tracker.get_slot('packages') == True:
            
            dispatcher.utter_message("Hey dude! Wait a sec, retrieving best package deals along with activities for you!",json_message=custom_payload)
            # dispatcher.utter_custom_message("Would you like to add aditional services/activities?",json_message=custom_payload,buttons=button_resp)

        else:
            dispatcher.utter_message("Hey dude! Wait a sec, retrieving properties for you!",json_message=custom_payload1)
            # dispatcher.utter_message("Would you like to add aditional services/activities?",buttons=button_resp)

        # if tracker.get_slot('additional_services') == True:
        #     dispatcher.utter_message("here are some amazing packages with activities included. Check them out!")

        # dispatcher.utter_message(x.text)
        return []

class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'
    def run(self, dispatcher, tracker, domain):
        if tracker.latest_message['intent'].get('name') == "greet":
            dispatcher.utter_template('utter_greet', tracker)
        return[AllSlotsReset()]
        
class ActivityPackageSearchForm(FormAction):
    def name(self):
        return "activity_package_search_form"

    def required_slots(self, tracker) -> List[Text]:
        return ["activity_name", "activity_date"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "activity_name": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ],
            "activity_date": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        buttons=[]
        custom_payload={
                "payload":"activities",
                "question":"display_activities"
            }
              
        dispatcher.utter_message("here fetching you some amazing destinations with properties where your desired activity is available! wait a sec!", json_message=custom_payload)
        return []

class PackageByBudgetForm(FormAction):
    def name(self):
        return "package_by_budget_form"

    def required_slots(self, tracker) -> List[Text]:
        return ["budget", "destination"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "budget": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ],
            "destination": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        custom_payload={
                "payload":"budget",
                "question":"display_budget"
            }
              
        dispatcher.utter_message("Showing some amazing packages under the budget you mentioned", json_message=custom_payload)
        return []

class ModifyCancelBookingForm(FormAction):
    def name(self):
        return "modify_cancel_booking_form"

    def required_slots(self, tracker) -> List[Text]:
        return ["cancel_reschedule","booking_ID"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cancel_reschedule": [self.from_text()],
            "booking_ID": [self.from_text(), ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        custom_payload={
                "payload":"cancel",
                "question":"cancel"
            }
        custom_payload1={
                "payload":"modify",
                "question":"modify"
            }
        if tracker.get_slot('cancel_reschedule') == 'cancel':
            dispatcher.utter_message("Your booking is cancelled succesfully", json_message=custom_payload)
        else :
            dispatcher.utter_message("let me take you to the rescheduling page!", json_message=custom_payload1)
        return []
class tracking(FormAction):
    def name(self):
        return "track_booking_form"

    def required_slots(self, tracker) -> List[Text]:
        return ["booking_ID"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "booking_ID": [self.from_text(not_intent=["travel_menu", "greet", "stop"]), ]
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        custom_payload={
                "payload":"track",
                "question":"track"

            }
              
        dispatcher.utter_message("Let me fetch the tracking status of your booking!", json_message=custom_payload)
        return []



#flask requests from angular 
# app = Flask(__name__)
# context_set = ""
# cors = CORS(app)
# CORS(app)

# @app.route('/', methods = ['POST'])
# @cross_origin()
# def index():

#     if request.method == 'POST':
#         val = str(request.args.get('text'))
#         data = json.dumps({"sender": "Rasa","message": val})
#         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
#         res = res.json()
#         console.log(res.text)
#         val = res[0]['text']
#         print(val)
#         return {'status':'OK','code': 200}
# if __name__ == '__main__':
#   app.run(port=5055)