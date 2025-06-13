# 💊 PillPal

PillPal is a simple, retrieval-augmented medical query assistant. It uses a local vector store (FAISS) and a language model to answer medical questions based on the content of *Current Essentials of Medicine*.

> ⚠️ Disclaimer: This tool is for informational and testing purposes only. It is not intended for clinical decision-making or patient care.

---

## 📖 Features

- 🔍 **Context-aware QA:** Retrieves relevant documents and answers based only on available context.
- 🤖 **LLM-powered reasoning:** Uses Hugging Face hosted models (like Mistral 7B) for natural, reliable responses.
- 📦 **FAISS vector store integration** for efficient similarity search.
- 🎛️ Streamlit-based interactive chat UI.
- 🛑 Avoids hallucination: if it doesn't know, it tells you — gracefully.

---

## 📦 Tech Stack

- Python 🐍  
- FAISS 📚  
- LangChain 🔗  
- Hugging Face Inference API 🤖  
- Streamlit (for UI) 🌐  

---

## 🚀 Getting Started

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
````

### 🔑 Set Up Environment Variables

Create a `.env` file with your Hugging Face token:

```
HF_TOKEN=your_huggingface_token_here
```

---

## 🏃‍♂️ Run the App

```bash
streamlit run app.py
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
├── requirements.txt
├── README.md
└── .gitignore
```

---


📬 Questions, feedback, or suggestions? Feel free to reach out at khanna.niharika09@gmail.com
