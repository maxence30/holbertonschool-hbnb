# Projet HBnB - Partie 2 : Logique métier

## Description
Ce projet fait partie de l'école Holberton.  
Dans cette partie, j'ai implémenté les **classes principales de la logique métier** pour l'application HBnB.  

Les classes créées sont :

- **BaseModel** : classe de base avec `id`, `created_at` et `updated_at`.
- **User** : représente un utilisateur, avec ses places et reviews.
- **Place** : représente un logement, avec ses reviews et amenities.
- **Review** : représente un avis, lié à un utilisateur et un logement.
- **Amenity** : représente un service ou équipement (WiFi, Piscine...), lié à plusieurs logements.

Les relations entre les classes sont correctement gérées et les validations des données sont incluses (email, rating, prix, etc.).

## Organisation des fichiers

part2/
-models/
--init.py
--base_model.py
--user.py
--place.py
--review.py
--amenity.py
-README.md

## Tests
J'ai utilisé un fichier `test.py` pour vérifier la création des objets et leurs relations.  
Exemple de test : créer un utilisateur, un logement, un review et un amenity et vérifier que tout est bien lié.  
