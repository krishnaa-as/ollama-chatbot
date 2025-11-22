import streamlit as st
import fitz  # PyMuPDF for reading PDFs
from llama_index.core import Document, VectorStoreIndex
from llama_index.core.settings import Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

# Streamlit UI Title
st.title("Campus Bot")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Set up LlamaIndex with Ollama
Settings.llm = Ollama(model="llama3.2:1b")
Settings.embed_model = OllamaEmbedding("all-minilm")  # Example alternative model


# Function to read a single PDF file
def read_pdf(file_path):
    """Reads text from a single PDF file."""
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text() + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

# Load and index a single document
@st.cache_resource
def load_index():
    """Loads and indexes the document."""
    try:
        pdf_path = "C:/Users/DELL/OneDrive/Desktop/chatbotorgdoc.pdf"  # Change to your file path
        pdf_text = read_pdf(pdf_path)
        
        if not pdf_text:
            return None  # Return None if the PDF couldn't be read

        doc = Document(text=pdf_text)
        return VectorStoreIndex.from_documents([doc])  # Create index from a single document

    except Exception as e:
        st.error(f"Error loading index: {e}")
        return None

index = load_index()

# Query function to get responses from the indexed document
def query_documents(query):
    """Fetches responses from indexed document."""
    if index is None:
        return "Error: Index could not be loaded."

    try:
        query_engine = index.as_query_engine()
        response = query_engine.query(query)
        return response.response
    except Exception as e:
        st.error(f"Error querying documents: {e}")
        return "Sorry, I couldn't fetch the answer."

# Chat history display
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Ask a question about the document..."):
    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = query_documents(prompt)  # Fetch response from document
        st.write(response)
        st.session_state["messages"].append({"role": "assistant", "content": response})
