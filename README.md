# Synonym Finder

A modern, "Vibrant and Premium" web application built with Flask that helps users find synonyms.

## Features
- **UI**: Glassmorphism design with animated backgrounds.
- **Backend**: Python Flask app integrating with the Datamuse API.
- **Documentation**: Includes a user guide in `synonym_user_guide.md`.

## Installation

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    python app.py
    ```
4.  Open `http://localhost:5000` in your browser.

## Documentation
See [User Guide](synonym_user_guide.md) for detailed usage instructions.

## Running with Docker (Recommended)

To run the application in a containerized environment:

1.  Ensure **Docker Desktop** is installed and running.
2.  Run the following command in the project root:
    ```bash
    docker compose up --build
    ```
3.  Access the app at `http://localhost:5000`.
