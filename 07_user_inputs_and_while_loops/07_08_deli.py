# This prints peoples sandwich orders and tells them they're being worked on

sandwich_orders = ['turkey', 'ham', 'beef', 'chicken']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making {current_sandwich} sandwhich...")
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
    print(f"I have finished making your {sandwich} sandwhich.")
