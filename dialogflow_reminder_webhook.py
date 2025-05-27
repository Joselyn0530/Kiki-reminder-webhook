
from flask import Flask, request, jsonify
from datetime import datetime
from dateutil import parser

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    parameters = req.get("queryResult", {}).get("parameters", {})
    task = parameters.get("reminder_task", "your task")
    time_raw = parameters.get("reminder_time", "")

    # Try formatting time
    try:
        dt = parser.isoparse(time_raw)
        formatted_time = dt.isoformat()
    except Exception as e:
        print("Failed to parse time:", e)
        formatted_time = time_raw  # fallback to raw

    response = {
        "fulfillmentText": f"Got it! I'll remind you to {task} at {formatted_time}.",
        "payload": {
            "richContent": [
                [
                    {
                        "type": "info",
                        "title": "Reminder placed successfully",
                        "subtitle": f"{task}|{formatted_time}"
                    }
                ]
            ]
        }
    }
    return jsonify(response)

@app.route('/')
def health():
    return 'Webhook is running.', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
