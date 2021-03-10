from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse



app = Flask(__name__)
level = 0

@app.route('/bot', methods=['POST'])
def bot():
    global level
    order = {}
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if '0' in incoming_msg and level ==0  :
        # return a quote
        reply = 'All Categories \n\t1. Chicken\n\t2. Chickish\n\t3. Fish\n\t4. Frozen Food\n\t5. Marinated Meat\n\t6. Prawns\n\t7. Promotions'
        level = 1
        msg.body(reply)
        responded = True

    elif '1' in incoming_msg and level == 1:
        # return a quote
        reply = 'Chicken\n\t1. Whole Chicken Meat - Rs.100\n\t2. Chicken Boneless - Rs.100\n\t3. Fresh Chicken (Karahi Cut) - Rs.100\n\t4. Chicken Boneless (Cube) - Rs.100\n\t5. Chicken Boneless (Filet) - Rs.100\n\t6. Chicken Boneless (Finger) - Rs.100\n\t7. Chicken Mince - Rs.100\n\t8. Fresh Chicken (Korma Cut) - Rs.100'
        level = 2
        msg.body(reply)
        responded = True

    elif '1' in incoming_msg and level == 2:
        # return a quote
        reply = 'Enter the quantity in numbers'
        level = 4
    #    thisdict.update({"Whole Chicken Meat": ["0","0"]})
        msg.body(reply)
        responded = True
#    if level  == 4:
#        reply = incoming_msg
#        level = level + 1
#        thisdict.update({"Whole Chicken Meat": ["0","0"]})
#        msg.body(reply)
#        responded = True
    elif not responded and level == 0:
        reply = 'Reply with "0" to get started with the order'
        msg.body(reply)
        level = 0
    elif not responded :
        reply = 'select the right option from above'
        msg.body(reply)
    return str(resp)


if __name__ == '__main__':
    app.run()
