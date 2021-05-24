emp = {
    'name': 'Anjali Bhardwaj',
    'designation':'assistent',
    'salary':
    {
        'basic': 1200,
        'dra': 10000,
        'hra': 4500,
        'misc': 890
    },
    'dept':'accounts',
    'doj':
    {
        'year':2000,
        'month': 15,
        'day': 56

    },
}

print(emp)
print(emp['name'])
print(emp['salary']['hra'])


print('another way of dict intialization')
stockprice = dict(google=235, facebook=211.98, netflix=200.9)
print(stockprice)


#add a value
print('add a value')
stockprice['disney']= 238.09
print(stockprice)

#update value
print('update value')
stockprice['facebook']=879
print(stockprice)