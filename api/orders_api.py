from pythonProject.Repository_books.api.base_api import BaseAPI

class OrdersApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.orders_url = "/orders"
        self.headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer 6790b28030606d0b378296b392ba9792fed7b12642343f7b877203a6969921ab'}

    def post_order(self, order_a_book):
        return self.post(url=f"{self.orders_url}", json=order_a_book, headers=self.headers)

    def get_orders(self):
        return self.get(url=f"{self.orders_url}", headers=self.headers)

    def get_one_order(self, order_id):
        return self.get(url=f"{self.orders_url}/{order_id}", headers=self.headers)

    def patch_customer_name(self, order_id, new_name):
        return self.patch(url=f"{self.orders_url}/{order_id}", json=new_name, headers=self.headers)

    def delete_order(self, order_id):
        return self.delete(url=f"{self.orders_url}/{order_id}", headers=self.headers)