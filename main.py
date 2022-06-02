from dataclasses import dataclass
from typing import List
from loguru import logger
import re
import os

logger.add(os.path.expanduser(__file__), level="DEBUG")


class Levenshtein:
    """Вычисление различия строк методом Левенштейна."""

    def __init__(self, str_one : str, srt_two : str) -> None:
        self.str_one = str_one
        self.str_two = srt_two
        self.distance = self.calculate_distance(len(str_one) - 1, len(srt_two) - 1)

    def calculate_distance(self, i : int, j : int) -> None:
        if i == 0 or j == 0:
            return max(i, j)
        elif self.str_one[i] == self.str_two[j]:
            return self.calculate_distance(i - 1, j - 1)
        return 1 + min(
            self.calculate_distance(i, j - 1),
            self.calculate_distance(i - 1, j),
            self.calculate_distance(i - 1, j - 1))

    def get_distance(self) -> int:
        return self.distance

@dataclass
class Credit:

    MONTH_IN_YEAR = 12
    INFO_MESSAGE = """Ваш ежемесячный платеж: {every_monthly_payment} руб.;
Переплата по кредиту: {charges} руб.;,
Общая сумма к выплате: {general} руб."""

    amount : int
    interest : float
    downpayment : int
    term : int

    def get_monthly_payment(self) -> float:
        every_monthly_interest = self.interest / self.MONTH_IN_YEAR / 100
        return round((self.amount - self.downpayment) *
                     (every_monthly_interest * (1 + every_monthly_interest) ** (self.MONTH_IN_YEAR * self.term)) /
                     ((1 + every_monthly_interest) ** (self.MONTH_IN_YEAR * self.term) - 1) , 2)

    def get_interest_charges(self) -> float:
        return round(self.get_general_sum_payment() - self.amount + self.downpayment, 2)

    def get_general_sum_payment(self) -> float:
        return round(self.get_monthly_payment() * self.MONTH_IN_YEAR * self.term, 2)

    def print_parametrs_credit(self) -> str:
        return self.INFO_MESSAGE.format(every_monthly_payment = self.get_monthly_payment(),
                                        charges = self.get_interest_charges(),
                                        general = self.get_general_sum_payment())

@logger.catch
def read_package(package : str) -> List:
    """Чтение строки и вынос параметров для реализации класса Credit."""
    INFO_MESSAGE_ERROR = 'Ошибка в {key}, пришло {package}'
    KEY_ERROR = 'Нет переноса на новую строку'
    DICT_KEYS = {'amount' : r'{key}:(\d+)',
                 'interest' : r'{key}:(\d.\d|\d|/d/d)%',
                 'downpayment' : r'{key}:(\d+)',
                 'term' : r'{key}:(\d+)'}
    LEVENSHTEIN_UP = 2
    list_values = []
    disspace_package_list = package.replace(' ', '').split('\n')
    if len(disspace_package_list) != 4:
        raise KeyError(INFO_MESSAGE_ERROR.format(key=KEY_ERROR, package=package))
    for key_input, key in zip(disspace_package_list, DICT_KEYS.keys()):
        try:
            if Levenshtein(key_input.split(':')[0], key).get_distance() > LEVENSHTEIN_UP:
                raise KeyError(INFO_MESSAGE_ERROR.format(key=key, package=package))
            list_values.append(float(re.findall(DICT_KEYS[key].format(key=key_input.split(':')[0]), key_input)[0]))
        except:
            raise KeyError(INFO_MESSAGE_ERROR.format(key=key, package=package))

    return list_values

if __name__ == '__main__':
    input = '''amount: 100000
interest: 5.5%
downpayment: 20000
term: 30'''
    print(Credit(*read_package(input)).print_parametrs_credit())