# game_logic/music_game.py

# Initial key mappings for instruments
PIANO_KEYS = {
    'a': 'C4', 's': 'D4', 'd': 'E4', 'f': 'F4', 'g': 'G4', 'h': 'A4', 'j': 'B4', 'k': 'C5'
}

DRUM_KEYS = {
    '1': 'kick', '2': 'snare', '3': 'hihat', '4': 'tom1', '5': 'tom2', '6': 'crash'
}

# The currently active instrument, starting with piano
current_instrument = PIANO_KEYS

def get_note_for_key(key):
    """
    Returns the note or sound corresponding to the key for the active instrument.
    If the key is invalid, returns None.
    """
    return current_instrument.get(key)

def switch_instrument(instrument_name):
    """
    Switches the active instrument based on the provided instrument name.
    """
    global current_instrument
    if instrument_name == 'piano':
        current_instrument = PIANO_KEYS
    elif instrument_name == 'drums':
        current_instrument = DRUM_KEYS
    else:
        raise ValueError(f"Unknown instrument: {instrument_name}")
