from flask import Flask, jsonify, request
from threading import Thread
from func import *

# Create a Flask app
app = Flask(__name__)
    
@app.route('/purchased_items', methods=['POST'])
def get_bought_items():
    credentials = request.data.decode('utf-8').split(',')
    print(credentials)
    return(get_purchased_items(credentials))




kafka_consumer_thread = Thread(target=consume_and_add_purchases)
kafka_consumer_thread.daemon = True
kafka_consumer_thread.start()

# Run the Flask app
if __name__ == '__main__':
    
    app.run(debug=True, port=6000, host='0.0.0.0')