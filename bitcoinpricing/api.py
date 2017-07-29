from decimal import Decimal

import requests
from typing import List


def get_api_price(url: str, decode: List[str], params: dict = {}) -> Decimal:
    """ Calls a generic api and returns the bitcoin price

    :param url: The API url to call
    :param decode: A list of strings which will act as dictionary keys
    :param params: A dictionary of keyword arguments passed to the request
    :return: The bitcoin price in a decimal format
    """
    response = requests.get(url=url, **params)

    js = response.json()
    for key in decode:
        js = js.get(key)

    return Decimal(js)


def get_currency_conversion(to: str, base: str) -> Decimal:
    url = f'http://api.fixer.io/latest?base={base}'
    response = requests.get(url)
    return Decimal(response.json()['rates'][to])


def get_site_prices(config: List[dict]) -> dict:
    """ Uses the loaded config file and gets the current bitcoin prices from each site

    :param config: The pre-validated config file
    :return: The dictionary of decimal price values, with the names as keys
    """
    prices = {}
    for site in config:
        prices[site['name']] = get_api_price(url=site['url'], decode=site['decode'], params=site.get('params', {}))

    return prices



if __name__ == '__main__':
    print('API test:')
    import yaml
    with open('sites.yml', 'r') as f:
        config_file = yaml.load(f)
    print(get_site_prices(config_file))
