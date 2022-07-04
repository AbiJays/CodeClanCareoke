import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        # do only set up whats needed for all here otherwise you set up before each test? 
        # Whats the best order for this to be in too. I know you need to have things that will be called in objects stated already: for instance songs need to be called into existence before you can have a list of songs in the room. then I guess you need guest after room? it just looks messy and I want to know the best setUp
        self.song_1 = "Technologic", "Daft Punk"
        self.song_2 = "Mexican Fender", "Weezer"
        self.song_3 = "Code Monkey", "Jonathan Coulton"
        
        self.song_to_add = "And So You Code", "Mishu"

        self.songs = [self.song_1, self.song_2, self.song_3]

        self.guests = []

        self.room_1 = Room("School of Rock", self.songs)

        self.guest_1 = Guest("Novus Fancy-Foam", 20)
        
        self.guest_2 = Guest("Freddie Bramblesprout", 1)


    def test_room_has_name(self):
        self.assertEqual("School of Rock", self.room_1.name)

    # @unittest.skip("delete this line to run the test")
    def test_add_song(self):
        self.room_1.add_song(self.songs, self.song_to_add)
        self.assertEqual(4, len(self.songs))

    # @unittest.skip("delete this line to run the test")
    def test_check_guest_in(self):
        self.room_1.check_guest_in(self.room_1.guests, self.guest_1)
        self.assertEqual(1, len(self.room_1.guests))
        # add guest names to list. how do you reference empty list in tests. you make it in the setUp because this is the example?

    def test_guest_can_afford_entry(self):
        self.room_1.check_guest_in(self.room_1.guests, self.guest_1)
        self.room_1.check_guest_in(self.room_1, self.guest_2)
        self.assertEqual(1, len(self.room_1.guests))

    # @unittest.skip("delete this line to run the test")
    def test_check_guest_out(self):
        self.room_1.check_guest_in(self.guest_1, self.guest_1)
        # have to set up there being someone in the room to ensure removal method works.
        self.room_1.check_guest_out(self.room_1.guests, self.guest_1)
        self.assertEqual(0, len(self.room_1.guests))

# room capacity

    def test_favourite_song_on_song_list(self):
        favourite_song_expected = "Whoo!"
        favourite_song_actual = self.room_1.
        self.room.fav_song(self.guest_1.favourite_song, self.songs)
        self.assertEqual("whoo!", )

    def test_pub_can_sell_drink__too_drunk(self):
        drunk_expected = "Go home you're drunk" # expected 
        drunk_actual = self.pub1.sell_drink(self.drink3, self.customer_3) # actual
        self.assertEqual(100, self.pub1.till)
        self.assertEqual(35, self.customer_3.wallet)
        self.assertEqual(drunk_expected, drunk_actual)
        # could put string in drunk_expected and remove drunk expected
