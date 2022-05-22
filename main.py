from dataclasses import dataclass
from typing import List
from loguru import logger
import re


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
    DICT_KEYS = {'amount' : r'amount:(\d+)\n',
                 'interest' : r'interest:(\d.\d|\d|/d/d)%',
                 'downpayment' : r'downpayment:(\d+)\n',
                 'term' : r'term:(\d+)'}
    list_values = []
    for key in DICT_KEYS.keys():
        try:
            list_values.append(float(re.findall(DICT_KEYS[key], package.replace(' ', ''))[0]))
        except:
            raise KeyError(INFO_MESSAGE_ERROR.format(key=key, package=package))

    return list_values

if __name__ == '__main__':
    input = '''amount: 100000
interest: 5.5%
downpayment: 20000
term: 30'''
    print(Credit(*read_package(input)).print_parametrs_credit())