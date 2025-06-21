# 🤖 Chatbot AI z LangChain + OpenAI API

Prosty, ale rozbudowany chatbot wykorzystujący **LangChain**, **OpenAI GPT**, **Streamlit** oraz wiele praktycznych funkcji:

- 🔄 Resetowanie rozmowy
- 🧠 Pamięć konwersacji
- 🧮 Licznik tokenów i kosztów (z limitem)
- 💾 Eksport rozmowy do TXT lub CSV
- 🎨 Przełącznik trybu jasny/ciemny
- ✍️ Efekt "piszącego AI"

---

## 🚀 Demo

    

---

## 🛠️ Technologie

- Python 3.10+
- Streamlit
- LangChain + langchain-community
- OpenAI API
- Python-dotenv
- Pandas

---

## 📁 Struktura projektu

```
chatbot-ai/
├── app.py                 # Główna aplikacja Streamlit
├── utils.py               # Funkcje pomocnicze: eksport, statystyki, limity
├── requirements.txt       # Lista zależności
├── .env                   # Klucz API OpenAI (niewersjonowany)
├── .gitignore             # Ignorowane pliki, w tym .env
└── README.md              # Opis projektu
```

---

## 🧑‍💻 Jak uruchomić lokalnie

1. **Sklonuj repozytorium:**

   ```bash
   git clone https://github.com/twoj-login/chatbot-ai.git
   cd chatbot-ai
   ```

2. **Zainstaluj zależności:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Utwórz plik **``** i dodaj klucz OpenAI:**

   ```env
   OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```

4. **Uruchom aplikację:**

   ```bash
   streamlit run app.py
   ```

---

## 🎛️ Funkcje aplikacji

- Wybór modelu GPT:
  - `gpt-3.5-turbo` (polecany – tani)
  - `gpt-4o` (średnia cena)
  - `gpt-4` (droższy)
- Tryb ciemny/jasny
- Efekt pisania AI (animowane odpowiedzi)
- Statystyki tokenów (wejście, wyjście, łącznie)
- Limit kosztu sesji (domyślnie \$0.05)
- Eksport rozmowy do `.txt` lub `.csv`
- Reset rozmowy jednym kliknięciem

---

## 🎨 Stylizacja: tryb ciemny

Aby nadać aplikacji ciemne tło i zachować dobrą czytelność, można w `app.py` dodać:

```python
st.markdown("""
    <style>
    body {
        background-color: #0b0f19;
        color: #f0f2f6;
    }
    .stTextInput>div>div>input,
    .stTextArea>div>textarea,
    .stSelectbox>div>div {
        background-color: #1e222e;
        color: #f0f2f6;
    }
    .css-1d391kg, .css-1v0mbdj {
        background-color: #0b0f19 !important;
    }
    </style>
""", unsafe_allow_html=True)
```

---

## 📜 Licencja

MIT License — możesz korzystać, modyfikować i rozwijać swobodnie.

---

## 📫 Kontakt

Michał Kowalewski\
📧 [kowalewski.michal04@gmail.com](mailto\:kowalewski.michal04@gmail.com)\
🌐 [GitHub](https://github.com/run4theh111z-stack)

