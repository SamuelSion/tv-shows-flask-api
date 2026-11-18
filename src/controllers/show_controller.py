from flask import Blueprint as Router
from models.show_search_model import ShowSearchModel
from services.show_service import ShowService

router = Router("show_router", __name__) # Blueprint = Router


# Search shows by name: GET /api/shows/<name>
@router.get("/api/shows/<name>")
def search_shows(name: str):
    search_model = ShowSearchModel(name)
    search_model.validate()
    service = ShowService()
    shows = service.search_shows(search_model)
    return shows # A list is converted to JSON by Flask.
