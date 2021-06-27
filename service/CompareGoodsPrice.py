from domain.Good import Good

import os


class CompareGoodsPrice:
    def __init__(self):
        pass

    def exec(self, good: Good) -> float:
        minPriceGood = next(good.goodStore.__iter__())
        maxPriceGood = minPriceGood

        for goodStore in good.goodStore:
            if minPriceGood.price.amount > goodStore.price.amount:
                minPriceGood = goodStore

            if maxPriceGood.price.amount < goodStore.price.amount:
                maxPriceGood = goodStore

        differencePriceGoods = maxPriceGood.price.amount - minPriceGood.price.amount

        return (differencePriceGoods / minPriceGood.price.amount) * 100
