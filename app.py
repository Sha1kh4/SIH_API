from flask import Flask, request, jsonify
from scraper import fetch_table_data
from threading import Thread
import time

app = Flask(__name__)

# Fetch the data once and store it in memory
data = fetch_table_data()
def update_data():
    global data
    while True:
        time.sleep(900)  # Sleep for 15 minutes
        data = fetch_table_data()  # Fetch new data

@app.route('/')
def index():
    return f"To use this API call, use the format: /api/data?ps_number='ps_number'.\nFor example: /api/data?ps_number=SIH1524"

@app.route('/api/data', methods=['GET'])
def get_data():
    ps_number = request.args.get('ps_number')
    
    if not ps_number:
        return jsonify({"error": "PS Number is required"}), 400
    
    # Find the matching data
    result = [item for item in data if item.get('PS Number') == ps_number]
    
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "No data found for the provided PS Number"}), 404

if __name__ == '__main__':
    # Fetch data for the first time
    data = fetch_table_data()
    
    # Start the data update thread
    thread = Thread(target=update_data)
    thread.daemon = True
    thread.start()
    
    # Run the Flask app
    app.run(debug=True)
