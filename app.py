import streamlit as st

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_community.tools import (
    WikipediaQueryRun,
    ArxivQueryRun,
    DuckDuckGoSearchRun,
)
from langchain_community.utilities import (
    WikipediaAPIWrapper,
    ArxivAPIWrapper,
)



st.set_page_config(
    page_title="OpenSource Agentic AI",
    page_icon="🤖",
)

st.title("🤖 OpenSource Agentic AI System")



groq_api_key = st.secrets["GROQ_API_KEY"]



llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="llama-3.1-8b-instant",
    temperature=0,
)



wiki_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=300,
)

wiki = WikipediaQueryRun(
    api_wrapper=wiki_wrapper,
)

arxiv_wrapper = ArxivAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=300,
)

arxiv = ArxivQueryRun(
    api_wrapper=arxiv_wrapper,
)

search = DuckDuckGoSearchRun()

tools = [
    search,
    wiki,
    arxiv,
]



agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are an intelligent AI assistant.

Use:
- DuckDuckGo for current information.
- Wikipedia for general knowledge.
- ArXiv for research papers.

Always choose the appropriate tool automatically.
""",
)



if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])



prompt = st.chat_input("Ask anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ]
            }
        )

        answer = response["messages"][-1].content

        st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )
