# holbertonschool-hbnb

This is a Holberton project that aims to recreate the Airbnb platform.

It includes the following diagrams:
- High-Level Package Diagram
- Detailed Class Diagram for the Business Logic Layer
- Sequence Diagrams for API Calls
- Technical Document

## High-Level Package Diagram

![High-Level Package Diagram](part1/diagramme_de_package.png)

## Class Diagram for the Business Logic Layer

![Class Diagram](part1/Diagramme_de_class.png)

## Sequence Diagrams for API Calls

--- User Registration ---
sequenceDiagram
User->>API: Register User (POST /users)
API->>BusinessLogic: Validate Input & Create User
BusinessLogic->>Database: Insert New User
Database-->>BusinessLogic: Return Success/Failure
BusinessLogic-->>API: Return Result
API-->>User: Registration Confirmation

--- Place Creation ---
sequenceDiagram
User->>API: Create Place (POST /places)
API->>BusinessLogic: Validate & Process Place Data
BusinessLogic->>Database: Save Place Information
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Created Place Details
API-->>User: Place Created Response

--- Review Submission ---
sequenceDiagram
User->>API: Submit Review (POST /reviews)
API->>BusinessLogic: Validate Review & Associate with Place/User
BusinessLogic->>Database: Save Review
Database-->>BusinessLogic: Confirm Review Saved
BusinessLogic-->>API: Return Review Confirmation
API-->>User: Review Submission Success

--- Fetch Places ---
sequenceDiagram
User->>API: Get Places (GET /places?criteria=...)
API->>BusinessLogic: Process Filters & Query Logic
BusinessLogic->>Database: Retrieve Matching Places
Database-->>BusinessLogic: Return Place Data
BusinessLogic-->>API: Format Response
API-->>User: Return List of Places
