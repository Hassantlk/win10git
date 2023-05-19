'''
filter()
filter() is another built-in function that you can use to iterate 
through a dictionary in Python and filter out some of its items. 
This function is defined as filter(function, iterable) and 
returns an iterator from those elements of iterable for which function returns True.

Suppose you want to know the products with a price lower than 0.40. 
You need to define a function to determine if the price satisfies that condition 
and pass it as first argument to filter(). The second argument can be prices.keys():
'''


prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def has_low_price(price):
    return prices[price] < 0.4

low_price = list(filter(has_low_price, prices.keys()))
print(low_price)


'''
Here, you iterated through the keys of prices with filter(). 
Then filter() applies has_low_price() to every key of prices. 
Finally, you need to use list() to generate the list of products with a low price, 
because filter() returns an iterator, and you really need a list object.
'''