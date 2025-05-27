
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName")

    if intent == "MemoryGameIntent":
        # Send a payload that frontend can catch to start the game
        return jsonify({
            "fulfillmentMessages": [
                {
                    "payload": {
                        "game": "memory_match",
                        "action": "start"
                    }
                }
            ]
        })

    # Default fallback response
    return jsonify({
        "fulfillmentText": "Sorry, I didn't understand that."
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
