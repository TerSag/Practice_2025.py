from json import loads as jloads
from datetime import datetime
from requests import get
 
 
 
 
def timenow():  
    return datetime.today().strftime("%B %d %H:%M:%S")
 
 
def get_currency():  
    req = get("https://api.monobank.ua/bank/currency").text
    if "errorDescription" not in req:
        with open("currency.json", "w") as f:
            f.write(req)
        print(f'{timenow()}: Done')
    else:
        print(f'{timenow()}: Error')
 
 
def print_currency(): 
    with open("currency.json", "r") as f:
        cur = jloads(f.read())
    res = str('Купівля/Продаж')
    res += f'\nUSD: {cur[0]["rateBuy"]}/{cur[0]["rateSell"]}'
    res += f'\nEUR: {cur[1]["rateBuy"]}/{cur[1]["rateSell"]}'
    return res

get_currency()
print(print_currency())