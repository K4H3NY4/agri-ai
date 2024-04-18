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
            "content": "Guide a farmer on how to grow plants and smart ways on farming making farming sustainable. Give the requirements of the plants requirements in a table for example, Altitude, Soil Preferences, Best seasons to plant. Recommend other plants that can thrive in those conditions and where you can get certified seed from in Kenya.Based on the seed companies compare the seed prices also get the e-commerce links where farmers can buy the seeds online.Respond in simplified English relatable with the Kenyan youth context. ",
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



