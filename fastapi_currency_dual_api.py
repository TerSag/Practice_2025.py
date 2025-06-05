from fastapi import FastAPI
from json import loads as jloads
from datetime import datetime
from requests import get

app = FastAPI()

def timenow():
    return datetime.today().strftime("%Y-%m-%d %H:%M:%S")

def get_currency():
    req = get("https://api.monobank.ua/bank/currency").text
    if "errorDescription" not in req:
        with open("currency.json", "w") as f:
            f.write(req)
        return True
    return False

def print_currency():
    with open("currency.json", "r") as f:
        cur = jloads(f.read())
    return {
        "USD": {"buy": cur[0]["rateBuy"], "sell": cur[0]["rateSell"]},
        "EUR": {"buy": cur[1]["rateBuy"], "sell": cur[1]["rateSell"]}
    }

@app.get("/currency/monobank")
def read_monobank_currency():
    get_currency()
    return print_currency()

@app.get("/currency/privatbank")
def read_privatbank_currency():
    response = get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
    data = response.json()
    return {item["ccy"]: {"buy": item["buy"], "sell": item["sale"]} for item in data if item["ccy"] in ["USD", "EUR"]}
