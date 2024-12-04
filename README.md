# mihoyo.system

mihoyo.system is a Django-based web app that accesses and analyses *Genshin Impact* player data.

## IMPORTANT

This was a culminating project for ICS4U1 in the Ontario curriculum. Please dont use this as reference as teachers mark very differently. 

This project is a complete dead-end, its a barebones webapp that should work as long as Enka's APIs don't go through major changes. Heavy dependency on the python wrapper for the Enka API.

Most of the code is actually just HTML logic, which properly fucked me over. Thank you to the lords of HTML for providing me with a week of trying to tear my hair out. 

The python logic is in the mainpage app, see for yourself on what does what.

## Purpose

~~This project tries to provide a user-friendly interface for retrieving and displaying character information from Genshin Impact, including stats, constellations, and basic damage calculations.~~

To get a somewhat high grade for my CS class

(i did get a 95 on my project so i'll take it)

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

(TAKE THIS WITH A GRAIN OF SALT)

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
