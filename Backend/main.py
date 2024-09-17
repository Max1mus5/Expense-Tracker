from fastapi import FastAPI
from .routers import expenses
from .db.database import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/status")
async def health_check():
    return {"status": "API running"}

# Registrar routers
app.include_router(expenses.router)
