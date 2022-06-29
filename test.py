import main as test
import re

input_standart_amount = 100000
input_standart_interest = 5.5
input_standart_downpayment = 20000
input_standart_term = 30

input_correct = '''amount: {amount}
interest: {interest}%
downpayment: {downpayment}
term: {term}'''.format(amount = 
input_standart_amount, interest = input_standart_interest, downpayment = input_standart_downpayment, term = input_standart_term)

input_correct_error = '''amuont: 100000
interest: 5.5%
downpayment: 20000
term: 30'''


def test_input_and_output() -> AssertionError:
    test.read_package(input_correct)
    output = ''
    list_text_name = ['��� ����������� ������', '��������� �� �������', '����� ����� � �������']
    list_value_standart = [1, 2, 3]
    for text, standart_value in zip(list_text_name, list_value_standart):
        correct_calculated_value(self, text, standart_value, output)
    try:
        test.read_package(input_correct, input_correct_error)
    except:
        raise AssertionError('��� ��������� ������������� ����� ������� ������')

def correct_calculated_value(self, text : str, standart_parametr : float, output : str) -> AssertionError:
    tmp_value = re.findall(r'{text}:(.+?)���.;'.format(text = text), output)
    assert len(tmp_value, output)) < 1, '���������� ����������� ����� ��� ������ - {text}: ����� ���.;'.format(text = text)
    parametr = float(tmp_value[0].replace(' ', ''))
    assert abs(parametr / standart_parametr - 1) < 0.01, '������������ ������: {text}'.format(text = text)


if __name__ == '__main__':
    test_input_and_output()