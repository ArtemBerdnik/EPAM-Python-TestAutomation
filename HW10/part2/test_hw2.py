from Discounts import MorningDiscount, ElderDiscount
from Order import Order


def test_discounts():
    order_1 = Order(100, MorningDiscount())
    assert order_1.final_price() == 50

    order_2 = Order(100, ElderDiscount())
    assert order_2.final_price() == 10