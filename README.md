# 📺 TV Shows Flask API

> A small layered REST API that searches TV shows by name.  
> Built with **Python** & **Flask**, on top of the public **TVmaze** API.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-blue)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Show search** | Returns all shows whose name contains the requested text |
| **External API** | Forwards the query to the public [TVmaze](https://www.tvmaze.com/api) search API |
| **Validation** | Empty or whitespace-only names are rejected with a clear error |
| **JSON errors** | Every error response has the shape `{ "message": "..." }` |
| **Layered design** | Controller, model, service and configuration are separated |

---

## 📡 Endpoint

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/api/shows/<name>` | Returns all shows whose name contains `<name>` |

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

| Status | When |
|--------|------|
| 200 | Search succeeded (an empty list `[]` means no matches) |
| 400 | The show name is empty or contains only whitespace |
| 404 | Unknown route |
| 500 | Unexpected error, for example TVmaze is unreachable |

---

## 🏗️ Architecture

```
src/
├── app.py                       # Server setup, blueprint registration, error handlers
├── controllers/
│   └── show_controller.py       # Route definition (Blueprint)
├── models/
│   └── show_search_model.py     # Input validation
├── services/
│   └── show_service.py          # Calls the TVmaze API with requests
└── utils/
    └── app_config.py            # Configuration (TVmaze URL, timeout)
```

**Layered design** — the controller only creates the model and calls `validate()`, the service talks to the external API, and the configuration lives in a single `AppConfig` class.

---

## 🔧 Technical Highlights

- **Flask Blueprints** — routes are registered as a blueprint
- **Validation in the model** — the controller never decides whether input is valid
- **Centralized error handling** — JSON error handlers for 404 and unexpected errors
- **Single configuration class** — the TVmaze URL and timeout are defined in `AppConfig`
- **Request timeout** — outgoing calls to TVmaze use a configured timeout

---

## 🚀 Getting Started

Requires **Python 3.10+**.

```bash
# Clone
git clone https://github.com/SamuelSion/tv-shows-flask-api.git
cd tv-shows-flask-api

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
flask --app src/app.py run --debug --port 4000
```

Then open http://127.0.0.1:4000/api/shows/girls

---

## 👤 Author

**Samuel Sion** — [github.com/SamuelSion](https://github.com/SamuelSion)
