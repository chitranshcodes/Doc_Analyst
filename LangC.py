from langchain.llms import ollama
from langchain_core.messages import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()


llm = ollama(
    model="gpt-3.5-turbo",
    temperature=0.7
)

message=[
    SystemMessage(content="you are a helpful AI Assistant"),
    HumanMessage(content="What is the capital of India?")
]

response=llm.invoke(message)

print(response.content)