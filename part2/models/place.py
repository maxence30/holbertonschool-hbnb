from models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        if price <= 0:
            raise ValueError("Price must be positive")

        if not (-90 <= latitude <= 90):
            raise ValueError("Invalid latitude")

        if not (-180 <= longitude <= 180):
            raise ValueError("Invalid longitude")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []      
        self.amenities = []

        # Ajout de cette place à l'utilisateur
        owner.places.append(self)
