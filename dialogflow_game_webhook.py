
from flask import jsonify

def handle_game(req):
    # Example: triggers Memory Match game
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
