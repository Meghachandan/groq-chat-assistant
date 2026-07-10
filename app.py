import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler


st.set_page_config(
    page_title="OpenSource Agentic AI System",
    page_icon="🤖",
)

st.title("🤖 OpenSource Agentic AI System")

groq_api_key = st.secrets["GROQ_API_KEY"]


llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0,
    streaming=True,
)


search = DuckDuckGoSearchRun(name="Web Search")

arxiv_wrapper = ArxivAPIWrapper(
    top_k_results=2,
    doc_content_chars_max=500,
)

arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

tools = [search, arxiv]
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=False,
    max_iterations=2,
    early_stopping_method="generate",
    agent_kwargs={
        "prefix": """
You are a helpful AI assistant.

Rules:
1. Answer from your own knowledge whenever possible.
2. Use Web Search only if the question requires recent or real-time information.
3. Use ArXiv only if the user specifically asks for research papers or academic publications.
4. Never call the same tool repeatedly for the same question.
5. After using a tool once, provide the final answer immediately.
"""
    },
)


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hello! I can search the web and research papers using Groq-powered AI."
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])



prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        st_callback = StreamlitCallbackHandler(
            st.container(),
            expand_new_thoughts=False
        )

        try:
            response = agent.run(
                prompt,
                callbacks=[st_callback]
            )
        except Exception as e:
            response = f"❌ Error: {e}"

        st.write(response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )
