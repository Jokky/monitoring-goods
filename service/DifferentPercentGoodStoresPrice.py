from domain.GoodStore import GoodStore
from utils.ConfigService import ConfigService
from utils.Observable import Observer


class DifferentPercentGoodStoresPrice(Observer[GoodStore]):
    def __init__(self):
        pass

    async def update(self, subject: GoodStore) -> None:
        actualPrice = subject.price
        prevPrice = subject.prices[1]

        percentPrice = (prevPrice.amount / actualPrice.amount) * 100

        if ConfigService.get('PERCENT_DOWN_GOOD_STORES', int) < percentPrice:
            print(f'{subject.name} has been changed by {percentPrice}%')
