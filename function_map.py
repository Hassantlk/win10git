'''
map()
Python’s map() is defined as map(function, iterable, ...) and 
returns an iterator that applies function to every item of iterable, 
yielding the results on demand. So, map() could be viewed as an iteration tool 
that you can use to iterate through a dictionary in Python.

Suppose you have a dictionary containing the prices of a bunch of products, 
and you need to apply a discount to them. In this case, you can define a function that 
manages the discount and then uses it as the first argument to map(). 
The second argument can be prices.items():
'''
prices = {'apple': 10.00, 'orange': 20.00, 'banana': 30.00}
def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))

new_prices = dict(map(discount, prices.items()))
print(new_prices)

'''
Here, map() iterated through the items of the dictionary (prices.items()) to apply 
a 5% discount to each fruit by using discount(). 
In this case, you need to use dict() to generate the new_prices dictionary 
from the iterator returned by map().

Note that discount() returns a tuple of the form (key, value), 
where current_price[0] represents the key and round(current_price[1] * 0.95, 2) 
represents the new value.
'''
