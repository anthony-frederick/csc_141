# This tells you if you will need to wait for a table based on group size

group = input("How many people are in your dinner group? ")
group = int(group)
if group > 8:
    print("\nSorry, you will have to wait for a table.")
else:
    print("\nYour table will be ready shortly.")