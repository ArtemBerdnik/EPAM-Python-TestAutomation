class StockCompany:

    def __init__(self, name: str, price: float, url: str, pe: float,
                 possible_profit: float, code: str, yearly_rate: float):
        self.name = name
        self.price = price
        self.url = url
        self.pe = pe
        self.possible_profit = possible_profit
        self.code = code
        self.yearly_rate = yearly_rate
