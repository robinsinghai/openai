from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

# Create client
client = OpenAI()

# Define conversation with roles
messages = [
    {"role": "system", "content": "You are a helpful Python tutor."},
    {"role": "user", "content": "Explain what a generator is in Python."}
]

# Send request to model
response = client.chat.completions.create(
    model="gpt-4o-mini",  # or gpt-4.1, gpt-4o, etc.
    messages=messages
)

# Print assistant's reply
print(response.choices[0].message.content)



# included a past assistant reply to maintain context.
# The model now knows the conversation history and will continue correcting grammar.
messages = [
    {"role": "system", "content": "You are a strict grammar corrector."},
    {"role": "user", "content": "i has a apple"},
    {"role": "assistant", "content": "You should say: 'I have an apple.'"},
    {"role": "user", "content": "what about 'she go to school yesterday'?"}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print(response.choices[0].message.content)
