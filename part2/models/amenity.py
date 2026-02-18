from models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):  
        super().__init__()
        self.name = name  
        self.places = []

    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)
            place.amenities.append(self)
