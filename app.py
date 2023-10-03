name = 'Kamal Baiyewu'
print(f'Hello {name} ')

def number(**num):
    add = num['num1'] + num['num2'] + num['num3']
    print(add)


number(num1 = 1, num2 = 3, num3 = 4)

def anything(food = 'beans'):
    print(f'I love {food}')

anything()
anything('plantain')
anything('rice')