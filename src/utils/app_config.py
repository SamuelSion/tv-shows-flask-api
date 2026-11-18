class AppConfig:

    # TVmaze search endpoint (the query string "q" is added by the service):
    tvmaze_search_url = "https://api.tvmaze.com/search/shows"

    # Seconds to wait for TVmaze before giving up:
    request_timeout = 10
