import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("The Python Programming Song", "Fynn Freund and Kim Ly")
    
    def test_song_has_title(self):
        self.assertEqual("The Python Programming Song", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Fynn Freund and Kim Ly", self.song_1.artist)