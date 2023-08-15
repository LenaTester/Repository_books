from http import HTTPStatus

from pythonProject.Repository_books.api.token_api import TokenApi

def test_token_generation(token_generation):
    '''token generation - 1'''
    response = TokenApi().post_token(token_generation)
    token_dict = response.json()
    token = token_dict['accessToken']
    assert len(token) == 64
    assert response.reason == 'Created'
    assert response.status_code == HTTPStatus.CREATED, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.Created}'