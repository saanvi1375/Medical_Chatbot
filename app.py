import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import os
import google.generativeai as ggi

# Set up environment variables and authenticate
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/deekshithrp/Desktop/DEEKSHITH/Sem-4/Genai/saand/saanvi/Authentication.json"
load_dotenv(".env")

fetcheed_api_key = os.getenv("API_KEY")
ggi.configure(api_key=fetcheed_api_key)

# Initialize the model
model = ggi.GenerativeModel("gemini-pro")
chat = model.start_chat()
chat.send_message("Answer only if question related to medical field is asked else reply with 'Not applicable' strictly")

def LLM_Response(question):
    response = chat.send_message(question, stream=True)
    return response


st.markdown(
    """
    <style>
    .centered-title {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .centered-subtitle {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-size: 1.2em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered title and subtitle
st.markdown("<h1 class='centered-title'>🩺Smart AI medical bot👩‍⚕️</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='centered-subtitle'>Chat with our specialized AI bot</h3><hr>", unsafe_allow_html=True)

def chat_ui():

    # Load images using PIL
    user_image = Image.open("/home/deekshithrp/Desktop/DEEKSHITH/Sem-4/Genai/saand/saanvi/images/user.png")
    bot_image = Image.open("/home/deekshithrp/Desktop/DEEKSHITH/Sem-4/Genai/saand/saanvi/images/bot2.png")

    col1, col2 = st.columns([1, 5])
    with col1:
        # Display the user image
        st.image(user_image, width=50, caption='User')
    with col2:
        user_input = st.text_input("Ask any questions related to medicine:", "", key="user_input")

    if user_input:
        with st.spinner('Fetching response...'):
            try:
                response = LLM_Response(user_input)
                
                col1, col2 = st.columns([1, 5])
                with col1:
                    # Display the bot image
                    st.image(bot_image, width=50, caption='Bot')
                with col2:
                    # Display the response
                    st.markdown(f"<div class='chat-message bot-message'>**Response:**\n\n{''.join([word.text for word in response])}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f'Error getting response: {e}')

# Call the chat UI function to render the interface
chat_ui()
