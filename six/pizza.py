pizza ={
    'crust': 'thick',
    'toppings':  ['mushrooms', 'extra cheese'],
}

print("Youo ordered a " +pizza['crust'] + "-crust pizza" + "with the following toppings:")
for toppings in pizza['toppings']:
    print("\t" +toppings)