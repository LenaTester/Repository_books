from pythonProject.Repository_books.api.base_api import BaseAPI

class BooksApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.status_url = '/status'
        self.books_url = '/books'

    def get_status(self, headers=None):
        return self.get(url=f"{self.status_url}")

    def get_books(self, headers=None):
        return self.get(url=f"{self.books_url}")
