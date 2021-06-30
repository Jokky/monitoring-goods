from domain.Price import Price
from repository.mock.GoodRepository import GoodRepository
from repository.mock.GoodStoreRepository import GoodStoreRepository
from repository.mock.StoreRepository import StoreRepository
from service.CategoryService import CategoryService
from service.DifferentPercentGoodsPrice import DifferentPercentGoodsPrice
from service.GoodService import GoodService
from service.StoreService import StoreService


class App:
    def __init__(self):
        self.differentPercentGoodsPrice = DifferentPercentGoodsPrice()

        self.store_repository = StoreRepository()
        self.good_store_repository = GoodStoreRepository(self.store_repository)
        self.good_repository = GoodRepository(self.good_store_repository)

        self.store_service = StoreService()
        self.good_service = GoodService(self.good_repository, self.good_store_repository)
        self.category_service = CategoryService(self.store_service, self.good_service)

    def run(self):
        print("Name\tPrice")
        for cat in self.category_service.get_categories():
            for good in cat.goods:
                for good_store in good.good_stores:
                    print("{}\t{}".format(good_store.name, good_store.price.amount))

        good = self.good_service.get_good_by_id(1)
        good.good_stores[0].name = "sadasdas"
        good.good_stores[0].price = Price(30000)
        self.good_service.update_good_store(1, good.good_stores[0])