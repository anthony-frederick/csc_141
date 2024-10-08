ticket_price = input("Please enter your age: ")
ticket_price = int(ticket_price)
if ticket_price <= 3:
    print("Your ticket is free.")
elif ticket_price <= 12:
    print("Your ticket costs $10")
else:
    print("Your ticket costs $15")