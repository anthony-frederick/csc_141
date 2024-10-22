# Shows basic greetings

def show_messages(messages):
    """Print some greetings to friends"""
    for message in messages:
        print(message)
texts = ["How is your day?", "What's up?", "Happy Friday!"]
show_messages(texts)