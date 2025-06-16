from flask import Flask, jsonify

app = Flask(__name__)

# Static data for last 5 IPL winners
ipl_winners = [
    {"year": 2025, "winner": "Royal Challengers Bengaluru"},
    {"year": 2024, "winner": "Kolkata Knight Riders"},
    {"year": 2023, "winner": "Chennai Super Kings"},
    {"year": 2022, "winner": "Gujarat Titans"},
    {"year": 2021, "winner": "Chennai Super Kings"}
]

@app.route('/ipl-winners', methods=['GET'])
def get_ipl_winners():
    return jsonify(ipl_winners)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)