import os
import streamlit as st
from constants import (
  MESSAGES,
  AI,
)
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    AIMessage,
)
from langchain_community.callbacks import StreamlitCallbackHandler
from ai.agent import agent_executer

def st_init():
    title = "Pokemon Chatbot"
    st.set_page_config(page_title=title)
    st.header(title)
    st.write("ポケモンに関する質問をオーキド博士が答えてくれます。")
    if MESSAGES not in st.session_state:
        st.session_state[MESSAGES] = []


def show_message(message: BaseMessage):
    with st.chat_message(message.type):
        st.markdown(message.content)


def append_message_to_session(message: BaseMessage):
    messages: list = st.session_state[MESSAGES]
    messages.append(message)


def main():
    st_init()

    for message in st.session_state[MESSAGES]:
        show_message(message)

    if prompt := st.chat_input("質問してください"):
        show_message(HumanMessage(content=prompt))

        with st.chat_message(AI):
            st_callback = StreamlitCallbackHandler(st.container())
            response = agent_executer.invoke(
                {"input": prompt, "chat_history": st.session_state[MESSAGES]},
                {"callbacks": [st_callback]},
            )
            st.write(response["output"])

            # stream = agent_executer.stream({
            #     "input": prompt,
            #     "chat_history": st.session_state[MESSAGES],
            # })
            # response = st.write_stream(stream)

        append_message_to_session(HumanMessage(content=prompt))
        append_message_to_session(AIMessage(content=response["output"]))


if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
    main()
