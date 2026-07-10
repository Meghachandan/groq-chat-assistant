prompt = st.chat_input("Ask me anything...")

if prompt:

    # Store and display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Questions that don't need tools
    simple_questions = [
        "what is",
        "define",
        "explain",
        "who is",
        "difference between",
        "how does",
        "why",
    ]

    with st.chat_message("assistant"):

        callback = StreamlitCallbackHandler(
            st.container(),
            expand_new_thoughts=False,
        )

        try:

            if any(prompt.lower().startswith(x) for x in simple_questions):
                # Answer directly using the LLM
                response = llm.invoke(prompt).content

            else:
                # Use Agent + Tools
                response = agent.run(
                    prompt,
                    callbacks=[callback],
                )

        except Exception as e:
            response = f"❌ Error: {e}"

        st.write(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )
