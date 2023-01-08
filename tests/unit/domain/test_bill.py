from datetime import date, timedelta
from src.domain.bill import UnitBill, BillTypes, Installment, InstallmentBill


def test_if_unit_bill_returns_true_if_its_already_paid():
    u = UnitBill(
        value=103.45,
        due_date=date.today()
    )
    u._paid = True
    assert u.is_bill_paid() == True


def test_if_unit_bill_returns_false_if_its_not_paid():
    u = UnitBill(
        value=103.45,
        due_date=date.today()
    )
    assert u.is_bill_paid() == False


def test_if_unit_bill_get_total_amount_due_returns_right_due_value():
    u = UnitBill(
        value=103.45,
        due_date=date.today()
    )
    assert u.get_total_amount_due() == 103.45


def test_if_unit_bill_get_total_amount_due_returns_zero_if_paid_is_true():
    u = UnitBill(
        value=103.45,
        due_date=date.today()
    )
    u._paid = True
    assert u.get_total_amount_due() == 0


def test_if_unit_bill_get_monthly_amount_due_returns_right_value_if_due_date_is_today():
    u = UnitBill(
        value=103.45,
        due_date=date.today()
    )
    assert u.get_monthly_amount_due() == 103.45


def test_if_unit_bill_get_monthly_amount_due_returns_zero_if_due_date_is_next_month():
    u = UnitBill(
        value=103.45,
        due_date=date.today() + timedelta(days=32) 
    )
    assert u.get_monthly_amount_due() == 0


def test_if_unit_bill_get_monthly_amount_due_returns_zero_if_due_date_is_last_month_and_paid_is_true():
    u = UnitBill(
        value=103.45,
        due_date=date.today() - timedelta(days=32) 
    )
    u._paid = True
    assert u.get_monthly_amount_due() == 0


def test_if_unit_bill_get_monthly_amount_due_returns_zero_if_due_date_is_next_year_and_paid_is_false():
    u = UnitBill(
        value=103.45,
        due_date=date.today() - timedelta(days=367) 
    )
    assert u.get_monthly_amount_due() == 0


def test_if_unit_bill_type_is_unit_type():
    u = UnitBill(
        value=103.45,
        due_date=date.today() - timedelta(days=367) 
    )
    assert u.type == BillTypes.UNIT


def test_if_installment_bill_get_total_amount_due_return_right_sum():
    i = InstallmentBill()
    installments = {
        Installment(10.11, date(2023, 1, 10)),
        Installment(10.11, date(2023, 2, 10)),
        Installment(10.11, date(2023, 3, 10)),
    }
    i.installments = installments
    assert i.get_total_amount_due() == 30.33


def test_if_installment_bill_get_total_amount_due_return_just_unpaid_values_sum():
    i = InstallmentBill()
    installments = {
        Installment(10.11, date(2023, 2, 10)),
        Installment(10.11, date(2023, 3, 10)),
    }
    paid_installment = Installment(10.11, date(2023, 1, 10))
    paid_installment.paid = True
    installments.add(paid_installment)
    i.installments = installments
    assert i.get_total_amount_due() == 20.22


def test_if_installment_bill_set_installment_as_paid_changes_installment_paid_status_to_true():
    i = InstallmentBill()
    installments = {
        Installment(10.11, date(2023, 1, 10), ref='7ba99d03-c3d0-426f-a928-5717233e6842'),
        Installment(10.11, date(2023, 2, 10)),
        Installment(10.11, date(2023, 3, 10)),
    }
    i.installments = installments
    i.set_installment_as_paid(ref='7ba99d03-c3d0-426f-a928-5717233e6842')
    assert i.get_total_amount_due() == 20.22