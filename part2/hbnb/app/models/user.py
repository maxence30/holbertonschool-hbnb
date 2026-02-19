from models.base_model import BaseModel
import re

class User(BaseModel):
    users_emails = set()

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()

        # Vérifications des noms
        if not first_name or not last_name:
            raise ValueError("First and last name cannot be empty")

        # Vérification email
        if not self.validate_email(email):
            raise ValueError("Invalid email format")

        if email in User.users_emails:
            raise ValueError("Email already exists")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

        self.places = []    # liste des places de l'utilisateur
        self.reviews = []   # liste des reviews de l'utilisateur

        User.users_emails.add(email)

    @staticmethod
    def validate_email(email):
        pattern = r"^[^@]+@[^@]+\.[^@]+$"
        return re.match(pattern, email)
