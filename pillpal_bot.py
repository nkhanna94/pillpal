import os
import streamlit as st

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

st.set_page_config(
    page_title="PillPal Dashboard",
    page_icon="💊"
)

DB_FAISS_PATH="vectorstore/db_faiss"
@st.cache_resource
def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)

def set_custom_prompt(template_text):
    return PromptTemplate(template=template_text, input_variables=["context", "question"])

def load_llm(repo_id, hf_token):
    return HuggingFaceEndpoint(
        repo_id=repo_id,
        temperature=0.5,
        huggingfacehub_api_token=hf_token,
        model_kwargs={"max_length": 512}
    )

def main():
    st.title("💊 PillPal — Because Not Every Headache Means Cancer")
    
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    avatars = {
        "user": "🙋",
        "assistant": "⚛️"
    }

    for msg in st.session_state.messages:
        st.chat_message(msg['role'], avatar=avatars.get(msg['role'], "💬")).markdown(msg['content'])


    user_prompt = st.chat_input("Hey, what's on your mind? 💭")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        CUSTOM_PROMPT_TEMPLATE = """
        Use only the information provided in the context to answer the user's question.
        If the answer isn’t available, reply:
        *"I wish I had that answer, but it’s not in my notes."*

        Give a concise, comprehensive answer in gpt style but be friendly and professional.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"
        HF_TOKEN = os.getenv("HF_TOKEN")

        try:
            vectorstore = get_vectorstore()

            qa_chain = RetrievalQA.from_chain_type(
                llm=load_llm(repo_id=HUGGINGFACE_REPO_ID, hf_token=HF_TOKEN),
                chain_type="stuff",
                retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
                return_source_documents=True,
                chain_type_kwargs={"prompt": set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)}
            )

            response = qa_chain.invoke({"query": user_prompt})

            result = response["result"]
            sources = response.get("source_documents", [])

            st.chat_message("assistant").markdown(f"**Answer:**\n{result}")

            if sources:
                st.expander("📖 Source Documents").write(
                    "\n\n".join(f"- {doc.metadata.get('source', 'Unknown Source')}" for doc in sources)
                )

            st.session_state.messages.append({"role": "assistant", "content": result})

        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    main()