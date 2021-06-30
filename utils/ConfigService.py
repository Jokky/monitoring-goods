import os
import ast
from typing import Any, TypeVar, Type

defaultValueEnv = {
    'SYSTEM_MONITORING': 'False',
    'SYSTEM_MONITORING_DELAY': 5,
    'PERCENT_DOWN_GOOD_STORES': 80,
    'PERCENT_DOWN_GOOD': 50
}

T = TypeVar('T')


class ConfigService:
    @staticmethod
    def get(key: str) -> T:
        value = ast.literal_eval(os.environ.get(key))

        if value is not None:
            return value

        value = ast.literal_eval(defaultValueEnv[key])

        if value is None:
            raise Exception('Not found ENV key {}'.format(key))

        return value
