# Consent Guardian 🛡️

Consent Guardian is an AI-powered web application designed to help users better understand and manage consent documents, terms of service, and privacy policies. It leverages GPT-powered summarization and contextual chat to explain complex legal or medical language in plain, user-friendly terms. The app also provides history tracking and customizable user preferences for personalized consent management.

---

## 🚀 Features

 Interactive Chat 💬
  Engage in a conversation with the AI to clarify confusing terms, ask questions, and get instant explanations about consent documents.

 Summarization 📑
  Upload or paste lengthy agreements and receive clear, concise summaries.

 User Preferences ⚙️
  Save personalized settings to tailor AI responses to your style of understanding.

 History Tracking 📜
  View and manage your past queries and consent summaries in a structured dashboard.

 AI-Powered 🤖
  Uses GPT-5 reasoning to adapt explanations to context and user history.

---

## 🛠️ Tech Stack

 Backend: Flask (Python) + MySQL
 Frontend: HTML, CSS, JavaScript (vanilla)
 AI Integration: GPT Service Layer
 Session Management: Flask sessions for interactive conversations
 Deployment: Docker / Local environment support

---

## 📂 Project Structure

```
clearchoice-consent/
│── app.py                # Main entrypoint
│── app/
│   ├── __init__.py       # App factory
│   ├── db.py             # Database connection
│   ├── services/
│   │   └── gpt_service.py # GPT integration logic
│   ├── routes/
│   │   ├── chat.py       # Chat endpoints
│   │   ├── summarize.py  # Summarization endpoints
│   │   ├── preferences.py# User preferences endpoints
│   │   └── history.py    # History endpoints
│   └── templates/        # HTML templates
│       ├── base.html
│       ├── index.html
│       ├── chat.html
│       ├── summarize.html
│       ├── preferences.html
│       └── history.html
│   └── static/css/
│       └── app.css       # Styling
│── .env                  # Environment variables
│── requirements.txt      # Python dependencies
│── README.md             # Documentation
```

---

## ⚡ Installation & Running

1. Clone Repository

   ```bash
   git clone https://github.com/yourusername/clearchoice-consent.git
   cd clearchoice-consent
   ```

2. Create Virtual Environment & Install Dependencies

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set Up Environment Variables (`.env` file)

   ```env
   SECRET_KEY=your-secret-key
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=yourpassword
   MYSQL_DATABASE=id_card
   ```

4. Run the App

   ```bash
   flask run
   ```

5. Open in browser → `http://127.0.0.1:5000/`

---

## 📊 Database Schema

`user_preferences`

 user\_id (PK)
 preference\_key
 preference\_value

`user_history`

 id (PK)
 user\_id (FK)
 action
 model
 tokens\_used
 success (bool)
 timestamp

---

## 🌍 Use Cases

 Healthcare: Simplify medical consent forms for patients.
 Finance: Clarify complex banking terms and agreements.
 Education: Explain student data privacy and e-learning consent.
 General Web Users: Understand Terms of Service & Privacy Policies.

---

## 🤝 Contributing


---

## 📜 License

isiahw © 2025 Consent Guardian Team
