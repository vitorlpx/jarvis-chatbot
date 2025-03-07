# **Jarvis - Assistente de IA 🤖**  

Este é um chatbot interativo baseado em **Streamlit** e **LangChain**, que utiliza a API **Groq (Llama 3.3-70B)** para gerar respostas inteligentes. O diferencial deste assistente é a capacidade de **analisar documentos** e responder perguntas com base no conteúdo extraído de **sites, PDFs e vídeos do YouTube**.  

## 🚀 **Funcionalidades**
✔️ **Carregamento de Documentos**:  
- 🔗 **Sites**: Extrai texto de páginas web.  
- 📄 **PDFs**: Lê e processa arquivos PDF.  
- 🎥 **YouTube**: Obtém transcrições de vídeos (quando disponíveis).  

✔️ **Interação via Chat**:  
- O usuário pode **perguntar** sobre o conteúdo carregado.  
- O assistente responde de forma contextualizada, **baseando-se nas informações carregadas**.  

✔️ **Histórico de Conversa**:  
- O histórico da conversa é armazenado na sessão do usuário.  
- As mensagens do usuário aparecem à direita, enquanto as respostas da IA aparecem à esquerda.  
- Uso de avatares personalizados para diferenciar as mensagens.  

---

## 🛠️ **Possíveis Melhorias**
Este projeto pode ser expandido com diversas melhorias, tais como:

### 1️⃣ **Armazenamento de Dados**
Atualmente, o histórico de conversas é armazenado apenas na sessão do usuário. Para preservar o histórico entre sessões, podemos:
- Usar um banco de dados (SQLite, PostgreSQL, MongoDB, etc.).
- Implementar um sistema de autenticação para salvar conversas por usuário.

### 2️⃣ Melhorias no Processamento de Documentos
- Melhor manipulação de PDFs escaneados via OCR (exemplo: pytesseract).
- Suporte a mais fontes de dados (Google Drive, Dropbox, etc.).

### 3️⃣ Refinamento das Respostas
- Melhor ajuste do prompt engineering para refinar as respostas da IA.
- Implementação de memória a longo prazo para que a IA lembre de contextos anteriores.

### 4️⃣ Melhor UI/UX no Streamlit
- Uso de componentes interativos, como dropdowns e botões personalizados.
- Adição de um modo escuro para uma melhor experiência do usuário.

### 5️⃣ Deploy na Web
Hospedar a aplicação no Streamlit Cloud, Railway, Render, ou AWS para facilitar o acesso.

Desenvolvido por *Vitor*.
