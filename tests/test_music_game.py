import sys
import os

# Modify sys.path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# Now you can import your game_logic module correctly
from game_logic.music_game import get_note_for_key, switch_instrument

import unittest

class TestMusicGame(unittest.TestCase):

    def test_get_note_for_piano_key(self):
        switch_instrument('piano')
        self.assertEqual(get_note_for_key('a'), 'C4')
        self.assertEqual(get_note_for_key('k'), 'C5')
        self.assertIsNone(get_note_for_key('z'))  # Invalid key

    def test_get_note_for_drum_key(self):
        switch_instrument('drums')
        self.assertEqual(get_note_for_key('1'), 'kick')
        self.assertEqual(get_note_for_key('6'), 'crash')
        self.assertIsNone(get_note_for_key('a'))  # Invalid key for drums

    def test_switch_instrument(self):
        switch_instrument('piano')
        self.assertEqual(get_note_for_key('a'), 'C4')
        switch_instrument('drums')
        self.assertEqual(get_note_for_key('1'), 'kick')

    def test_invalid_instrument_switch(self):
        with self.assertRaises(ValueError):
            switch_instrument('guitar')  # Should raise an exception

if __name__ == '__main__':
    unittest.main()
