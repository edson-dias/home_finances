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
    def __init__(self, id: uuid4, ref: uuid4, value: float, due_date: date):
        self.id = id
        self.ref = ref
        self.value = value
        self.due_date = due_date
        self.paid = False
        self.type = BillTypes.UNIT.value

    def get_total_amount_due(self):
        if not self.paid:
            return self.value
        return 0
    
    def get_monthly_amount_due(self):
        # TODO: adicionar a validação do ano tbm, pois a atual regra está quebrada.
        if not self.paid and self.due_date.month <= date.today().month:
            return self.value
        return 0

    def is_bill_paid(self):
        if self.paid:
            return True
        return False
