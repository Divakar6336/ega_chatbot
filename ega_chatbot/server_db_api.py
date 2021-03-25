from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
import requests
import json
from db_connect import get_order_status

class ActionOrderDetails(Action):
    def name(self):
        return 'action_order_details'

    def run(self, dispatcher, tracker, domain):
       # text_="http://dubal5136v/PortalWS/PortalCPWS.asmx?op=Bot_Get_status_order_number"
       order_id = tracker.get_slot('order_number')
       print("Status order",order_id)
       text=get_order_status(order_id)
       PARAMS={'user_id':'admin','password':'12345'}
       req = requests.get('http://127.0.0.1:8081/', params = PARAMS)
       req_dict = json.loads(req.text)
       print(text)
       dispatcher.utter_message("Status of order number:"+str(order_id)+","+req_dict["data"]+'; Your Order Status: '+text_)
       # return [SlotSet('order_number',order_id)]  

class ActionOrderETADetails(Action):
    def name(self):
        return 'action_order_eta_details'

    def run(self, dispatcher, tracker, domain):
       # text="Call API: http://dubal5136v/PortalWS/PortalCPWS.asmx?op=Bot_Get_ETA"
       order_id = tracker.get_slot('order_number')
       text=get_eta_status(order_id)
       dispatcher.utter_message("ETA detials of order number:"+str(order_id)+","+text)
       # return [SlotSet('order_number',order_id)]  

class ActionOrderETSDetails(Action):
    def name(self):
        return 'action_order_ets_details'

    def run(self, dispatcher, tracker, domain):
       # text="Call API: http://dubal5136v/PortalWS/PortalCPWS.asmx?op=Bot_Get_ETS"
       order_id = tracker.get_slot('order_number')
       text=get_ets_status(order_id)
       dispatcher.utter_message("ETS detail of order number:"+str(order_id)+", "+text)
       # return [SlotSet('order_number',order_id)]         

class ActionOrderValue(Action):
    def name(self):
      return 'action_order_value'

    def run(self, dispatcher, tracker, domain):
      # text="Call API: http://dubal5136v/PortalWS/PortalCPWS.asmx?op=Bot_Get_order_value"
      order_id = tracker.get_slot('order_number')
      text=get_ets_status(order_id)
      dispatcher.utter_message("Order value of order number:"+str(order_id)+","+text)
       # return [SlotSet('order_number',order_id)]     


class OrderForm(FormAction):
    def name(self):
        """Unique identifier of the form"""
        return "order_form"

    @staticmethod
    def required_slots(tracker):
        """A list of required slots that the form has to fill.
        Use `tracker` to request different list of slots
        depending on the state of the dialogue
        """
        print(tracker.get_slot('order_number'))
        return ["order_number"]

    def submit(self):
        """Define what the form has to do
              after all required slots are filled"""
        dispatcher.utter_template('utter_submit',tracker)    

        return []    