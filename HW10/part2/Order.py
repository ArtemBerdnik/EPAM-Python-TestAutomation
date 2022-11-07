from Discounts import Discount


class Order:

    def __init__(self, price: float, discount: Discount):
        self.price = price
        self.discount = discount

    def final_price(self) -> float:
        return self.price - self.price * self.discount.off_price
