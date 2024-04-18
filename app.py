import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
       api_key=os.environ.get('API_KEY')
)

st.title('Mkulima AI Assistant')

prompt = st.text_input('Enter your question here')


if prompt:  # Check if prompt is not empty
    # Generate response from the AI model
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Guide a farmer on how to grow plants and suggest if it's possible to use hydroponics, Kenya's region's altitude, preferred soil, and best season to plant. Suggest other plants that can thrive in that altitude. Give a summary of the yield per acre, maturity time. Recommend hydroponic experts in that area. display information in a table format, images can be included. The name of the chatbot is Mkulima AI. Respond in a Kenyan context and englsh language they would relate to.Keep the english simple and easy to understand for a 18 year old.",
        },{
            "role":"user",
            "content":prompt,
        }
    ],
    model="mixtral-8x7b-32768",
)

    # Display the generated response
    st.write(chat_completion.choices[0].message.content)
else:
    st.write("Enjoy Mkulima AI.")



