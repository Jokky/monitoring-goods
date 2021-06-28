from domain.Good import Good
from utils.Observable import Observer


class DifferentPercentGoodsPrice(Observer[Good]):
    def __init__(self):
        pass

    def update(self, subject: Good) -> None:
        minPriceGood = subject.good_stores[0]
        maxPriceGood = minPriceGood

        for goodStore in subject.good_stores:
            if minPriceGood.price.amount > goodStore.price.amount:
                minPriceGood = goodStore

            if maxPriceGood.price.amount < goodStore.price.amount:
                maxPriceGood = goodStore

        differencePriceGoods = maxPriceGood.price.amount - minPriceGood.price.amount

        print((differencePriceGoods / minPriceGood.price.amount) * 100)