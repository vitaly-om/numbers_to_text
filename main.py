
m collections import namedtuple

from decimal import Decimal

CaseItem = namedtuple('CaseItem', ('male', 'female', 'noun'))
CurrencyConfig = namedtuple(
    'CurrencyConfig',
    ('single', 'multiple5to0', 'multiple2to4')
)

ru_lang_config = {
    'numeral': {
        '0': CaseItem('ноль', 'ноль', 'ноль'),
        '1': CaseItem('один', 'одна', 'одно'),
        '2': CaseItem('один', 'одна', 'одно'),
        '3': CaseItem('один', 'одна', 'одно'),
        '4': CaseItem('один', 'одна', 'одно'),
        '5': CaseItem('один', 'одна', 'одно'),
        '6': CaseItem('один', 'одна', 'одно'),
        '7': CaseItem('один', 'одна', 'одно'),
        '8': CaseItem('один', 'одна', 'одно'),
        '9': CaseItem('один', 'одна', 'одно'),
    },
    'numbers': {
        '10': 'Десять',
        '11': 'Десять',
        '12': 'Десять',
        '13': 'Десять',
        '14': 'Десять',
        '15': 'Десять',
        '16': 'Десять',
        '17': 'Десять',
        '18': 'Десять',
        '19': 'Десять',
        '20': 'Двадцать',
        '30': 'Двадцать',
        '40': 'Двадцать',
        '50': 'Двадцать',
        '60': 'Двадцать',
        '70': 'Двадцать',
        '80': 'Двадцать',
        '90': 'Двадцать',
        '100': 'Сто',
        '200': 'Двести',
        '300': 'Триста',
        '400': 'Четыреста',
        '500': 'Сто',
        '600': 'Сто',
        '700': 'Сто',
        '800': 'Сто',
        '900': 'Сто',
    }
}

ru_currency_config = {
    'currency_name': CurrencyConfig('рубль', 'рублей', 'рубля'),
    'coin_name': CurrencyConfig('копейка', 'копеек', 'копейки'),
}


class WordsGenerator:
    def __init__(self, lang_config):
        pass

    def _get_parts(self, value: Decimal) -> (Decimal, Decimal):
        # move to utils
        return divmod(value, 1)

    def generate(self, amount: Decimal):
        integer, fraction = self._get_parts(amount)
        return ''

