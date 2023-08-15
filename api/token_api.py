from pythonProject.Repository_books.api.base_api import BaseAPI

class TokenApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.token_url = "/api-clients"

    def post_token(self, token_generation):
        return self.post(url=f"{self.token_url}", json=token_generation)
