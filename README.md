# ollama-chatbot


# Campus Bot

A Streamlit-based chatbot that can answer questions from a PDF document using LlamaIndex and Ollama.

## Objectives
- Develop an AI chatbot that employs LLM to efficiently handle campus front desk enquiries.  
- Reduce the time and effort required for administrative staff and visitors to have their questions answered.  
- Enhance the user experience through polite, conversational, and user-friendly chatbot interactions.  
- Implement a one-time automated solution that can simplify the process, reduce workload, and increase overall productivity since the majority of front desk enquiries are frequently asked questions.


## Features
- Upload or use a PDF document.
- Ask questions in natural language.
- Chat interface using Stremlit provides persistent conversation history.
- Powered by Ollama LLM and embeddings via LlamaIndex.

## Installation & Setup
1. Clone the repository
    ```bash
    git clone https://github.com/krishnaa-as/ollama-chatbot.git
    cd ollama-chatbot
    
2. Install Python dependencies
    pip install -r requirements.txt

3.Install Ollama
4.Pull the Llama model 
        ollama pull llama3.2:1b
    Make sure Ollama is running locally for the chatbot to work.

5.Run the App
    Start the Streamlit app with:
       streamlit run chatbot.py
    Streamlit will launch a local web interface.
    Open the URL displayed in the terminal (usually http://localhost:8501) to start chatting. 

 ## How it Works
- PDF Reading: PyMuPDF extracts text from PDFs.  
- Indexing: LlamaIndex converts text into a searchable document index.  
- Querying: Ollama embeddings understand queries; LLM generates answers.  
- Chat Interface: Streamlit displays messages and keeps session chat history.

## Customization
- Dynamic PDF Upload: Replace the fixed PDF path with `st.file_uploader` in `chatbot.py`.  
- Change Models: Update `Settings.llm` or `Settings.embed_model` to use different LLMs or embeddings.
