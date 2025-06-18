
from flask import Flask, request, jsonify
from dialogflow_game_webhook import handle_game
from dialogflow_reminder_webhook import handle_reminder
from play_game_buttons import handle_play_game

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName")

    if intent == "MemoryGameIntent":
        return handle_game(req)
    elif intent == "SetReminderIntent":
        return handle_reminder(req)
    elif intent == "PlayGameIntent":
        return handle_play_game()
    else:
        return jsonify({ "fulfillmentText": "Sorry, I didn’t understand that." })

if __name__ == '__main__':
    app.run()
