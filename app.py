from transformers import pipeline

# Initialize the chatbot (using text-generation instead of conversational)
chatbot = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

# First user message
user_input = "What are some fun activities I can do in the winter?"
response = chatbot(user_input, max_length=100, do_sample=True)
print("Bot:", response[0]['generated_text'])

# Follow-up question
user_input = "What else do you recommend?"
response = chatbot(user_input, max_length=100, do_sample=True)
print("Bot:", response[0]['generated_text'])