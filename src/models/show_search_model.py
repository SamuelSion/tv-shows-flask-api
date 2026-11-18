from werkzeug.exceptions import BadRequest


class ShowSearchModel:

    def __init__(self, name: str):
        self.name = name

    # Validate the search text, raise BadRequest if it is invalid:
    def validate(self):
        if not self.name or not self.name.strip():
            raise BadRequest("show name must not be empty.")
        self.name = self.name.strip()
