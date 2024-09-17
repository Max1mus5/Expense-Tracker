from fastapi import HTTPException, APIRouter
from database.database import Session
from database.models import expenses as expense_model
from database.schemas import expense as expense_schema
from datetime import datetime
from typing import List
from fastapi.responses import JSONResponse

expenseController = APIRouter()

def get_expenses():
  db = Session()
  try:
    expenses = db.query(expense_model.Expense).all()
    expense_list = [expense_schema.Expense.from_orm(expense) for expense in expenses]
    return JSONResponse(content={"expenses": expense_list})
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  finally:
    db.close()