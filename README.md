# Currency Volatility Tracker

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-enabled-blue?style=flat&logo=docker)](https://www.docker.com/)
[![Tests](https://img.shields.io/badge/tests-pytest-green.svg)](https://docs.pytest.org/)

An asynchronous, lightweight FastAPI microservice designed to fetch historical exchange rates and calculate the statistical volatility (standard deviation) of various world currencies against the US Dollar (USD). 

This repository also serves as an educational monorepo, housing a collection of optimized Python solutions for various algorithmic challenges in the `codewars/` directory.

---

## Table of Contents

- [Project Purpose & Overview](#project-purpose--overview)
- [How Volatility is Calculated](#how-volatility-is-calculated)
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

## Project Purpose & Overview

The **Currency Volatility Tracker** is engineered to assess financial risk and stability metrics for foreign currencies relative to the USD. 

The service integrates directly with the free and open [Frankfurter API](https://www.frankfurter.app/) (utilizing the public `.dev` instance) to pull historical daily exchange rates over a predefined time-window. By processing this dataset asynchronously, the microservice computes mathematical variance and standard deviation on the fly, outputting a precise volatility score.

### Operational Flow

```
   ┌─────────────┐             ┌─────────────┐             ┌─────────────────────┐
   │             │             │             │             │                     │
   │   Client    │ ──(Request)─►   FastAPI   │ ──(Request)─►  Frankfurter API    │
   │             │ ◄──(JSON)───│   Service   │ ◄──(Rates)──│ (Historical Rates)  │
   └─────────────┘             └──────┬──────┘             └─────────────────────┘
                                      │
                         [ Parses & Loads Datapoints ]
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │     CurrencyAnalyzer      │
                        │ ───────────────────────── │
                        │  1. Compute Mean          │
                        │  2. Compute Variance      │
                        │  3. Compute Volatility    │
                        └───────────────────────────┘
```

---

## How Volatility is Calculated

The volatility score represents the **Population Standard Deviation ($\sigma$)** of the exchange rates over the analyzed period.

1. **Mean ($\mu$):**
   $$\mu = \frac{1}{N} \sum_{i=1}^{N} x_i$$
   *Where $x_i$ is the exchange rate for day $i$, and $N$ is the total number of days analyzed.*

2. **Variance ($\sigma^2$):**
   $$\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2$$

3. **Volatility / Standard Deviation ($\sigma$):**
   $$\sigma = \sqrt{\sigma^2}$$

This calculation is implemented natively in Python within the custom `CurrencyAnalyzer` class inside `main.py` without requiring external mathematical heavy-lifters (like `numpy` or `pandas`), keeping the app lightweight and lightning-fast.

---

## Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python 3.10+** | Base programming language |
| **FastAPI** | High-performance, async web framework for building APIs |
| **Uvicorn** | High-speed, ASGI web server implementation |
| **HTTPX** | Next-generation, fully asynchronous HTTP client |
| **Pytest** | Testing framework for unit and integration validation |
| **Docker** | Containerization environment |

---

## Project Structure

```bash
├── codewars/                           # Algorithmic code challenges and solutions
│   ├── build_a_pile_of_cubes.py
│   ├── calculating_with_functions.py
│   ├── camel_case.py
│   ├── can_you_get_the_loop.py
│   ├── count_the_smiley_face.py
│   ├── descending_order.py
│   ├── extract_domain_name.py
│   ├── linked_lists.py
│   ├── not_very_secure.py
│   ├── pete_the_baker.py
│   ├── printer_errors.py
│   ├── rot13.py
│   ├── simple_pig_latin.py
│   ├── Stop_gninnipS_My_sdroW!.py
│   ├── top_3_words.py
│   ├── two_sum.py
│   └── who_likes_it.py
├── .dockerignore                       # Exclusions for Docker builds
├── Dockerfile                          # Build instructions for container engine
├── main.py                             # Main FastAPI app & CurrencyAnalyzer business logic
├── main01.py                           # Alternative/development playground scratchpad
├── requirements.txt                    # Project package dependencies
└── test_main.py                        # Automated API and unit test suite
```

---

## Getting Started

### Prerequisites

- **Python 3.10** or higher installed on your machine.
- **Docker** (Optional, for containerized deployments).

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fawaztanigbola/currency-volatility-tracker.git
   cd currency-volatility-tracker
   ```

2. **Set up a Python Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Running the Application

Launch the ASGI server using Uvicorn:

```bash
uvicorn main:app --reload
```

- **API Endpoint:** `http://127.0.0.1:8000`
- **Interactive Swagger Docs:** `http://127.0.0.1:8000/docs`
- **Alternative ReDoc UI:** `http://127.0.0.1:8000/redoc`

### Running with Docker

You can package and run the application in a fully isolated container:

1. **Build the Docker Image:**
   ```bash
   docker build -t currency-volatility-tracker .
   ```

2. **Run the Container:**
   ```bash
   docker run -d -p 8000:8000 --name currency-tracker-app currency-volatility-tracker
   ```

The service will now be accessible at `http://localhost:8000`.

---

## API Reference

### 1. Health Check

Verifies that the microservice is active and healthy.

- **Endpoint:** `GET /`
- **Headers:** None required
- **Curl Example:**
  ```bash
  curl -s http://127.0.0.1:8000/
  ```
- **Response (200 OK):**
  ```json
  {
    "check": true
  }
  ```

### 2. Get Currency Volatility

Calculates standard deviation of exchange rates against USD over a designated historical time frame.

- **Endpoint:** `GET /volatility`
- **Query Parameters:**
  - `currency` *(string, optional)*: Case-insensitive, 3-letter ISO 4217 code of the target currency. Default is `EUR`. Must conform to the pattern `^[a-zA-Z]{3}$`.
- **Curl Example:**
  ```bash
  curl -s "http://127.0.0.1:8000/volatility?currency=GBP"
  ```
- **Response (200 OK):**
  ```json
  {
    "Currency": "GBP",
    "total_days_analyzed": 22,
    "volatility": 0.003924
  }
  ```

#### Error Handling Responses:

* **422 Unprocessable Entity** (Invalid format / Unsupported currency):
  ```json
  {
    "detail": "Currency code 'XYZ' is invalid or unavailable."
  }
  ```
* **502 Bad Gateway** (Frankfurter API connection failure):
  ```json
  {
    "detail": "Failed to fetch external currency data"
  }
  ```

---

## Running Tests

Automated unit and integration tests are managed using `pytest`. The test suite validates the endpoints, request sanitization rules, and the mathematical correctness of the `CurrencyAnalyzer`'s calculations.

To run the test suite:

```bash
pytest -v --tb=short
```

---

## Codewars Solutions

The `codewars/` directory hosts clean, optimized, and thoroughly thought-out solutions to popular programming exercises on the Codewars platform.

### Quick Breakdown of Solutions

| Domain | Solution Files |
| :--- | :--- |
| **Data Structures** | `linked_lists.py` |
| **Algorithms / Arithmetic** | `build_a_pile_of_cubes.py`, `two_sum.py`, `descending_order.py`, `pete_the_baker.py` |
| **String Manipulation** | `simple_pig_latin.py`, `camel_case.py`, `Stop_gninnipS_My_sdroW!.py`, `top_3_words.py` |
| **Security & RegEx** | `not_very_secure.py`, `extract_domain_name.py`, `count_the_smiley_face.py` |
| **Cryptography** | `rot13.py` |

You can test any individual solution directly via standard Python:
```bash
python codewars/rot13.py
```

---

## License

This project is licensed under the MIT License. Feel free to use and adapt this code for educational, personal, or corporate projects.