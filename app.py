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
            "content": "Guide a farmer on how to farm in a smart way and making farming sustainable. Give the requirements in a table. Recommend other farming that can thrive in those conditions and where you can get certified producers from in Kenya.Based on the companies compare the prices also get the e-commerce links where farmers can buy the seeds online.Respond in simplified English relatable with the Kenyan youth context. if the plants have a problem recommend agro vets websites. ",
        },{
            "role":"user",
            "content":prompt,
        }
    ],
    model="gemma-7b-it",
    temperature=0.9,
)

    # Display the generated response
    st.write(chat_completion.choices[0].message.content)
else:
    st.write("Enjoy Mkulima AI.")



