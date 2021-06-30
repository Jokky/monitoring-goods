import os
from typing import Any, TypeVar, Type

defaultValueEnv = {
    'PERCENT_DOWN_GOOD_STORES': 80,
    'PERCENT_DOWN_GOOD': 50
}

T = TypeVar('T')


class ConfigService:
    @staticmethod
    def get(key: str, return_type: Type[T] = str) -> T:
        value = return_type(os.environ.get(key))

        if value is not None:
            return value

        value = return_type(defaultValueEnv[key])

        if value is None:
            raise Exception('Not found ENV key {}'.format(key))

        return value
