# Tells you it is making a sandwich with certain condiments

def sandwich_condiments(*condiments):
    """Prints some condiments that would be on a sandwich"""
    print(f"Making a sandwich with {condiments}")
sandwich_condiments('mayonaise')
sandwich_condiments('ketchup', 'relish')
sandwich_condiments('mustard', 'mayonaise', 'ketchup')