from Discounts import Discount


class Order:

    def __init__(self, price: float, *discounts: Discount):
        self.price = price
        self.discount = self.get_final_discount(discounts)

    def final_price(self) -> float:
        return self.price - self.price * self.discount

    @staticmethod
    def get_final_discount(discounts: tuple) -> float:
        final_discount = 0
        max_discount = 0
        for disc in iter(discounts):
            final_discount += disc.off_price
            if disc.off_price > max_discount:
                max_discount = disc.off_price

        return final_discount if final_discount <= 0.99 else max_discount
