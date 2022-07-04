class Room:
    
    def __init__(self, name, songs):
        self.name = name
        # why don’t you need to include lists etc in parameters of the def__init__ of a Class?
        self.songs = songs
        self.guests = []
    
    # def add_song(self, songs, new_song):
    #     self.songs.append(new_song)
    def add_song(self, new_song):
        self.songs.append(new_song)
        # because you reference self.songs you dont need to then reference 'songs' in the parameter as in above.

    
    # def add_songs(self, songs)
    
    def check_guest_in(self, guests, new_guest):
        #check pub sell if over 18
        if self.guest.wallet >= 3:
            return "Not enough money Pal. Get outta here!"
        self.guests.append(new_guest)
    
    def check_guest_out(self, guests, old_guest):
        self.guests.remove(old_guest)

        # capacity limit is a quality that is stated in booking but not explicitly in code?
