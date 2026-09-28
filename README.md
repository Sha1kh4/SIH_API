# SIH API

A lightweight Flask API that scrapes the official SIH 2026 PS table and exposes it through a simple query endpoint by PS number.

## Project Overview

This application:

- fetches the SIH table data from the public government website
- parses the HTML table with BeautifulSoup
- stores the data in memory
- refreshes it automatically every 15 minutes
- serves a REST endpoint for lookup by `ps_number`

## Files

- `app.py` — Flask application and API routes
- `scraper.py` — scraping logic for the SIH data table
- `req.txt` — Python dependencies

## Requirements

- Python 3.9+
- pip

## Setup

1. Clone or open the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r req.txt
```

## Run the API

Start the server:

```bash
python app.py
```

The app will run in debug mode by default on:

```text
http://127.0.0.1:5000
```

## API Usage

### Root endpoint

```http
GET /
```

Returns a usage message explaining the API format.

### Fetch data by PS number

```http
GET /api/data?ps_number=SIH1524
```

Example response:

```json
[
  {
    "PS Number": "SIH1524",
    "Project Title": "Example Project",
    "Department": "Example Department"
  }
]
```

If no match is found:

```json
{
  "error": "No data found for the provided PS Number"
}
```

If the query parameter is missing:

```json
{
  "error": "PS Number is required"
}
```

## Notes

- The app updates its cached data every 15 minutes.
- The scraper disables SSL certificate verification because the source site may present certificate issues during scraping.
- The source website may change its table structure over time, which could affect parsing.

## Example with curl

```bash
curl "http://127.0.0.1:5000/api/data?ps_number=SIH1524"
```

## License

This project is provided as-is for local development and educational use.
