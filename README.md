# Quant-Trading Full-Stack Application

This project is a full-stack web application for running quantitative trading backtests. It uses Django for the backend and React for the frontend.

## Prerequisites

Before you start, please ensure you have the following installed on your system:
*   **Python (3.8 or newer)** and its package installer, `pip`.
*   **Node.js** and its package manager, `npm`.

---

## 1. Installation

First, you'll need to install the dependencies for both the Django backend and the React frontend.

**a. Backend (Django)**

It is a best practice to use a virtual environment to manage your Python dependencies.

1.  Navigate to the root directory of the repository in your terminal.
2.  Create a Python virtual environment:
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    *   On macOS or Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```
4.  Install the required Python packages using `pip` and the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

**b. Frontend (React)**

1.  From the root of the repository, navigate into the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install the required Node.js packages using `npm`:
    ```bash
    npm install
    ```

---

## 2. Running the Application

You need to run the backend and frontend servers simultaneously in two separate terminal windows.

**a. Start the Django Backend Server**

Open a new terminal window for the backend.

1.  Make sure you are in the project's root directory.
2.  Activate the virtual environment if it isn't already:
    ```bash
    source venv/bin/activate
    ```
3.  Change into the Django project directory:
    ```bash
    cd quant_trading_app
    ```
4.  Start the Django development server on port 8080:
    ```bash
    python manage.py runserver 0.0.0.0:8080
    ```
    You should see output indicating the server is running and listening on `http://0.0.0.0:8080/`.

**b. Start the React Frontend Server**

Open a **second, separate** terminal window for the frontend.

1.  From the root of the repository, navigate into the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Start the React development server:
    ```bash
    npm start
    ```
    This command should automatically open a new tab in your default web browser.

---

## 3. Accessing the Application

Once both servers are running, you can access the application by navigating to the following URL in your web browser:

**http://localhost:3000**

You should see the "MACD Backtest" interface, ready for you to input parameters and run the analysis.
