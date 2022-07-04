How do you decide which class to add methods to?
    which class does the method affect? put in this class
    what class does the method use in parameters? put in (parameters)

### test writing
               test function(self)  =  def test_pub_can_sell_drink__to_over_18(self):
call function and state perameters  =  self.pub1.sell_drink(self.drink3, self.customer_1)
     show what would change if the  =  self.assertEqual(104, self.pub1.till)
       function happens as desired  =  self.assertEqual(6, self.customer_1.wallet)



### MVP
Room
    entry fee. check guest has money and can afford
    capacity - can fit into room

Songs
    title  song.title is the title property
    artist song.artist the artist property

Guests
    wallet
    favourite song() woo print


encapsulation
    encapsulating properties and methods together into a single concept thus creating classes.
    you can override previous code and rename something:    
    def setUp(self):
        self.song = Song("Highway to Hell", "AC/DC")
        self.song.title = "lol, something else"
    single underscore.
    python doesn't have a concept of private properties.
        ._capacity = feeble attempt at making something private. please don't modify this. please dont change this property.
        "_" is a flag of please no change. 


def check_in_guest(Self, guest)
	arguments: guests. this is the only thing coming from the outside. assuming methods are already written
	1: check if guest can fit
	if self.free_spaces() == 0:
		return
	2: check if guest can afford fee
    	if not guest.can_afford:
		    none
    1&2: Or return together in an and statement
        if self.free_spaces() == 0 or not guest.can_afford:
		    none
	3: remove money from guest
        guest.pay(self.fee)
	4: add money to till
        self.till += self.fee
	5: add guest to list
        self.guests.append(guest)