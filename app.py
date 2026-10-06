import streamlit as st
from langchain_ollama import OllamaLLM

st.set_page_config(
    page_title="AI Scam Detector",
    page_icon="🛡️"
)

st.title("🛡️ AI Scam Detector Chatbot")
st.write("Chat with the AI to check suspicious messages, links, offers, and emails.")

# Create Ollama model
llm = OllamaLLM(model="llama3.2")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_message = st.chat_input(
    "Paste a suspicious message here..."
)

if user_message:

    # Show user message
    st.chat_message("user").markdown(user_message)

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    # AI prompt
    prompt = f"""
You are an AI Scam Detection Assistant.

The user has sent this message:

{user_message}

Analyze it and determine whether it is:
- SCAM
- SAFE
- SUSPICIOUS

Respond in a simple and friendly way.

Use this format:

Verdict: SCAM / SAFE / SUSPICIOUS

Reason:
Explain briefly why.

Warning Signs:
Mention important warning signs.

Safety Advice:
Give practical safety advice.

Do not invent facts that are not present in the message.
"""

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("🤖 Analyzing..."):
            response = llm.invoke(prompt)

        st.markdown(response)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })