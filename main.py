import streamlit as st

from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader, YoutubeLoader
from dotenv import load_dotenv

load_dotenv()

chat = ChatGroq(model="llama-3.3-70b-versatile")

def resposta_bot(mensagens, documento):
    mensagem_system = f"""Você é um assistente chamado Jarvis.
    Você utiliza as seguintes informações para dar as suas respostas: {documento}
    """
    mensagens_modelo = [SystemMessage(content=mensagem_system)] + mensagens

    template = ChatPromptTemplate.from_messages([(msg.type, msg.content) for msg in mensagens_modelo])
    chain = template | chat
    return chain.invoke({}).content

def carrega_site(url):
    loader = WebBaseLoader(url)
    lista_ws = loader.load()
    return "".join(doc.page_content for doc in lista_ws)

def carrega_pdf(uploaded_file):
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())
    loader = PyPDFLoader("temp.pdf")
    lista_pdf = loader.load()
    return "".join(doc.page_content for doc in lista_pdf)

def carrega_youtube(url):
    loader = YoutubeLoader.from_youtube_url(url, language=["pt"])
    lista_yt = loader.load()
    return "".join(doc.page_content for doc in lista_yt)

st.title("Jarvis - Assistente de IA 🤖")

if "historico" not in st.session_state:
    st.session_state.historico = []
if "documento" not in st.session_state:
    st.session_state.documento = ""

select_box = st.selectbox("Escolha o tipo de documento", ["Site", "PDF", "Youtube"])

if select_box == "Site":
    url = st.text_input("Digite a URL do site:")
    if url:
        st.session_state.documento = carrega_site(url)
        st.write("✅ **Conteúdo carregado!** Agora você pode fazer perguntas.")
elif select_box == "PDF":
    uploaded_file = st.file_uploader("Escolha um arquivo PDF:", type="pdf")
    if uploaded_file:
        st.session_state.documento = carrega_pdf(uploaded_file)
        st.write("✅ **Conteúdo carregado!** Agora você pode fazer perguntas.")
elif select_box == "Youtube":
    url = st.text_input("Digite a URL do vídeo do Youtube:")
    if url:
        st.session_state.documento = carrega_youtube(url)
        st.write("✅ **Conteúdo carregado!** Agora você pode fazer perguntas.")

for msg in st.session_state.historico:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar="🧑‍💻"):  
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.write(msg.content)

prompt_usuario = st.chat_input("Digite sua pergunta:")

if prompt_usuario:
    st.session_state.historico.append(HumanMessage(content=prompt_usuario))

    resposta = resposta_bot(st.session_state.historico, st.session_state.documento)

    st.session_state.historico.append(AIMessage(content=resposta))

    with st.chat_message("user", avatar="🧑‍💻"):
        st.write(prompt_usuario)
    with st.chat_message("assistant", avatar="🤖"):
        st.write(resposta)