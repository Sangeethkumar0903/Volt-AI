from flask import Flask, jsonify
from battery_control import adjust_battery_power

app = Flask(__name__)

@app.route('/battery-status', methods=['GET'])
def battery_status():
    response = adjust_battery_power()
    return jsonify(response)

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)