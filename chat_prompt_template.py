from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} assistant.'),
    ('human', 'Explain about the {topic} in detail.')
    
])
prompt =template.invoke({'domain': 'Computer Science', 'topic': 'AI'})
print(prompt)
