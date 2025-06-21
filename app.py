import os
import time
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.callbacks import get_openai_callback
from utils import (
    init_session_state,
    update_session_stats,
    export_data,
    show_cost_warning
)

# 🔐 Wczytaj klucz API z .env
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# ⚙️ Konfiguracja strony
st.set_page_config(page_title="Chatbot AI", page_icon="🤖")

# 🎨 Motyw: Ciemny / Jasny
theme = st.selectbox("🎨 Motyw:", ["🌑 Ciemny", "🌕 Jasny"], index=0)

dark_mode_css = """
<style>
body {
    background-color: #0e1117;
    color: #fafafa;
}
.stTextInput>div>div>input {
    background-color: #1e222a;
    color: #fafafa;
}
</style>
"""

light_mode_css = """
<style>
body {
    background-color: #ffffff;
    color: #000000;
}
.stTextInput>div>div>input {
    background-color: #f1f1f1;
    color: #000000;
}
</style>
"""

# 💅 Wstaw CSS zgodnie z wyborem
if theme.startswith("🌑"):
    st.markdown(dark_mode_css, unsafe_allow_html=True)
else:
    st.markdown(light_mode_css, unsafe_allow_html=True)

st.title("🤖 Chatbot AI z LangChain")


# 🧠 Inicjalizacja session_state
init_session_state()

# 🎛️ Wybór modelu GPT
model_options = {
    "gpt-3.5-turbo (polecany – tani)": "gpt-3.5-turbo",
    "gpt-4o (średnia cena)": "gpt-4o",
    "gpt-4 (droższy)": "gpt-4"
}
model_display_name = st.selectbox(
    "Wybierz model GPT:", list(model_options.keys()), index=0)
model_name = model_options[model_display_name]

# 🧠 Model językowy
llm = ChatOpenAI(
    openai_api_key=openai_key,
    temperature=0.7,
    model_name=model_name
)

# 💬 Pamięć konwersacji
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

# 🔄 Łańcuch konwersacyjny
conversation = ConversationChain(llm=llm, memory=st.session_state.memory)

# 🧹 Reset rozmowy
if st.button("🔄 Resetuj rozmowę"):
    st.session_state.memory.clear()
    st.session_state.chat_log = []
    st.session_state.total_tokens = 0
    st.session_state.total_cost = 0.0
    st.success("Historia rozmowy została wyczyszczona.")

# 📥 Pole tekstowe
user_input = st.text_input("Zadaj pytanie lub rozpocznij rozmowę:")

# ▶️ Obsługa odpowiedzi i statystyk
if user_input:
    with get_openai_callback() as cb:
        response = conversation.run(user_input)

        # 🧠 Wyświetlenie odpowiedzi
        st.markdown("**AI pisze...**")
        placeholder = st.empty()

        display_text = ""
        for char in response:
            display_text += char
            placeholder.markdown(f"**AI:** {display_text}")
            time.sleep(0.015)  # ~15ms na znak – możesz dopasować

        # 📊 Statystyki bieżącego zapytania
        st.markdown("---")
        st.subheader("📊 Statystyki zapytania:")
        st.markdown(f"- Tokeny wejściowe: `{cb.prompt_tokens}`")
        st.markdown(f"- Tokeny wyjściowe: `{cb.completion_tokens}`")
        st.markdown(f"- Tokeny łącznie: `{cb.total_tokens}`")
        st.markdown(f"- Koszt tego zapytania: `${cb.total_cost:.5f}`")

        # ➕ Aktualizacja sesji
        update_session_stats(
            user_input, response,
            cb.prompt_tokens,
            cb.completion_tokens,
            cb.total_tokens,
            cb.total_cost
        )

        # 🚨 Ostrzeżenie o koszcie
        show_cost_warning()

# 📜 Historia rozmowy
with st.expander("📜 Historia rozmowy"):
    st.info(st.session_state.memory.buffer)

# 📈 Statystyki całej sesji
st.markdown("---")
st.subheader("📈 Statystyki całej sesji:")
st.markdown(f"- Tokeny łącznie: `{st.session_state.total_tokens}`")
st.markdown(f"- Szacowany koszt: `${st.session_state.total_cost:.5f}`")

# 💾 Eksport rozmowy
st.markdown("---")
st.subheader("💾 Eksport rozmowy i statystyk:")
format_option = st.selectbox("Wybierz format eksportu:", ["TXT", "CSV"])

export_content, filename = export_data(format_option)
st.download_button(
    label="📤 Pobierz rozmowę",
    data=export_content,
    file_name=filename,
    mime="text/plain" if format_option == "TXT" else "text/csv"
)
