from datetime import date, timedelta
from uuid import uuid4
from src.domain.bill import UnitBill


def test_if_unit_bill_returns_true_if_its_already_paid():
    u = UnitBill(
        id=uuid4(),
        ref=uuid4(),
        value=103.45,
        due_date=date.today()
    )
    u.paid = True
    assert u.is_bill_paid() == True


def test_if_unit_bill_returns_false_if_its_not_paid():
    u = UnitBill(
        id=uuid4(),
        ref=uuid4(),
        value=103.45,
        due_date=date.today()
    )
    assert u.is_bill_paid() == False


def test_if_unit_bill_get_total_amount_due_returns_right_due_value():
    u = UnitBill(
        id=uuid4(),
        ref=uuid4(),
        value=103.45,
        due_date=date.today()
    )
    assert u.get_total_amount_due() == 103.45


def test_if_unit_bill_get_total_amount_due_returns_zero_if_paid_is_true():
    u = UnitBill(
        id=uuid4(),
        ref=uuid4(),
        value=103.45,
        due_date=date.today()
    )
    u.paid = True
    assert u.get_total_amount_due() == 0


def test_if_unit_bill_get_monthly_amount_due_returns_right_value_if_due_date_is_today():
    u = UnitBill(
        id=uuid4(),
        ref=uuid4(),
        value=103.45,
        due_date=date.today()
    )
    assert u.get_monthly_amount_due() == 103.45


def test_if_unit_bill_get_monthly_amount_due_returns_zero_if_due_date_is_next_month():
    u = UnitBill(
        id=uuid4(),
        ref=uuid4(),
        value=103.45,
        due_date=date.today() + timedelta(days=32) 
    )
    assert u.get_monthly_amount_due() == 0


def test_if_unit_bill_get_monthly_amount_due_returns_zero_if_due_date_is_last_month_and_paid_is_true():
    u = UnitBill(
        id=uuid4(),
        ref=uuid4(),
        value=103.45,
        due_date=date.today() - timedelta(days=32) 
    )
    assert u.get_monthly_amount_due() == 0


# TODO: Lembrar de pesquisar as fixtures para sempre criar um UNitBill