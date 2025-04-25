from flask import Flask, jsonify, request
import logging
from tradingapi_a.mconnect import MConnect

app = Flask(__name__)

# Initialize the MConnect object
mconnect_obj = MConnect()

# Login function
@app.route('/login', methods=['POST'])
def login():
    user_id = request.json.get('user_id')
    password = request.json.get('password')
    login_response = mconnect_obj.login(user_id, password)
    return jsonify(login_response)

# Fetch live data (Price, Buy Rate, Stop Loss, etc.)
@app.route('/api/price', methods=['GET'])
def get_price():
    index = request.args.get('index')
    # Sample response for now, you can integrate real API calls
    data = {
        "price": 17200,  # This should be dynamic based on API data
        "buy": 17150,
        "stoploss": 17000,
        "target": 17300
    }
    return jsonify(data)

# Place Order
@app.route('/place_order', methods=['POST'])
def place_order():
    order_data = request.json
    # Call your place_order method here
    order_response = mconnect_obj.place_order(
        _tradingsymbol=order_data["tradingsymbol"],
        _exchange=order_data["exchange"],
        _transaction_type=order_data["transaction_type"],
        _order_type=order_data["order_type"],
        _quantity=order_data["quantity"],
        _product=order_data["product"],
        _validity=order_data["validity"],
        _price=order_data["price"],
        _trigger_price=order_data["trigger_price"]
    )
    return jsonify(order_response)

if __name__ == '__main__':
    app.run(debug=True)