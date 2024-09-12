from flask import Flask, request, jsonify
from scraper import fetch_table_data

app = Flask(__name__)

# Fetch the data once and store it in memory
data = fetch_table_data()

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
    app.run(debug=True)
