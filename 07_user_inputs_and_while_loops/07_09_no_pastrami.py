sandwich_orders = ['turkey', 'pastrami', 'ham', 'pastrami', 'beef', 'pastrami', 'chicken']
finished_sandwiches = []
print("Sorry, we are all out of pastrami for today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making {current_sandwich} sandwhich...")
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
    print(f"I have finished making your {sandwich} sandwhich.")