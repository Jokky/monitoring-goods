import os
import threading
import psutil

from domain.Price import Price
from repository.mock.GoodRepository import GoodRepository
from repository.mock.GoodStoreRepository import GoodStoreRepository
from repository.mock.StoreRepository import StoreRepository
from service.CategoryService import CategoryService
from observer.DifferentPercentGoodsPrice import DifferentPercentGoodsPrice
from service.GoodService import GoodService
from service.StoreService import StoreService
from utils.ConfigService import ConfigService


class App:
    TIMOUT = 1

    def __init__(self):
        self.differentPercentGoodsPrice = DifferentPercentGoodsPrice()

        self.store_repository = StoreRepository()
        self.good_store_repository = GoodStoreRepository(self.store_repository)
        self.good_repository = GoodRepository(self.good_store_repository)

        self.store_service = StoreService()
        self.good_service = GoodService(self.good_repository, self.good_store_repository)
        self.category_service = CategoryService(self.store_service, self.good_service)

        self.TIMEOUT = ConfigService.get('SYSTEM_MONITORING_DELAY')

        if ConfigService.get('SYSTEM_MONITORING'):
            self.show_stat()

    def show_stat(self):
        os.system('clear')
        print(f'CPU: {psutil.cpu_percent()}\tRAM: {psutil.virtual_memory().percent}')
        threading.Timer(self.TIMEOUT, self.show_stat).start()

    def run(self):
        print("Name\tPrice")
        for cat in self.category_service.get_categories():
            for good in cat.goods:
                for good_store in good.good_stores:
                    print(f'{good_store.name}\t{good_store.price.amount}')

        good = self.good_service.get_good_by_id(1)
        # good.good_stores[0].name = "sadasdas"
        # good.good_stores[0].price = Price(30000)
        # self.good_service.update_good_store(1, good.good_stores[0])

        for i in range(0, 10000):
            good.good_stores[0].price = Price(good.good_stores[0].price.amount - i)
            self.good_service.update_good_store(1, good.good_stores[0])
