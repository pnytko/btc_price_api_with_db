import requests 
import time 
import db_gen
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db_gen.engine)
session = Session()

def add_price(coin, currency, price):
    p = db_gen.Prices(coin, currency, price)
    session.add(p)
    session.commit()


while True:

    res = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD').json()
    print(res['data']['base'], res['data']['currency'], res['data']['amount'])
    add_price(res['data']['base'], res['data']['currency'], res['data']['amount'])


session.close()