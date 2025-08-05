# 📞 Telecom Customer Service Chatbot using RAG and Dify

This project is a **Telecom-based AI Chatbot** built to simulate a customer support assistant. It uses **Retrieval-Augmented Generation (RAG)** to provide accurate responses based on company-specific data.

The chatbot is developed using **Dify**, a no/low-code platform for building production-ready LLM applications. This frontend interacts with Dify’s API to display responses in a conversational format.

---

## 🔍 Project Highlights

- 📡 Domain: **Telecom Customer Support**
- 🧠 Powered by **RAG (Retrieval-Augmented Generation)**
- 🔧 Built using **Dify** – a low-code platform to create LLM apps
- 💬 Chat interface built using **Python (Streamlit)**
- ⚡ Connects to **Dify API** to generate answers from uploaded data
- 🔐 Secured with API Key (user-provided)

---

## 🚀 How It Works

1. Domain-specific knowledge base (e.g., telecom FAQs, policy PDFs) is uploaded into Dify.
2. Dify internally uses **RAG** to extract relevant context for each query.
3. The `app.py` file sends user queries to Dify’s chat API.
4. The bot replies with accurate, real-time responses based on the context.

---

## 📦 Tech Stack

| Tool         | Purpose                         |
|--------------|----------------------------------|
| 🧠 Dify       | LLM backend & RAG knowledge base |
| 🐍 Python     | App logic                       |
| 🚀 Streamlit  | Frontend UI (chat interface)     |
| 🔗 REST API   | Communication with Dify          |

---

## 💡 Use Cases

- Simulating a **telecom customer support agent**
- Answering queries like:
  - *“How do I port my number?”*
  - *“What’s the international roaming charge?”*
  - *“How to check my data balance?”*
- Adaptable to other domains: Banking, Insurance, E-commerce, etc.

---

## 🧪 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Telecom_ChatBot.git
cd Telecom_ChatBot
