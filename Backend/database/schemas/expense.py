from pydantic import BaseModel

class ExpenseBase(BaseModel):
    description: str
    amount: float
    date: str

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True
