#cThis lets you choose toppings to be added to you pizza

toppings = "\nEnter a topping to be added to your pizza:"
toppings += "\nEnter quit if you are done choosing: "
while True:
    topping = input(toppings)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza.")