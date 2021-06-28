class Currency:
    RUB = 'rub'
    USD = 'usd'


class Price:
    def __init__(self, amount: int, currency: Currency = Currency.RUB):
        self.amount = amount
        self.currency = currency
