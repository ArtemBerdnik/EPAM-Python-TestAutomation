
class Discount:
    def __init__(self, off_price: float):
        self.off_price = off_price


class MorningDiscount(Discount):
    def __init__(self):
        super().__init__(0.5)


class StudentDiscount(Discount):
    def __init__(self):
        super().__init__(0.3)


class ElderDiscount(Discount):
    def __init__(self):
        super().__init__(0.9)
