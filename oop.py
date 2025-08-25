class Chat:
    def __init__(self):
        self.chatee = input("Who are you cattin with? \n")
        self.last_message = input("What was your message \n")
        self.last_message_time = input("When was the last message sent \n")

    def __str__(self):
        return f"You are chatting with {self.chatee}"

    def open(self):
        return f"You just opened the chat with {self.chatee} with last message {self.last_message} that was sent at {self.last_message_time}"