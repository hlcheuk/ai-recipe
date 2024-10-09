import secrets
import datetime
from dotenv import load_dotenv
import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langsmith import Client
from graph import graph
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

import uuid
import asyncio

from src.prompts.prompts import BEGINNING_CANNED_RESPONSE

# Load env var
load_dotenv()

# Initialise Langsmith client
client = Client()

# Initialise memory
history = StreamlitChatMessageHistory(key="history")

# Streamlit page setting
st.set_page_config(initial_sidebar_state="collapsed")


# Main function to run the Streamlit app
def main():
    # Streamlit settings

    st.markdown(
        """<style>.block-container{max-width: 66rem !important;}</style>""",
        unsafe_allow_html=True,
    )
    st.title("Recipe Generator")
    st.markdown("---")

    # Session state initialization
    if "session_id" not in st.session_state.keys():
        st.session_state.session_id = secrets.token_urlsafe(16)
    if "session_start_time" not in st.session_state.keys():
        st.session_state.session_start_time = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    if "chat_history" not in st.session_state.keys():
        st.session_state.chat_history = [
            {"role": "assistant", "content": BEGINNING_CANNED_RESPONSE}
        ]
    if "answer_placeholder" not in st.session_state.keys():
        st.session_state.answer_placeholder = []
    if "streaming" not in st.session_state.keys():
        st.session_state.streaming = False
    if "config" not in st.session_state.keys():
        st.session_state.config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    # Display sidebar
    # sidebar_interface()

    # Display chat interface
    run_chat_interface()


# def sidebar_interface():
#     # Sidebar for prompt setting
#     with st.sidebar:
#         selected_llm = st.radio(
#             "Select a LLM",
#             ["GPT-3.5-Turbo"],
#         )

#         save = st.button("Update")
#         # reset = st.button("Reset prompt")

#     if selected_llm:
#         st.session_state.llm = selected_llm
#         print("Current session_state llm", st.session_state.llm)


# Display the chat history
def create_chat_area(chat_history):
    for chat in chat_history:
        role = chat["role"]
        with st.chat_message(role):
            st.write(chat["content"])


# async def langgraph_streaming():
#     with st.chat_message("assistant"):
#         with st.spinner("thinking ..."):
#             question = {
#                 "messages": [
#                     HumanMessage(
#                         content=st.session_state.chat_history[-1]["content"].strip()
#                     )
#                 ]
#             }
#             full_output = ""
#             st.session_state.answer_placeholder.append(st.empty())
#             print("-------------------")
#             async for event in graph.astream_events(
#                 question, config=st.session_state.config, version="v1"
#             ):
#                 kind = event["event"]
#                 if kind == "on_chat_model_stream":
#                     content = event["data"]["chunk"].content
#                     if content:
#                         full_output += content
#                         st.session_state.answer_placeholder[-1].write(full_output)
#             message = {
#                 "role": "assistant",
#                 "content": full_output,
#             }
#             st.session_state.chat_history.append(message)


def langgraph_invoke():
    show_response_nodes = [
        "chitchat",
        "need_for_recipe",
        "need_for_other_help",
    ]
    with st.chat_message("assistant"):
        with st.spinner("thinking ..."):
            question = {
                "messages": [
                    HumanMessage(
                        content=st.session_state.chat_history[-1]["content"].strip()
                    )
                ]
            }
            full_output = ""
            st.session_state.answer_placeholder.append(st.empty())
            print("-------------------")
            for event in graph.stream(question, config=st.session_state.config):
                for key, value in event.items():
                    if key in show_response_nodes:
                        print("--------------------------------------")
                        full_output = value["messages"][-1].content
                        st.session_state.answer_placeholder[-1].write(full_output)
            message = {
                "role": "assistant",
                "content": full_output,
            }
            st.session_state.chat_history.append(message)


# Run the chat interface within Streamlit
def run_chat_interface():
    # display chat history
    create_chat_area(st.session_state.chat_history)
    # User-provided prompt
    if prompt := st.chat_input(disabled=False):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
    if len(st.session_state.chat_history) >= 2:
        # asyncio.run(langgraph_streaming())
        langgraph_invoke()

    def clear_chat_history():
        st.session_state.chat_history = [
            {"role": "assistant", "content": BEGINNING_CANNED_RESPONSE}
        ]
        st.session_state.config = {"configurable": {"thread_id": str(uuid.uuid4())}}
        st.session_state.tool_product_type = False
        st.session_state.tool_product_requirements = False
        history.clear()

    st.button("Clear Chat History", on_click=clear_chat_history)


if __name__ == "__main__":
    main()
