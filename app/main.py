from app import db
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.services import get_conversion_history, create_conversion_history, get_exchange_rate

app = FastAPI()

db.init_db()


@app.get("/api/rates")
async def convert_currency(from_currency: str, to_currency: str, value: float, db: Session = Depends(db.get_db)):
    rate = get_exchange_rate(from_currency, to_currency)
    converted_value = value * rate
    converted_value = round(converted_value, 2)

    create_conversion_history(
        db,
        from_currency=from_currency,
        to_currency=to_currency,
        value=value,
        result=converted_value
    )

    return {"result": converted_value}


@app.get("/api/history")
async def get_conversion(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    history = get_conversion_history(db, skip=skip, limit=limit)
    return history



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)