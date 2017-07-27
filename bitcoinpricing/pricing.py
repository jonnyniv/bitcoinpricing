from decimal import Decimal, getcontext

from bitcoinpricing import api

getcontext().prec = 7


def get_coinbase_buying_cost(buying_cost: Decimal, quantity: Decimal, fixed_costs: Decimal) -> Decimal:
    """

    :param buying_cost:
    :param quantity:
    :param fixed_costs:
    :return:
    """
    total_costs = quantity + fixed_costs
    bitcoin_gained = quantity / buying_cost
    final_buying_cost = total_costs / bitcoin_gained
    return final_buying_cost


if __name__ == '__main__':
    print('Pricing tests')
    coinbase_price = api.get_coinbase_price()
    print(f'Coinbase for different amounts (Base cost = {coinbase_price}):')
    for i in (10 ** a for a in range(4)):
        print(f'Quantity: {i} = {get_coinbase_buying_cost(coinbase_price, i, Decimal(4.00*1.08))} BTC/EUR')
