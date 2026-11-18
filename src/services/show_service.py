import requests
from models.show_search_model import ShowSearchModel
from utils.app_config import AppConfig


class ShowService:

    # Search TVmaze for shows whose name contains the given text:
    def search_shows(self, search_model: ShowSearchModel):

        # GET https://api.tvmaze.com/search/shows?q=<name>
        # Passing the name via params lets requests encode spaces and special characters:
        response = requests.get(AppConfig.tvmaze_search_url, params = { "q": search_model.name }, timeout = AppConfig.request_timeout)

        # Raise an exception for 4xx / 5xx answers from TVmaze (caught by the Catch-All):
        response.raise_for_status()

        shows = response.json()
        return shows
