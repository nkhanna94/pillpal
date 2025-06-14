# 💊 PillPal

PillPal is a simple, retrieval-augmented medical query assistant. It uses a local vector store (FAISS) and a language model to answer medical questions based on the content of *Current Essentials of Medicine*.

> ⚠️ **Disclaimer:** This tool is for informational and testing purposes only. It is **not** intended for clinical decision-making or patient care.

---

## 📖 Features

* 🔍 **Context-aware QA:** Retrieves relevant documents and answers based solely on available context.
* 🤖 **LLM-powered reasoning:** Utilizes Hugging Face-hosted models (like Mistral 7B) for natural, reliable responses.
* 📦 **FAISS vector store integration** for efficient similarity search.
* 🎛️ **Streamlit-based interactive chat UI**
* 🛑 **Graceful fallback:** If the system doesn't know, it responds appropriately instead of hallucinating answers.

---

## 📦 Tech Stack

* **Python** 🐍
* **FAISS** 📚
* **LangChain** 🔗
* **Hugging Face Inference API** 🤖
* **Streamlit** 🌐
* **Docker** 🐳

---

## 🚀 Getting Started

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔑 Set Up Environment Variables

Create a `.env` file in the project root:

```bash
HF_TOKEN=your_huggingface_token_here
```

---

## 🏃‍♂️ Run the App

```bash
streamlit run pillpal_bot.py
```

---

## 🐳 Run via Docker (optional)

Build and run the Docker container:

```bash
docker build -t pillpal .
docker run -p 8501:8501 --env-file .env pillpal
```

---

## 📂 Project Structure

```
pillpal/
├── data/
│   └── Current Essentials of Medicine.pdf
│
├── vectorstore/
│   └── db_faiss/
│       ├── index.faiss
│       └── index.pkl
│
├── app.py
├── create_memory.py
├── connect_memory.py
├── pillpal_bot.py
│
├── Dockerfile
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

📬 Questions, feedback, or suggestions?
Reach out at 📧 **[khanna.niharika09@gmail.com](mailto:khanna.niharika09@gmail.com)**

---
