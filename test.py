# -*- coding: utf-8 -*-
import main as test
import re
import io
from contextlib import redirect_stdout

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

file_path = 'main.py'

try:
    with open(file_path, encoding='utf-8') as f:
        user_code = f.read()

    with io.StringIO() as buf, redirect_stdout(buf):
        exec(user_code)
        output = buf.getvalue()
except Exception as e:
    print(e)

def test_input_and_output() -> AssertionError:
    test.read_package(input_correct)
    list_text_name = ['Ваш ежемесячный платеж', 'Переплата по кредиту', 'Общая сумма к выплате']
    list_value_standart = [454.23, 83522.8, 163522.8]
    for text, standart_value in zip(list_text_name, list_value_standart):
        correct_calculated_value(text, standart_value, output)
    try:
        test.read_package(input_correct_error)
    except:
        raise AssertionError('Нет обработки некорректного ввода входных данных')

def correct_calculated_value(text : str, standart_parametr : float, output : str) -> AssertionError:
    tmp_value = re.findall(r'{text}:(.+?)руб'.format(text = text), output)
    assert len(tmp_value) > 0, 'Пожалуйста используйте фразу для выхода - {text}: ЧИСЛО руб.;'.format(text = text)
    parametr = float(tmp_value[0].replace(' ', ''))
    assert abs(parametr / standart_parametr - 1) < 0.01, 'Неправильный расчёт: {text}'.format(text = text)


if __name__ == '__main__':
    test_input_and_output()