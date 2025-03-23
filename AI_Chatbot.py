import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
import os


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Streamlit UI Layout
col1, col2 = st.columns([0.8, 0.2])  

with col1:
    st.title("Let's start the conversation")

with col2:
    if st.button(" New Chat"):
        st.session_state.chat_history = []  
        st.session_state.memory.clear()  
        st.rerun()  

if not GEMINI_API_KEY:
    st.error("Please set the GEMINI_API_KEY environment variable.")
else:
    try:
        model = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=GEMINI_API_KEY
        )

        if "memory" not in st.session_state:
            st.session_state.memory = ConversationBufferMemory()

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        for role, text in st.session_state.chat_history:
            display_name = "You" if role == "user" else "Bot" 
            with st.chat_message(role):
                st.write(f"**{display_name}:** {text}")

        user_input = st.chat_input("Enter your message...")

        if user_input:  
            try:
                
                previous_chat = "\n".join(
                    [f"{role}: {text}" for role, text in st.session_state.chat_history]
                )

                
                full_input = f"{previous_chat}\nUser: {user_input}"

                
                result = model.invoke(full_input)
                response_text = result.content

                # Store chat in one time conversation
                st.session_state.chat_history.append(("user", user_input)) 
                st.session_state.chat_history.append(("assistant", response_text))  

                # Store in LangChain memory
                st.session_state.memory.save_context({"input": user_input}, {"output": response_text})

                # Automatically clear prompt after clicking
                st.rerun()

            except Exception as e:
                st.error(f"Error during model invocation: {e}")

    except Exception as e:
        st.error(f"Error initializing the model: {e}")
