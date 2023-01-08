from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime, date
from enum import Enum
from typing import Protocol
from uuid import uuid4
from src.domain.budget import Budget
from src.domain.user import User


class BillTypes(Enum):
    UNIT = 'unit'
    FIXED = 'fixed'
    INSTALLMENT = 'installment'


class AbstractBill(Protocol):
    type: BillTypes

    @abstractmethod
    def is_bill_paid(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_total_amount_due(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_monthly_amount_due(self):
        raise NotImplementedError
    


@dataclass
class Bill:
    id: uuid4
    ref: uuid4
    bill: AbstractBill
    user: User
    budget: Budget
    description: str
    created_at: datetime


class UnitBill:
    def __init__(self, value: float, due_date: date, id: uuid4 = None, ref: uuid4 = None):
        self.id = id
        self.ref = ref
        self.value = value
        self.due_date = due_date
        self._paid = False
        self.type = BillTypes.UNIT

    @property
    def paid(self):
        return self._paid
    
    @paid.setter
    def paid(self, paid):
        self._paid = paid
    
    def get_total_amount_due(self) -> float:
        if not self._paid:
            return self.value
        return 0
    
    def get_monthly_amount_due(self) -> float:
        if not self._paid and self.due_date.month == date.today().month and self.due_date.year == date.today().year:
            return self.value
        return 0

    def is_bill_paid(self) -> bool:
        return self.paid


class InstallmentBill:
    def __init__(self, id: uuid4 = None, ref: uuid4 = None) -> None:
        self.id = id
        self.ref = ref
        self._paid = False
        self.type = BillTypes.INSTALLMENT
        self.installments = set()

    def get_total_amount_due(self) -> float:
        unpaid_values = [i.value for i in self.installments if not i.paid]
        return sum(unpaid_values)
    
    def get_monthly_amount_due(self) -> float:
        ...
    
    def is_bill_paid(self) -> bool:
        ...
    
    def set_installment_as_paid(self, ref: uuid4):
        installment = next(i for i in self.installments if i.ref == ref)
        if not installment.paid:
            installment.paid = True


class Installment:
    def __init__(self, value: float, due_date: date, id: uuid4 = None, ref: uuid4 = None):
        self.id = id
        self.ref = ref
        self._paid = False
        self.due_date = due_date
        self.value = value

    @property
    def paid(self):
        return self._paid
    
    @paid.setter
    def paid(self, paid):
        self._paid = paid