def chatgpt(message):
    if "Hi" in message:
        return "Hello! How can I assist you today?"
    elif "bye" in message:
        return "Have a great day! Goodbye!"
    else:
        return "I don't understand. Can you please rephrase your question?"

message = input("Enter your message: ")
response = chatgpt(message)
print(response)
