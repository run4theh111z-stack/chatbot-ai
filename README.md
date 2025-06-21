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

![Demo działania chatbota](demo.gif)

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

3. **Utwórz plik ****\`\`**** i dodaj klucz OpenAI:**

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

---

## 📜 Licencja

MIT License — możesz korzystać, modyfikować i rozwijać swobodnie.
