class Currency:
    RUB = 'rub'
    USD = 'usd'


class Price:
    def __init__(self, amount: int):
        self.amount = amount
        self.currency = Currency.RUB
