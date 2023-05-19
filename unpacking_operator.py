'''
Using the Dictionary Unpacking Operator (**)
Suppose you have two (or more) dictionaries, and you need to iterate through them together, 
without using collections.ChainMap or itertools.chain(). 
you can use the dictionary unpacking operator (**) to merge 
the two dictionaries into a new one and then iterate through it:
'''
fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
# How to use the unpacking operator **
{**vegetable_prices, **fruit_prices}

# You can use this feature to iterate through multiple dictionaries
for k, v in {**vegetable_prices, **fruit_prices}.items():
    print(k, '->', v)
'''
It’s important to note that if the dictionaries you’re trying to 
merge have repeated or common keys, then the values of the right-most dictionary will prevail:
'''
