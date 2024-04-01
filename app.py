import os
import anthropic
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Anthropics API client
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Streamlit app title
st.title('AI Assistant for Farmers')

# User input for the question
prompt = st.text_input('Enter your question here')

if prompt:  # Check if prompt is not empty
    # Generate response from the AI model
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.9,
        system="Guide a farmer on how to grow plants and suggest if it's possible to use hydroponics, region's altitude, preferred soil, and best season to plant. Suggest other plants that can thrive in that altitude. Give a summary of the yield per acre, maturity time.",
        messages=[{"role": "user", "content": prompt}]
    )

    # Display the generated response
    st.write(message.content[0].text)
else:
    st.write("Please enter your question.")
