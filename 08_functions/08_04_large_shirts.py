#  Gives different size shirts and different messages

def make_shirt(size= 'large', text= 'I love python'):
    """A shirt with some text on it."""
    print(f"The shirt is {size} and says {text}.")
make_shirt()
make_shirt(size= 'medium')
make_shirt(size= 'small', text= 'I like java' )