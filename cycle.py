from itertools import cycle
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
times = 5  # Define how many times you need to iterate through prices
total_items = times * len(prices)
for item in cycle(prices.items()):
    if not total_items:
        break
    total_items -= 1
    # print("------------")
    print(item)