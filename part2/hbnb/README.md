# HBnB - REST API (Holberton Project)

## Project Overview

HBnB is a RESTful API backend developed as part of the Holberton School curriculum.

The project follows a **layered architecture** composed of:
- Presentation Layer
- Business Logic Layer
- Persistence Layer

The application implements the **Facade Pattern** to centralize communication between layers and uses a **repository abstraction** to allow future integration of a database.

---

## Architecture

The project is organized into three main layers:

### Presentation Layer

#### app/api/v1/

Responsibilities:
- Define API endpoints
- Handle HTTP requests and responses
- Communicate exclusively with the Facade
- Return JSON responses

This layer contains no business logic.

---

### Business Logic Layer

#### app/services/

Responsibilities:
- Implement domain logic
- Validate input data
- Coordinate operations
- Interact with the repository interface
- Expose a Facade as a single entry point

The `facade.py` file centralizes all interactions between the API and the business services.

---

### Persistence Layer

#### app/persistence/

Responsibilities:
- Manage data storage
- Provide a repository interface
- Abstract storage logic from business logic

Currently, the persistence layer uses an **in-memory repository**.
This implementation will later be replaced with a database-backed solution (Part 3 of the project).

---

## Project Structure

hbnb/
├── app/
│ ├── api/
│ │ └── v1/
│ │ ├── users.py
│ │ ├── places.py
│ │ ├── reviews.py
│ │ ├── amenities.py
│ │
│ ├── models/
│ │ ├── user.py
│ │ ├── place.py
│ │ ├── review.py
│ │ ├── amenity.py
│ │
│ ├── services/
│ │ └── facade.py
│ │
│ ├── persistence/
│ └── repository.py
│
├── run.py
├── config.py
├── requirements.txt
├── README.md

---

## Design Patterns Used

### Facade Pattern

The API layer communicates only with the `Facade`.
This reduces coupling and provides a clear entry point for business operations.

Flow:

API → Facade → Business Logic → Repository

---

### Repository Pattern

The persistence layer exposes a repository interface.
The business layer depends on the abstraction, not the concrete implementation.

Benefits:
- Loose coupling
- Easy replacement of in-memory storage
- Database integration without modifying business logic

---

## Installation & Setup

### Clone the repository

```bash
git clone <repository_url>
cd hbnb
```

### Install dependencies

pip install -r requirements.txt

#### Author

