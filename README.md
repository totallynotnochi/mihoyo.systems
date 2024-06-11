# mihoyo.system

mihoyo.system is a Django-based web app that accesses and analyses *Genshin Impact* player data .

## Purpose

This project tries to provide a user-friendly interface for retrieving and displaying character information from Genshin Impact, including stats, constellations, and basic damage calculations.

## Goals

By the end of the project, I hoped to achieve the following:

*   Create a clean and intuitive UI that's easy for players to navigate.
*   Fetch character data accurately and efficiently using the Enka.Network API.
*   Display character information in a clear and organized manner.
*   Implement basic damage calculation functionality for player analysis. 

## Technologies Used

*   **Backend:**
    *   Python
    *   Django (Web framework)
    *   EnkaNetwork API Wrapper (For interacting with the Enka.Network API)
*   **Frontend:**
    *   HTML
    *   CSS (Massively theme from HTML5 UP)
    *   JavaScript (For minor interactions)

## How to Run

1.  **Clone the repository:**  
    ```bash
    git clone https://github.com/totallynotnochi/mihoyo.systems
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Start the Django server:**
    ```bash
    python manage.py runserver
    ```
4.  **Open in your browser:**


    Visit `http://127.0.0.1:8000/`
