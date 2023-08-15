from http import HTTPStatus
import json

from pythonProject.Repository_books.api.orders_api import OrdersApi

def test_book_order(order_a_book):
    '''order a book - 1'''
    response = OrdersApi().post_order(order_a_book)
    order_dict = response.json()
    order = order_dict['created']
    assert order == True
    assert response.reason == 'Created'
    assert response.status_code == HTTPStatus.CREATED, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.Created}'

def test_check_all_orders():
    '''checks, that orders contain all necessary keys - 2'''
    response = OrdersApi().get_orders()
    orders_dict = response.json()
    for order in list(orders_dict):
        assert list(order) == ['id', 'bookId', 'customerName', 'createdBy', 'quantity', 'timestamp']
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

def test_newly_created_order_is_in_orders(order_a_book):
    '''order a book - 3'''
    response_one_order = OrdersApi().post_order(order_a_book)
    new_order_dict = response_one_order.json()
    new_order_id = new_order_dict['orderId']
    response_all_orders = OrdersApi().get_orders()
    all_orders_dict = response_all_orders.json()
    ids_list = []
    for order in all_orders_dict:
        ids_list.append(order['id'])
    assert new_order_id in ids_list
    assert response_one_order.reason == 'Created'
    assert response_one_order.status_code == HTTPStatus.CREATED, f'\nStatus code is not as expected\nActual: {response_one_order.status_code}' \
                                                       f'\nExpected: {HTTPStatus.Created}'

def test_change_customer_name(order_a_book, new_name):
    '''change customer name after order - 4'''
    response = OrdersApi().post_order(order_a_book)
    order_dict = response.json()
    order_id = order_dict['orderId']
    response = OrdersApi().patch_customer_name(order_id, new_name)
    updated_response = OrdersApi().get_one_order(order_id)
    updated_response_dict = updated_response.json()
    new_name_json = json.loads(new_name)
    assert new_name_json['customerName'] == updated_response_dict['customerName']
    assert response.reason == 'No Content'
    assert response.status_code == HTTPStatus.NO_CONTENT, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.NO_CONTENT}'

def test_delete_order(order_a_book):
    '''delete order - 5'''
    response = OrdersApi().post_order(order_a_book)
    order_dict = response.json()
    order_id = order_dict['orderId']
    response = OrdersApi().delete_order(order_id)
    assert response.reason == 'No Content'
    assert response.status_code == HTTPStatus.NO_CONTENT, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.NO_CONTENT}'