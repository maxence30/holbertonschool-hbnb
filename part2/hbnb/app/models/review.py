from models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, user, place):
        super().__init__()

        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        # Check if user already reviewed this place
        for review in place.reviews:
            if review.user == user:
                raise ValueError("User already reviewed this place")

        self.text = text
        self.rating = rating
        self.user = user
        self.place = place

        user.reviews.append(self)
        place.reviews.append(self)
