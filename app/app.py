from flask import Flask, render_template, request, jsonify

# Import the music game logic
from game_logic.music_game import get_note_for_key, switch_instrument

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/play-note', methods=['POST'])
def play_note():
    key = request.json.get('key')
    note = get_note_for_key(key)
    if note:
        return jsonify({'note': note}), 200
    else:
        return jsonify({'error': 'Invalid key'}), 400

@app.route('/switch-instrument', methods=['POST'])
def switch_inst():
    instrument_name = request.json.get('instrument')
    try:
        switch_instrument(instrument_name)
        return jsonify({'message': f'Switched to {instrument_name}'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
