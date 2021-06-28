from typing import List

from domain.Category import Category
from domain.CategoryStore import CategoryStore
from service.GoodService import GoodService
from service.StoreService import StoreService


class CategoryService:
    __categories: List[Category] = []

    def __init__(self, store_service: StoreService, good_service: GoodService):
        category_stores = [
            CategoryStore(store_service.get_store_by_id(1), 'Смарфоны', [good_service.get_good_store_by_id(1, 1)]),
            CategoryStore(store_service.get_store_by_id(2), 'Смартфоны Apple', [good_service.get_good_store_by_id(1, 2)])
        ]

        self.__categories = [
            Category(1, category_stores, 'Смарфтоны', [good_service.get_good_by_id(1)])
        ]

    def get_category_by_id(self, category_id) -> Category:
        return [category for category in self.__categories if category.id == category_id][0]

    def get_categories(self):
        return self.__categories
