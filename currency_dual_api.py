from fastapi import FastAPI, Query
from typing import List, Optional
from datetime import datetime
import requests

app = FastAPI() 

def get_monobank_data():
    response = requests.get("https://api.monobank.ua/bank/currency")
    if response.status_code == 200:
        return response.json()
    return []

# ISO 4217 коди: валюта => код
currency_iso = {
    "UAH": 980, "USD": 840, "EUR": 978, "GBP": 826,
    "CNY": 156, "PLN": 985, "CHF": 756, "CZK": 203,
    "BGN": 975, "CAD": 124
}

@app.get("/monobank")
def get_currency_pairs(
    base: Optional[List[str]] = Query(default=None),
    quote: Optional[List[str]] = Query(default=["UAH"])
):
    data = get_monobank_data()
    result = []

    base_codes = [currency_iso.get(b) for b in base] if base else None
    quote_codes = [currency_iso.get(q) for q in quote] if quote else None

    for entry in data:
        code_a = entry.get("currencyCodeA")
        code_b = entry.get("currencyCodeB")

        if base_codes and code_a not in base_codes:
            continue
        if quote_codes and code_b not in quote_codes:
            continue

        base_code = next((k for k, v in currency_iso.items() if v == code_a), None)
        quote_code = next((k for k, v in currency_iso.items() if v == code_b), None)

        result.append({
            "base": base_code,
            "quote": quote_code,
            "rateBuy": entry.get("rateBuy"),
            "rateSell": entry.get("rateSell"),
            "rateCross": entry.get("rateCross"),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source": "monobank"
        })

    return result

@app.get("/currency/privatbank")
def read_privatbank_currency(date: str = Query(default=datetime.today().strftime("%d.%m.%Y"))):
    url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"
    response = requests.get(url)
    data = response.json().get("exchangeRate", [])

    result = {}
    for item in data:
        currency = item.get("currency")
        if currency:
            result[currency] = {
                "buy": item.get("purchaseRate"),
                "sell": item.get("saleRate"),
                "source": "privatbank",
                "date": date
            }
    return result
