
from flask import jsonify

def handle_play_game():
    return jsonify({
        "fulfillmentMessages": [
            {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "info",
                                "title": "Let's play a game! 🎮",
                                "subtitle": "Pick one to get started:"
                            },
                            {
                                "type": "button",
                                "text": "Match Memory 🧠",
                                "event": {
                                    "name": "MemoryGameEvent",
                                    "languageCode": "en"
                                }
                            },
                            {
                                "type": "button",
                                "text": "Reaction Test ⚡",
                                "event": {
                                    "name": "ReactionTestEvent",
                                    "languageCode": "en"
                                }
                            },
                            {
                                "type": "button",
                                "text": "Sequence 🔢",
                                "event": {
                                    "name": "SequenceGameEvent",
                                    "languageCode": "en"
                                }
                            },
                            {
                                "type": "button",
                                "text": "Stroop Effect 🎨",
                                "event": {
                                    "name": "StroopEffectEvent",
                                    "languageCode": "en"
                                }
                            }
                        ]
                    ]
                }
            }
        ]
    })
