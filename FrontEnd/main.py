from flask import Flask, render_template, request
from func import *

# Create a Flask app
app = Flask(__name__)

item_list = ['apple', 'banana', 'strawberry', 'coconut', 'bread', 'coca-cola']

# Define a route for handling GET requests
@app.route('/', methods=['GET'])
def get_value():
    return render_template('main.html', item_list=item_list, item_list_length=len(item_list))

@app.route('/get_bought_items', methods=['POST', 'GET'])
def query_bought_items():
    if request.method == 'GET':
        return render_template('bought-items.html', method="GET")
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # print(get_bought_items(username, password))

        # print(username, password)
        print(type(get_bought_items(username, password)))
        return render_template('bought-items.html', method="POST", bought_items=get_bought_items(username, password))

@app.route('/buy_items', methods=['POST'])
def send_buy_request():
    counter = request.form.get("counter")
    item = request.form.get("item-name")
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "" or password == "":
        return {"status":"error", "msg":"Invalid username or password"}

    print(counter, item, username, password)
    buy_items(counter, item, username, password)

    return {"status":"ok"}


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0')