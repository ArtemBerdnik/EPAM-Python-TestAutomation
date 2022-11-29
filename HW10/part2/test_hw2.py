from Discounts import MorningDiscount, ElderDiscount, StudentDiscount
from Order import Order


def test_discounts():
    order_1 = Order(100, MorningDiscount())
    assert order_1.final_price() == 50

    order_2 = Order(100, ElderDiscount())
    assert order_2.final_price() == 10


def test_mixes_discounts():
    order_1 = Order(100, MorningDiscount(), ElderDiscount())
    assert order_1.final_price() == 10

    order_2 = Order(100, MorningDiscount(), StudentDiscount())
    assert order_2.final_price() == 20