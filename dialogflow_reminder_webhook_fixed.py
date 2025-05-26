
from flask import Flask, request, jsonify
from datetime import datetime
from dateutil import parser

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    print("Request received:", req)

    # Extract parameters
    reminder_task = req.get("queryResult", {}).get("parameters", {}).get("reminder_task", "something")
    reminder_time_raw = req.get("queryResult", {}).get("parameters", {}).get("reminder_time")

    # Default fallback
    formatted_time = reminder_time_raw

    try:
        dt = parser.isoparse(reminder_time_raw)
        formatted_time = dt.strftime("%Y-%m-%d %-I:%M%p").lower()  # Example: 2025-05-27 3:00am
    except Exception as e:
        print("Error formatting time:", e)

    response = {
        "fulfillmentText": f"I'll remind you to {reminder_task} at {formatted_time}.",
        "payload": {
            "richContent": [
                [
                    {
                        "type": "info",
                        "title": "Reminder placed successfully",
                        "subtitle": f"{reminder_task}|{formatted_time}"
                    }
                ]
            ]
        }
    }
    return jsonify(response)

@app.route('/')
def health_check():
    return 'Webhook is live!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
