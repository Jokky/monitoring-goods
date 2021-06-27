import os

defaultValueEnv = {
    'PERCENT_DOWN_GOOD_STORES': 80,
    'PERCENT_DOWN_GOOD': 50
}


class ConfigService:
    @staticmethod
    def get(key):
        value = os.environ.get(key)

        if value is not None:
            return value

        value = defaultValueEnv[key]

        if value is None:
            raise Exception('Not found ENV key {}'.format(key))

        return value
