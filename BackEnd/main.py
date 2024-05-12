from flask import Flask, jsonify, request
from func import *

# Create a Flask app
app = Flask(__name__)

# Define a route for handling GET requests
@app.route('/buy_item', methods=['POST'])
def kafka_buy_item():
    data = request.data
    print(data)
    buy_item(data)

    return jsonify({'message': 'Item purchased successfully'}), 200
    
@app.route('/get_bought_items', methods=['POST'])
def get_bought_items():
    credentials = request.data
    print(credentials)
    data = query_bought_items(credentials)
    print(data)
    
    return data


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')