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