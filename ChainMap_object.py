from collections import ChainMap

fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
chained_dict = ChainMap(fruit_prices, vegetable_prices)
print(type(chained_dict))  # A ChainMap object
for key, value in chained_dict.items():
    print(key, '->', value)
