from domain.Category import Category
from domain.CategoryStore import CategoryStore
from domain.Good import Good
from domain.GoodStore import GoodStore
from domain.Price import Price
from domain.Store import Store
from service.CompareGoodsPrice import CompareGoodsPrice
from utils.ConfigService import ConfigService


class App:
    def __init__(self):
        self.compareGoodsPrice = CompareGoodsPrice()

    def run(self):
        print(ConfigService.get('PERCENT_DOWN_GOOD'))

        eldorrado = Store('Eldorado')
        mvideo = Store('MVideo')
        dns = Store('DNS')

        eldorradoIPhone = GoodStore('iphone 11 pro max 256GB', Price(90000), eldorrado)
        mvideoIPhone = GoodStore('iphone 11 pro max white 256GB', Price(81000), mvideo)

        iphone = Good([eldorradoIPhone, mvideoIPhone])

        categoryPhoneEldorado = CategoryStore(eldorrado, 'Смарфоны', [eldorradoIPhone])
        categoryPhoneMvideo = CategoryStore(mvideo, 'Смартфоны Apple', [mvideoIPhone])

        categoryPhone = Category([categoryPhoneEldorado, categoryPhoneMvideo], 'Смарфтоны', [iphone])

        print("Name\tPrice")
        for cat in categoryPhone.categoryStore:
            for good in cat.goods:
                print("{}\t{}".format(good.name, good.price.amount))

        print("Percent goods compare by price: {}".format(self.compareGoodsPrice.exec(iphone)))