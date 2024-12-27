import streamlit as st
import time

# Define specific intents and responses for an e-commerce chatbot
intents = {
    "product_inquiry": ["tell me about", "what is", "product details", "describe", "information about"],
    "order_status": ["where is my order", "order status", "track my order", "when will my order arrive"],
    "return_refund": ["return my order", "refund request", "return policy", "how do I return"],
    "greet": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "take care", "ok"],
}

responses = {
    "product_inquiry": "Our latest phone is the 'XYZ Pro' with a 12GB RAM, 256GB storage, and a 48MP camera. It's priced at $999.",
    "order_status": "Your order #12345 is out for delivery and should arrive within 2 days.",
    "return_refund": "You can initiate a return within 30 days of receiving your order. Please visit your order page to start the return process.",
    "greet": "Hello! How can I help you today?",
    "goodbye": "Goodbye! Have a great day!",
    "fallback": "Sorry, I didn't understand that. Can you rephrase your question?",
}

# Function to match user input with the specific intents
def get_intent(user_input):
    for intent, examples in intents.items():
        if any(example in user_input.lower() for example in examples):
            return intent
    return "fallback"

# Streamed response emulator
def response_generator(intent):
    response = responses.get(intent, responses["fallback"])
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Streamlit App setup
st.title("E-commerce Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get intent and generate response
    intent = get_intent(prompt)
    response = st.write_stream(response_generator(intent))

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})