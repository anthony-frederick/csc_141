

ticket_price = input("Please enter your age: ")
ticket_price += "Enter quit to stop the program"
ticket_price = int(ticket_price)
while True:
    if ticket_price <= 3:
        print("Your ticket is free.")
    elif ticket_price == quit:
        break
    elif ticket_price <= 12:
        print("Your ticket costs $10")
    else:
        print("Your ticket costs $15")