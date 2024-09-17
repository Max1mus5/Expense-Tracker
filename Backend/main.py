from fastapi import FastAPI
from router.expense import expenseController
from database.database import engine, Base
from database.models import Base
from fastapi.middleware.cors import CORSMiddleware  

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
  "http://localhost:3000",
  "https://mastervault.vercel.app",
  "https://mastervault-aaozxopju-max1mus5.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"],
)

#creaacion de la BD:
Base.metadata.create_all(bind=engine)


@app.get("/status")
async def health_check():
    return {"status": "API running"}

# Registrar routers
app.include_router(expenses.router)
