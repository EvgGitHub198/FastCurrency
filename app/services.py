import requests
from sqlalchemy.orm import Session
from app.config import EXCHANGE_RATE_API_URL
from app.models import ConversionHistory


def get_exchange_rate(from_currency, to_currency):
    response = requests.get(EXCHANGE_RATE_API_URL)
    data = response.json()
    rates = data.get("rates", {})

    if from_currency in rates and to_currency in rates:
        return rates[to_currency] / rates[from_currency]
    else:
        raise ValueError("Invalid currency codes")


def create_conversion_history(db: Session, from_currency: str, to_currency: str, value: float, result: float):
    db_conversion = ConversionHistory(from_currency=from_currency, to_currency=to_currency, value=value, result=result)
    db.add(db_conversion)
    db.commit()
    db.refresh(db_conversion)


def get_conversion_history(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ConversionHistory).offset(skip).limit(limit).all()