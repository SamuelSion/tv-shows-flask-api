# TV Shows Flask API

A small layered REST API built with **Python** and **Flask**. It receives a TV show name from the client, queries the public [TVmaze](https://www.tvmaze.com/api) search API, and returns the matching shows.

## Endpoint

| Method | Route                | Description                                   |
| ------ | -------------------- | --------------------------------------------- |
| GET    | `/api/shows/<name>`  | Returns all shows whose name contains `<name>` |

The API forwards the request to `https://api.tvmaze.com/search/shows?q=<name>` and returns TVmaze's JSON: a list of `{ "score": ..., "show": { ... } }` objects.

### Example

```
GET http://127.0.0.1:4000/api/shows/girls
```

```json
[
  {
    "score": 0.89,
    "show": {
      "id": 139,
      "name": "Girls",
      "language": "English",
      "genres": ["Drama", "Romance"],
      "premiered": "2012-04-15"
    }
  }
]
```

### Responses

| Status | When                                                      |
| ------ | --------------------------------------------------------- |
| 200    | Search succeeded (an empty list `[]` means no matches)    |
| 400    | The show name is empty or contains only whitespace        |
| 404    | Unknown route                                             |
| 500    | Unexpected error, e.g. TVmaze is unreachable              |

Error responses have the shape `{ "message": "..." }`.

## Project structure

```
src/
├── app.py                         # Server setup, blueprint registration, error handlers
├── controllers/
│   └── show_controller.py         # Route definition (Blueprint)
├── models/
│   └── show_search_model.py       # Input validation
├── services/
│   └── show_service.py            # Calls the TVmaze API with requests
└── utils/
    └── app_config.py              # Configuration (TVmaze URL, timeout)
```

The code follows a layered design: the controller only creates the model and calls `validate()`, the service talks to the external API, and the configuration lives in a single `AppConfig` class.

## Getting started

Requirements: Python 3.10+

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
flask --app src/app.py run --debug --port 4000
```

Then open `http://127.0.0.1:4000/api/shows/girls`.

## Tech stack

- Python
- Flask
- Requests
