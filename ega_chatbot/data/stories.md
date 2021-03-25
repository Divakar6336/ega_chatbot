## greetings
* greet
  - utter_greet

## check order status
* order_status
  - utter_get_order_number
  - form{"name":"order_form"}
  - action_order_details     
* order_status{"order_number":"12345"}
  - form{"name":"order_form"}
  - slot{"order_number":"12345"}
  - action_order_details
* goodbye
  - utter_goodbye 

## check order eta
* order_status_eta
  - utter_get_order_number
  - slot{"order_number":"12345"}
  - action_order_eta_details
* order_status_eta{"order_number":"12345"}
  - slot{"order_number":"12345"}
  - action_order_eta_details
* goodbye
  - utter_goodbye  
  
## check order ets 
* order_status_ets
  - utter_get_order_number
  - slot{"order_number":"12345"}
  - action_order_ets_details
* order_status_ets{"order_number":"12345"}
  - slot{"order_number":"12345"}
  - action_order_ets_details
* goodbye
  - utter_goodbye 
  
## check order value
* order_value
  - utter_get_order_number
  - slot{"order_number":"12345"}
  - action_order_value
* order_value{"order_number":"12345"}
  - slot{"order_number":"12345"}
  - action_order_value

## check my shipment details 
* my_shipment_details
  - utter_my_shipment_details  
  
## check shipment details 
* shipment_details
  - utter_shipment_details

## check lme price
* lme_price
  - utter_lme_price

## check lme trends
* lme_trends
  - utter_lme_trends 

## check active standing instructions
* active_standing_instructions
  - utter_active_standing_instructions

## check expired standing instructions
* expired_standing_instructions
  - utter_expired_standing_instructions

## check cancelled standing instructions
* cancelled_standing_instructions
  - utter_cancelled_standing_instructions

## check my order detail
* my_order_details
  - utter_my_order_details  
  
## check order detail
* order_details
  - utter_order_details

## check price setting
* price_setting
  - utter_price_setting  

## say goodbye
* goodbye
  - utter_goodbye