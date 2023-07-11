# example 6: Memory
from langchain import OpenAI, ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

print(conversation.run("Hi there!"))
print(conversation.run("I'm doing well! Just having a conversation with an AI."))
