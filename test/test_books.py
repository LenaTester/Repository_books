from http import HTTPStatus

from pythonProject.Repository_books.api.books_api import BooksApi

def test_get_status():
    '''checks, that status is ok - 1'''
    response = BooksApi().get_status()
    book_dict = response.json()
    assert book_dict == {"status": "OK"}
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

def test_check_books():
    '''checks, that books contain all necessary keys - 2'''
    response = BooksApi().get_books()
    book_dict = response.json()
    for book in list(book_dict):
        assert list(book) == ['id', 'name', 'type', 'available']
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

def test_check_first_book():
    '''checks keys and values of first book - 3'''
    response = BooksApi().get_books()
    book_dict = response.json()
    assert book_dict[0] == {'id': 1, 'name': 'The Russian', 'type': 'fiction', 'available': True}
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'



