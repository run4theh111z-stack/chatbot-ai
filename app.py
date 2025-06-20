<<<<<<< HEAD
import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# 🔐 Wczytaj zmienne środowiskowe z pliku .env
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# 🧠 Inicjalizacja modelu językowego (GPT)
llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_key)

# 💬 Pamięć konwersacji
memory = ConversationBufferMemory()

# 🔄 Łańcuch konwersacyjny z pamięcią
conversation = ConversationChain(llm=llm, memory=memory)

# 🎨 Interfejs Streamlit
st.set_page_config(page_title="Chatbot AI", page_icon="🤖")
st.title("🤖 Chatbot AI z LangChain")

# 📥 Wprowadzenie użytkownika
user_input = st.text_input("Zadaj pytanie lub rozpocznij rozmowę:")

# ▶️ Obsługa zapytania
if user_input:
    response = conversation.run(user_input)
    st.markdown(f"**AI:** {response}")

# 🧾 Historia konwersacji
with st.expander("📜 Historia rozmowy"):
    st.info(memory.buffer)
=======
import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# 🔐 Wczytaj zmienne środowiskowe z pliku .env
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# 🧠 Inicjalizacja modelu językowego (GPT)
llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_key)

# 💬 Pamięć konwersacji
memory = ConversationBufferMemory()

# 🔄 Łańcuch konwersacyjny z pamięcią
conversation = ConversationChain(llm=llm, memory=memory)

# 🎨 Interfejs Streamlit
st.set_page_config(page_title="Chatbot AI", page_icon="🤖")
st.title("🤖 Chatbot AI z LangChain")

# 📥 Wprowadzenie użytkownika
user_input = st.text_input("Zadaj pytanie lub rozpocznij rozmowę:")

# ▶️ Obsługa zapytania
if user_input:
    response = conversation.run(user_input)
    st.markdown(f"**AI:** {response}")

# 🧾 Historia konwersacji
with st.expander("📜 Historia rozmowy"):
    st.info(memory.buffer)
>>>>>>> 71b3832c9bc03893458f4e76c3f6b181676c0026
