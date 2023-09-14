from pydantic import BaseModel


class CurrencyConversionRequest(BaseModel):
    from_currency: str
    to_currency: str
    value: float


class CurrencyConversionResponse(BaseModel):
    result: float
