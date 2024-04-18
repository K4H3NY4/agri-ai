import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv


client = Groq(
       api_key=os.environ.get("gi"),
)

st.title('Mkulima AI Assistant')

prompt = st.text_input('Enter your question here')


if prompt:  # Check if prompt is not empty
    # Generate response from the AI model
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Guide a farmer on how tgit o grow plants and suggest if it's possible to use hydroponics, region's altitude, preferred soil, and best season to plant. Suggest other plants that can thrive in that altitude. Give a summary of the yield per acre, maturity time.Recommend hydroponic experts in that area.",
        },{
            "role":"user",
            "content":prompt,
        }
    ],
    model="llama2-70b-4096",
)

    # Display the generated response
    st.write(chat_completion.choices[0].message.content)
else:
    st.write("Enjoy Mkulima AI.")



