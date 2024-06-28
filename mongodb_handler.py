from flask_pymongo import PyMongo
import json

class MongoDBHandler:
    def __init__(self, app):
        self.mongo = PyMongo(app)

    def save_game_state(self, game):
        game_state = {
            "board": json.dumps(game.board),
            "turn": game.turn,
            "status": game.status,
            "result": game.result
        }
        self.mongo.db.game_state.update_one({}, {"$set": game_state}, upsert=True)

    def load_game_state(self):
        state = self.mongo.db.game_state.find_one()
        if state:
            state['board'] = json.loads(state['board'])
        return state if state else {}

