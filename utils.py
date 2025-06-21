import pandas as pd
from io import StringIO
import streamlit as st

# 🔒 Limit kosztów dla sesji (USD)
COST_LIMIT = 0.05


def init_session_state():
    """Zainicjalizuj liczniki sesji, jeśli nie istnieją"""
    if "total_tokens" not in st.session_state:
        st.session_state.total_tokens = 0
        st.session_state.total_cost = 0.0
        st.session_state.chat_log = []


def update_session_stats(user_input, response, prompt_tokens, completion_tokens, total_tokens, total_cost):
    """Aktualizuj statystyki w session_state"""
    st.session_state.total_tokens += total_tokens
    st.session_state.total_cost += total_cost
    st.session_state.chat_log.append({"User": user_input, "AI": response})


def export_data(format_option):
    """Eksportuj historię rozmowy i statystyki do wybranego formatu"""
    if format_option == "TXT":
        buffer = StringIO()
        for entry in st.session_state.chat_log:
            buffer.write(f"User: {entry['User']}\n")
            buffer.write(f"AI: {entry['AI']}\n\n")
        buffer.write(
            f"---\nTokeny: {st.session_state.total_tokens}\nKoszt: ${st.session_state.total_cost:.5f}\n")
        return buffer.getvalue(), "chat_history.txt"

    elif format_option == "CSV":
        df = pd.DataFrame(st.session_state.chat_log)
        buffer = StringIO()
        df.to_csv(buffer, index=False)
        buffer.write(
            f"\nTOTAL TOKENS,{st.session_state.total_tokens}\nTOTAL COST,${st.session_state.total_cost:.5f}\n")
        return buffer.getvalue(), "chat_history.csv"


def show_cost_warning():
    """Wyświetl ostrzeżenie o przekroczeniu limitu"""
    if st.session_state.total_cost >= COST_LIMIT:
        st.warning(
            f"Przekroczono limit sesji ${COST_LIMIT:.2f}. Rozważ zakończenie rozmowy.")
