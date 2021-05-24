contacts = {'help':100}
print('your temp contact book')
while True :
    print('$'*20)
    name = input('=> enter contact name:')
    if name:
        if name in contacts:
            print('=> contact found')
            print(f'=> {name} : {contacts[name]}')
        else:
            print('=> contact not found')
            print('=> contact ')
            