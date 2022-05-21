from dataclasses import dataclass


@dataclass
class Credit:
    amount : int
    interest : float
    downpayment : int
    term : int

    def get_monthly_payment(self):
        pass

    def get_interest_charges(self):
        pass

    def general_sum_payment(self):
        pass


def read_package():
    """Чтение строки и вынос параметров для реализации класса Credit."""
    pass

if __name__ == '__main__':
    pass
