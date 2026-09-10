# Currency Volatility Tracker

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-enabled-blue?style=flat&logo=docker)](https://www.docker.com/)
[![Tests](https://img.shields.io/badge/tests-pytest-green.svg)](https://docs.pytest.org/)

An asynchronous, lightweight FastAPI microservice designed to fetch historical exchange rates and calculate the statistical volatility (standard deviation) of various currencies against the US Dollar (USD). 

This repository also serves a dual purpose, hosting a curated collection of clean, well-tested Python solutions for algorithmic challenges in the `codewars/` directory.

---

## Table of Contents

- [Overview & Architecture](#overview--architecture)
- [Mathematical Methodology](#mathematical-methodology)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Local Installation](#local-installation)
  - [Running the Application](#running-the-application)
- [API Reference](#api-reference)
- [Running with Docker](#running-with-docker)
- [Running Tests](#running-tests)
- [Codewars Solutions](#codewars-solutions)
- [License](#license)

---

## Overview & Architecture

The **Currency Volatility Tracker** acts as an analytical proxy layer over the free [Frankfurter Exchange Rate API](https://www.frankfurter.app/). When a user requests the volatility of a specific currency, the service:
1. Asynchronously queries the external Frankfurter API for historical exchange rates over a specific time series (defaulting to the `2026-04-28..2026-05-28` timeframe).
2. Parses the JSON response into in-memory structured data points.
3. Computes statistical metrics (mean, variance, standard deviation) on the data series.
4. Returns a clean, structured JSON payload representing the calculated volatility.

```
┌─────────┐                ┌───────────┐                 ┌─────────────────┐
│  User   │ ─────────────> │  FastAPI  │ ──────────────> │ Frankfurter API │
│ Client  │ <───────────── │ Service   │ <────────────── │  (Ext. Rates)   │
└─────────┘  HTTP Response └───────────┘  Async HTTP Req └─────────────────┘
                                 │
                        ┌────────▼────────┐
                        │CurrencyAnalyzer │
                        │  (StdDev/Var)   │
                        └─────────────────┘
```

### Key Features
- **Asynchronous I/O**: Leverages `FastAPI` and `httpx` to handle network requests concurrently without blocking the main execution thread.
- **On-the-Fly Analytics**: Utilizes a highly optimized Python-based `CurrencyAnalyzer` to compute metrics without reliance on heavy external math libraries.
- **Input Validation**: Employs Python's standard `typing.Annotated` along with FastAPI query validation to enforce strict ISO 4217 currency code constraints (3-character alphabetic strings).
- **Error Resiliency**: Gracefully intercepts network issues (returning a `502 Bad Gateway` if the upstream API is down) and missing currency records (returning `422 Unprocessable Entity` if the target currency is invalid or missing).

---

## Mathematical Methodology

The application measures currency volatility through **Standard Deviation ($\sigma$)**, which quantifies the amount of variation or dispersion of a set of exchange rates.

### 1. Mean Exchange Rate ($\mu$)
$$\mu = \frac{1}{N} \sum_{i=1}^{N} x_i$$
Where $x_i$ is the currency rate on day $i$, and $N$ is the total number of days analyzed.

### 2. Variance ($\sigma^2$)
$$\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2$$

### 3. Volatility / Standard Deviation ($\sigma$)
$$\sigma = \sqrt{\sigma^2}$$

These formulas are natively implemented within the `CurrencyAnalyzer` class inside `main.py` to ensure fast, lightweight computations.

---

## Tech Stack

| Technology | Role | Description |
| :--- | :--- | :--- |
| **Python 3.10+** | Language | High-level runtime for main application logic and scripting. |
| **FastAPI 0.111.0** | Framework | Modern, high-performance web framework for building APIs with auto-generated OpenAPI docs. |
| **Uvicorn 0.30.1** | Server | Lightning-fast ASGI server implementation for run-time serving. |
| **HTTPX 0.27.0** | HTTP Client | Next-generation, asynchronous HTTP client to perform non-blocking requests to upstream services. |
| **Pytest 8.2.1** | Testing | Full-suite testing framework for evaluating route validation and analyzer mathematical correctness. |
| **Docker** | Containerization | Builds production-ready, standardized containers isolated from host dependencies. |

---

## Project Structure

```bash
├── codewars/                 # Collection of Codewars algorithmic solutions
│   ├── build_a_pile_of_cubes.py
│   ├── calculating_with_functions.py
│   ├── camel_case.py
│   ├── ...
│   └── who_likes_it.py
├── .dockerignore             # Docker build ignores (venv, git, etc.)
├── Dockerfile                # Configures optimized container environments
├── main.py                   # Main FastAPI application & core analytical models
├── main01.py                 # Alternative reference entrypoint
├── requirements.txt          # Python packaging dependencies
└── test_main.py              # Suite of unit and integration tests
```

---

## Getting Started

### Prerequisites
- **Python 3.10+** installed locally, OR
- **Docker** Engine (Desktop or CLI) installed.

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fawaztanigbola/currency-volatility-tracker.git
   cd currency-volatility-tracker
   ```

2. **Create and activate a isolated virtual environment:**
   ```bash
   # On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

   # On Windows:
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install application dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the ASGI local web server:
   ```bash
   uvicorn main:app --reload
   ```
2. The server will launch successfully at `http://127.0.0.1:8000`.
3. Open your browser and navigate to:
   - **Interactive API Documentation (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **Alternative Interactive Docs (ReDoc)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Reference

### 1. Health Check
Ensures that the service is running and ready to accept connections.

- **Endpoint:** `GET /`
- **Headers:** `Accept: application/json`
- **Response (200 OK):**
  ```json
  {
    "check": true
  }
  ```

### 2. Get Currency Volatility
Calculates standard deviation of historical exchange rates against the USD over the analyzed time frame.

- **Endpoint:** `GET /volatility`
- **Query Parameters:**
  
| Parameter | Type | Required | Default | Constraint / Description |
| :--- | :--- | :--- | :--- | :--- |
| `currency` | `string` | No | `EUR` | Must be an alphabetic 3-character ISO code (e.g., `GBP`, `CAD`, `JPY`). Pattern: `^[a-zA-Z]{3}$` |

- **Example Request (using `curl`):**
  ```bash
  curl -X 'GET' 'http://127.0.0.1:8000/volatility?currency=EUR' -H 'accept: application/json'
  ```

- **Example Response (200 OK):**
  ```json
  {
    "Currency": "EUR",
    "total_days_analyzed": 22,
    "volatility": 0.004123
  }
  ```

- **Error Responses:**
  - **422 Unprocessable Entity**: The requested currency is invalid, unsupported by the upstream, or fails the pattern validation.
    ```json
    {
      "detail": "Currency code 'INVALID' is invalid or unavailable."
    }
    ```
  - **502 Bad Gateway**: The upstream Frankfurter API failed to return data or was unreachable.
    ```json
    {
      "detail": "Failed to fetch external currency data"
    }
    ```

---

## Running with Docker

You can easily build and run this application inside a standardized Docker container, bypassing any host-level dependency mismatch.

1. **Build the Docker container image:**
   ```bash
   docker build -t currency-volatility-tracker .
   ```

2. **Spin up the container forwarding host port 8000:**
   ```bash
   docker run -d -p 8000:8000 --name volatility-tracker-service currency-volatility-tracker
   ```

3. **Verify the container is running:**
   ```bash
   docker ps
   ```
   You can now query `http://localhost:8000/volatility?currency=EUR` exactly as if it were running natively on your workstation.

---

## Running Tests

Unit and integration tests are managed using `pytest` to ensure structural code integrity and mathematical precision of calculation functions.

To run the full suite, execute:

```bash
# Run pytest with standard output
pytest

# Run pytest with high verbosity and print metrics
pytest -v -s
```

---

## Codewars Solutions

The `codewars/` directory houses clean, fully functional Python solutions to popular platform challenges. They showcase solid algorithmic thinking, modular logic, and strict adhering to Clean Code guidelines.

### Categorized Solution List
- **String Parsing & Formatting**:
  - `simple_pig_latin.py`
  - `camel_case.py`
  - `Stop_gninnipS_My_sdroW!.py`
  - `extract_domain_name.py`
- **Mathematical & Algorithmic Computations**:
  - `build_a_pile_of_cubes.py`
  - `two_sum.py`
  - `descending_order.py`
  - `calculating_with_functions.py`
- **Data Structures / Custom Logic**:
  - `linked_lists.py`
  - `count_the_smiley_face.py`
- **Cryptography & Security**:
  - `rot13.py`
  - `not_very_secure.py`

Any single Codewars solution can be tested locally using raw python commands:
```bash
python codewars/rot13.py
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file (if present) or feel free to utilize code configurations for educational, evaluation, and portfolio purposes.