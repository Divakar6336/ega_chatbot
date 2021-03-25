from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
import requests
import json
from db_connect import get_order_status
from db_connect import get_eta_status
from db_connect import get_ets_status
from db_connect import get_order_value

class ActionOrderDetails(Action):
    def name(self):
        return 'action_order_details'

    def run(self, dispatcher, tracker, domain):
    	order_id = tracker.get_slot('order_number')
    	print("Status order",order_id)
    	text_=get_order_status(order_id)
    	print(type(text_))
    	if text_ is None:
    		dispatcher.utter_message("Record doesn't exist")
    	else:
    		dispatcher.utter_message("Status of order number:"+str(order_id)+'\n Your Order Status: '+str(text_))
       
class ActionOrderETADetails(Action):
    def name(self):
        return 'action_order_eta_details'

    def run(self, dispatcher, tracker, domain):
    	order_id = tracker.get_slot('order_number')
    	text=get_eta_status(order_id)
    	if text is None:
    		dispatcher.utter_message("Record doesn't exist")
    	else:
    		dispatcher.utter_message("ETA details of order number:"+str(order_id)+'\n Your Order ETA: '+str(text))
       
class ActionOrderETSDetails(Action):
    def name(self):
        return 'action_order_ets_details'

    def run(self, dispatcher, tracker, domain):
        order_id = tracker.get_slot('order_number')
        text=get_ets_status(order_id)
        if text is None:
        	dispatcher.utter_message("Record doesn't exist")
        else:
        	dispatcher.utter_message("ETS details of order number:"+str(order_id)+'\n Your Order ETS: '+str(text))
            

class ActionOrderValue(Action):
    def name(self):
    	return 'action_order_value'

    def run(self, dispatcher, tracker, domain):
    	order_id = tracker.get_slot('order_number')
    	text=get_order_value(order_id)
    	if text is None:
    		dispatcher.utter_message("Record doesn't exist")
    	else:
    		dispatcher.utter_message("Order value of order number:"+str(order_id)+'\n Your Order Value: USD '+str(text))
       

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




 # text="Call API: http://dubal5136v/PortalWS/PortalCPWS.asmx?op=Bot_Get_ETA"
       # PARAMS={'user_id':'admin','password':'12345'}
       # req = requests.get('http://127.0.0.1:8081/', params = PARAMS)
       # req_dict = json.loads(req.text)
       # return [SlotSet('order_number',order_id)]    