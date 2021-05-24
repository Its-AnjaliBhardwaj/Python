fruits = {'apple':100, 'banana':40, 'kiwi':90, 'dragonfruit':400}
print('updating values')

new_fruits = {'guava':35, 'peach':70}
fruits.update(new_fruits)
print(fruits)


print('removing values')
fruits.pop('kiwi')
print(fruits)


print('better version')

if 'orange' in fruits:
    fruits.pop('orange')
    print(fruits)

else:
    print('orange not found')

last_item_removed = fruits.popitem()
print(fruits)
print(f'{last_item_removed} removed from fruits')

print('accessing value from dict')
print(fruits['apple'])
print(fruits['Apple'])
#this method may give u an error

print('better version of above')
print('using the get() with default value in dict')
print(fruits.get('apple'))
print(fruits.get('Apple'))
print(fruits.get('Apple', 'price not found'))


print('accessing keys , values and items')


print(fruits.values())
print(fruits.keys())
print(fruits.items())


