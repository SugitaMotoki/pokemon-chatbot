from langchain_openai import ChatOpenAI
from langchain.callbacks.base import BaseCallbackManager

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=1,
)
