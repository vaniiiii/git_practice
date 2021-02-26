# Defining Art class
class Art: 
  # Constructor
  def __init__(self, artist, title, medium , year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  # Printing method
  def __repr__(self):
    return self.artist + ". " + "\"" + self.title + "\"" + ". " + str(self.year) + ", " + self.medium + ". " + self.owner.name + ", " + self.owner.location + "."
# Defining Marketplace class
class Marketplace:
# Constructor
 def __init__(self):
   self.listings = []
# Add listing method
 def add_listing(self, new_listing):
   self.listings.append(new_listing)
# Remove listing method
 def remove_listing(self, expired_listing):
   self.listings.remove(expired_listing)
# Show listenings method
 def show_listings(self):
   for listing in self.listings:
     print(listing)
# Defining Client Class
class Client:
# Constructor
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
# Sell artwork method
  def sell_artwork(self, artwork, price):
      if artwork.owner == self:
       listing_item = Listing(artwork, price, self)
       veneer.add_listing(listing_item)  
  def buy_artwork(self,artwork):
    if artwork.owner != self:
      # hack
      art_listing = None
      for listing in veneer.listings:
        if artwork == listing.art:
         art_listing = listing
         artwork.owner = self
         veneer.remove_listing(art_listing)
        else: 
          continue


# Listing class
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return self.art.title + str(self.price)




# Object veneer
veneer = Marketplace()
#veneer.show_listings()
edytta = Client("Edytta Halpirt", "Private Collection", False)
moma = Client("The MOMA", "New York", True)
# Object girl_with_mandolin
girl_with_mandolin = Art("Piccaso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
# print(girl_with_mandolin)
edytta.sell_artwork(girl_with_mandolin, 6000000)
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()