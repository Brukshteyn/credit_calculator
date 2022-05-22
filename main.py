from dataclasses import dataclass


@dataclass
class Credit:

    MONTH_IN_YEAR = 12

    amount : int
    interest : float
    downpayment : int
    term : int

    def get_monthly_payment(self):
        every_monthly_interest = self.interest / self.MONTH_IN_YEAR / 100
        return round((self.amount - self.downpayment) *
                     (every_monthly_interest * (1 + every_monthly_interest) ** (self.MONTH_IN_YEAR * self.term)) /
                     ((1 + every_monthly_interest) ** (self.MONTH_IN_YEAR * self.term) - 1) , 2)

    def get_interest_charges(self):
        return round(self.get_general_sum_payment() - self.amount + self.downpayment, 2)

    def get_general_sum_payment(self):
        return round(self.get_monthly_payment() * self.MONTH_IN_YEAR * self.term, 2)


def read_package(package : str):
    """Чтение строки и вынос параметров для реализации класса Credit."""
    pass

if __name__ == '__main__':
    pass