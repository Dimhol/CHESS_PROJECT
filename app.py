from flask import Flask, render_template, jsonify, request
from constants import *
from main import Game
from mongodb_handler import MongoDBHandler

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/chessDB"


mongo_handler = MongoDBHandler(app)


game = Game(mongo_handler)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game-state', methods=['GET'])
def game_state():
    state = {
        "board": game.board,
        "turn": game.turn,
        "status": game.status,
        "result": game.result
    }
    return jsonify(state)

@app.route('/make-move', methods=['POST'])
def make_move():
    data = request.json
    from_pos = data['from']
    to_pos = data['to']
    result = game.make_move(from_pos, to_pos)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
