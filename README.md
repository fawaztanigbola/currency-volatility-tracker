# Currency Volatility Tracker

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-enabled-blue?style=flat&logo=docker)](https://www.docker.com/)
[![Tests](https://img.shields.io/badge/tests-pytest-green.svg)](https://docs.pytest.org/)

An asynchronous, lightweight FastAPI microservice designed to fetch historical exchange rates and calculate the statistical volatility (standard deviation) of various currencies against the US Dollar (USD). 

This repository also contains a collection of Python solutions for various algorithmic challenges in the `codewars/` directory.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Local Installation](#local-installation)
  - [Running the Application](#running-the-application)
  - [Running with Docker](#running-with-docker)
- [API Reference](#api-reference)
- [Running Tests](#running-tests)
- [Codewars Solutions](#codewars-solutions)
- [License](#license)

---

## Features

- **Asynchronous Architecture**: Built on FastAPI and utilizing `httpx` for non-blocking external API requests.
- **Statistical Analysis**: Custom `CurrencyAnalyzer` class that calculates:
  - Mean exchange rate over a given period.
  - Variance of exchange rates.
  - Volatility (Standard Deviation) of the target currency.
- **Robust Validation**: Strict query parameter validation ensuring currency codes conform to the ISO 4217 standard (3-letter alphabetic codes).
- **Dockerized**: Ready for containerized deployment.
- **Comprehensive Testing**: Unit tests implemented with `pytest`.

---

## Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python 3.10+** | Core programming language |
| **FastAPI** | High-performance web framework for building APIs |
| **Uvicorn** | ASGI web server implementation |
| **HTTPX** | Next-generation, fully async HTTP client |
| **Pytest** | Testing framework |
| **Docker** | Containerization and deployment |

---

## Project Structure

```bash
├── codewars/                 # Collection of Codewars algorithmic solutions
│   ├── build_a_pile_of_cubes.py
│   ├── rot13.py
│   └── ... (other solutions)
├── .dockerignore             # Docker ignore rules
├── Dockerfile                # Docker deployment configuration
├── main.py                   # Main FastAPI application & business logic
├── main01.py                 # Alternative/development entrypoint
├── requirements.txt          # Project dependencies
└── test_main.py              # Pytest test suite
```

---

## Getting Started

### Prerequisites

- **Python 3.10+** installed locally, OR
- **Docker** installed locally.

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fawaztanigbola/currency-volatility-tracker.git
   cd currency-volatility-tracker
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the Uvicorn development server:

```bash
uvicorn main:app --reload
```

The server will start running at `http://127.0.0.1:8000`. You can access the interactive Swagger API documentation at `http://127.0.0.1:8000/docs`.

### Running with Docker

1. **Build the Docker image:**
   ```bash
   docker build -t currency-volatility-tracker .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 currency-volatility-tracker
   ```

The application will be accessible at `http://localhost:8000`.

---

## API Reference

### 1. Health Check
Returns the status of the service.

* **Endpoint:** `GET /`
* **Response:**
  ```json
  {
    "check": true
  }
  ```

### 2. Get Currency Volatility
Fetches historical exchange rates against the USD for a specified currency and calculates its volatility over the analyzed timeframe.

* **Endpoint:** `GET /volatility`
* **Query Parameters:**
  * `currency` (string, optional): The 3-letter ISO currency code to analyze. Default is `EUR`. Must match pattern `^[a-zA-Z]{3}$`.
* **Example Request:**
  ```bash
  curl -X 'GET' 'http://127.0.0.1:8000/volatility?currency=EUR' -H 'accept: application/json'
  ```
* **Example Response (200 OK):**
  ```json
  {
    "Currency": "EUR",
    "total_days_analyzed": 22,
    "volatility": 0.004123
  }
  ```
* **Error Responses:**
  * `422 Unprocessable Entity`: Invalid currency code format or unsupported currency.
  * `502 Bad Gateway`: External Frankfurter API is unreachable or returned an error.

---

## Running Tests

The test suite validates both the API endpoints and the mathematical calculations inside the `CurrencyAnalyzer` class.

To run the tests, execute:

```bash
pytest -v
```

---

## Codewars Solutions

The `codewars/` directory contains clean, well-structured Python solutions to various popular Codewars challenges. These include:
- **String Manipulation**: `simple_pig_latin.py`, `camel_case.py`, `Stop_gninnipS_My_sdroW!.py`
- **Algorithms & Math**: `build_a_pile_of_cubes.py`, `two_sum.py`, `descending_order.py`
- **Data Structures**: `linked_lists.py`
- **Cryptography**: `rot13.py`

These scripts can be run individually using standard Python:
```bash
python codewars/rot13.py
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details (or feel free to use this code for educational and portfolio purposes).