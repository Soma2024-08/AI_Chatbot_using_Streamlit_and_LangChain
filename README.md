**AI Chatbot using Streamlit & LangChain**

**Description**:

This project is an AI-powered chatbot built using Streamlit, LangChain, and Google Gemini API. It provides a user-friendly chat interface with memory handling to retain conversation context.

**Features**:

1. Conversational AI using Google Gemini API

2. Chat history retention with LangChain's ConversationBufferMemory

3. User-friendly interface built with Streamlit

4. State management for storing chat history

5. Secure API handling using environment variables

**Technologies Used**:

Python

Streamlit

LangChain

Google Gemini API

dotenv (for environment variable management)

**Create and activate a virtual environment**:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

**Install dependencies**:

pip install -r requirements.txt

**Set up environment variables**:

1. Create a .env file in the project root.
2. Add your Google Gemini API key: GEMINI_API_KEY=your_api_key_here

**Run the chatbot**:
streamlit run <your file name >.py
