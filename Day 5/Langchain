import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import Runnable

# -------------------------------
# Set Gemini API Key via LangChain
# -------------------------------
GOOGLE_API_KEY = "AIzaSyCHg89y9oxyvXe4vjyUSSTG1ZtlXdqmeLY"  # 🔒 Replace with your actual Gemini API key

# ✅ Load Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=GOOGLE_API_KEY
)

# -------------------------------
# Define Prompt for Translation
# -------------------------------
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are a helpful translator that translates English to French."
)
human_prompt = HumanMessagePromptTemplate.from_template(
    "Translate this to French: {input}"
)
prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

# Create the chain: prompt | llm
chain: Runnable = prompt | llm

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="English to French Translator", page_icon="🌍")
st.title("🌍 English to French Translator")

st.write("Enter an English sentence below and click **Translate**:")

# Input text box
english_input = st.text_input("Enter your English sentence:")

# Button to trigger translation
if st.button("Translate") and english_input:
    with st.spinner("Translating..."):
        result = chain.invoke({"input": english_input})
        st.subheader("🇫🇷 Translated French:")
        st.write(result.content)

