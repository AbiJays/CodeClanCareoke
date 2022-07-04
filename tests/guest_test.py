import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Novus Fancy-Foam", 20)
    
    def test_guest_has_name(self):
        self.assertEqual("Novus Fancy-Foam", self.guest_1.name)

    def test_guest_has_money(self):
        self.ssertEqual(20, self.guest_1.wallet)

    
    