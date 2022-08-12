from fastapi import FastAPI
import main as design

app = FastAPI()

@app.post('/credit')
def create_credit(credit : design.Credit):
    """������ ������� �� ������� ���������� ����������."""
    return {'every_monthly_payment' : credit.get_monthly_payment(),
            'charges' : credit.get_interest_charges(),
            'general' : credit.get_general_sum_payment()}

@app.post('/credit_from_str')
def create_credit_from_str(credit_str : str):
    """������ ������� �� ������� ������."""
    credit_str = credit_str.replace('\\n', "\n")
    return create_credit(design.Credit(*design.read_package(credit_str)))

@app.post('/set_levinshteyn')
def set_levinshteyn(ust : int):
    """��������� ��������� ��� �������� ������� ������."""
    design.LEVENSHTEIN_UP = ust
    return {'LEVENSHTEIN_UP' : ust}
