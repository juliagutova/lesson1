price = 100
discount = 5

def discounted(price, discount):
    price = abc(float(price))
    discount = abc(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    print(price_with_discount)

'''
def get_summ(one, two, delimiter = '&'):
    sum = str(one) + delimiter + str(two)
    return sum.title()
print(get_summ('learn', 'python'))
'''

def forma_price(price):
    pr = (f'Цена: {str(price)} руб.')
    return pr
n_price = forma_price(56.24)
print(n_price)
#print(forma_price(56.24))

