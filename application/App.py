from domain.Category import Category
from domain.CategoryStore import CategoryStore
from domain.Good import Good
from domain.GoodStore import GoodStore
from domain.Price import Price
from domain.Store import Store
from service.DifferentPercentGoodsPrice import DifferentPercentGoodsPrice
from utils.ConfigService import ConfigService


class App:
    def __init__(self):
        pass

    def run(self):
        # print(ConfigService.get('PERCENT_DOWN_GOOD'))

        eldorrado = Store('Eldorado')
        mvideo = Store('MVideo')
        dns = Store('DNS')

        eldorradoIPhone = GoodStore('iphone 11 pro max 256GB', Price(90000), eldorrado)
        mvideoIPhone = GoodStore('iphone 11 pro max white 256GB', Price(81000), mvideo)
        dnsIPhone = GoodStore('iphone 11 pro max black 256GB', Price(79000), dns)

        differentPercentGoodsPrice = DifferentPercentGoodsPrice()

        iphone = Good([eldorradoIPhone, mvideoIPhone])
        iphone.attach(differentPercentGoodsPrice)

        categoryPhoneEldorado = CategoryStore(eldorrado, 'Смарфоны', [eldorradoIPhone])
        categoryPhoneMvideo = CategoryStore(mvideo, 'Смартфоны Apple', [mvideoIPhone])

        categoryPhone = Category([categoryPhoneEldorado, categoryPhoneMvideo], 'Смарфтоны', [iphone])

        print("Name\tPrice")
        for cat in categoryPhone.categoryStore:
            for good in cat.goods:
                print("{}\t{}".format(good.name, good.price.amount))

        iphone.update_good_store(dnsIPhone)
        # print("Percent goods compare by price: {}".format())