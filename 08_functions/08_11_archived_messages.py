# This prints some messages to friends

def show_messages(messages):
    """Print the messages in the list"""
    print("Showing all messages.")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print the messages and move them to sent_messages"""
    print("\n Sending messages...")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["How is your day?", "What's up?", "Happy Friday!"]
show_messages(messages)
sent_messages = []
send_messages(messages[:], sent_messages)
print("Final lists:")
print(messages)
print(sent_messages)