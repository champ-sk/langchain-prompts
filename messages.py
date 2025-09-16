from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
messages = [SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content="Tell me about Langchain")]

response = model.invoke(messages)
messages.append(AIMessage(content = response.content))

print(messages)
