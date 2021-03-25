## intent:greet
- hey
- hello
- hi
- hii
- hiii
- good morning
- good afternoon
- good evening
- hey there

## intent:order_status
- What is the status of my order [12345](order_number) ?
- What is the status of my order number [12345](order_number) ?
- What is the status of my order id [12345](order_number) ?
- status of order number [12345](order_number)
- status of order id [12345](order_number)
- status of order [12345](order_number)
- order status
- order status [12345](order_number)
- order status of [12345](order_number)
- order status of order id [12345](order_number)
- order status of order number [12345](order_number)
- order status
- order status of order number 23658

## intent:order_status_eta
- What is the ETA of my order [12345](order_number)  ?
- What is the ETA of my order number [12345](order_number)  ?
- What is the ETA of my order id [12345](order_number)  ?
- ETA of my order number [12345](order_number)
- ETA of my order id [12345](order_number)
- Expected time of arrival
- Expected time of arrival for order number [12345](order_number)
- eta of order id [12345](order_number)
- eta of order number [12345](order_number)
- order eta
- order eta of order number [12345](order_number)
- order eta of order id [12345](order_number)
- eta
- eta of [12345](order_number)

## intent:order_status_ets
- What is the ETS of my order [12345](order_number) ?
- What is the ETS of my order number [12345](order_number)  ?
- What is the ETS of my order id [12345](order_number)  ?
- ETS of my order number [12345](order_number)
- ETS of my order id [12345](order_number)
- Expected time of shipment
- Expected time of shipment for order number [12345](order_number)
- Expected time of shipment for order id [12345](order_number)
- order ets
- ets
- ets of [12345](order_number)
- ets of order [12345](order_number)
- ets of order number [12345](order_number)
- ets of order id [12345](order_number)

## intent:order_value
- What is the value of order [12345](order_number)  ?
- What is the value of order id [12345](order_number)  ?
- What is the value of order number [12345](order_number)  ?
- value of order id [12345](order_number)
- value of order number [12345](order_number)
- order value
- order value of [12345](order_number)
- order value of order id [12345](order_number)
- order value of order number [12345](order_number)
- value of order

## intent:provide_order_number
- [23456](order_number)
- [1234](order_number)
- [123456](order_number)

## intent:my_shipment_details
- How many shipments do I have in transit ?
- number of shipments I have in transit

## intent:shipment_details
- Show me the details of the Shipments in Transit
- Display the details of the Shipments in Transit 
- show me the details of Shipments which are arriving
- Arrival of Shipment
- Shipments in Transit

## intent:lme_price
- What is the current LME price?
- What is the present LME price?
- current lme price

## intent:lme_trends
- show me historical LME Prices 
- display me historical LME Prices
- LME 

## intent:active_standing_instructions
- What are my active standing instructions ?
- my active standing instructions

## intent:expired_standing_instructions
- Show my expired standing instructions ?
- expired standing instructions

## intent:cancelled_standing_instructions
- Show my cancelled standing instructions ?
- cancelled standing instructions

## intent:my_order_details
- How many orders have I declared this month ?
- My declared number of orders this month
- show my order details
- my order details 

## intent:order_details
- List the Order Details Declared this Month
- show order details of this Month

## intent:price_setting
- Show the price settings I have performed last week ?
- My last week price settings

## intent:goodbye
- bye
- by
- goodbye
- see you around
- see you later
- Talk to you later

## regex:order_number
- [0-9]{5}