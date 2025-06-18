
from flask import jsonify
from dateutil import parser

def handle_reminder(req):
    params = req["queryResult"]["parameters"]
    task = params.get("task")
    time_str = params.get("time")

    # Parse time using dateutil
    if time_str:
        try:
            time_obj = parser.parse(time_str)
            confirmation = f"Got it! I'll remind you to '{task}' at {time_obj.strftime('%I:%M %p')}."
        except Exception as e:
            confirmation = f"Sorry, I couldn't understand the time: {time_str}"
    else:
        confirmation = "Sorry, please specify a time for the reminder."

    return jsonify({
        "fulfillmentText": confirmation
    })
