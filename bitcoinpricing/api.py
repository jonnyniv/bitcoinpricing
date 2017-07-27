from decimal import Decimal

import requests


def get_coinbase_price() -> Decimal:
    url = 'https://api.coinbase.com/v2/prices/BTC-EUR/buy'
    headers = {'CB-VERSION': '2017-05-19'}
    response = requests.get(url=url, headers=headers)

    return Decimal(response.json()['data']['amount'])


def get_coinfloor_price() -> Decimal:
    url = 'https://webapi.coinfloor.co.uk:8090/bist/XBT/EUR/ticker/'
    response = requests.get(url=url)

    return Decimal(response.json()['ask'])


def get_bitstamp_price() -> Decimal:
    url = 'https://www.bitstamp.net/api/v2/ticker/btceur/'
    response = requests.get(url=url)

    return Decimal(response.json()['ask'])


def get_currency_conversion(to: str, base: str) -> Decimal:
    url = f'http://api.fixer.io/latest?base={base}'
    response = requests.get(url)
    return Decimal(response.json()['rates'][to])


if __name__ == '__main__':
    print('API test:')
    print(f'Coinbase: {get_coinbase_price()}')
    print(f'Coinfloor: {get_coinfloor_price()}')
    print(f'Bitstamp: {get_bitstamp_price()}')
