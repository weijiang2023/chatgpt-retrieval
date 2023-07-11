# example 2
'''
Chat models are a variation on language models. While chat models use language models under the hood, the interface they expose is a bit different: rather than expose a "text in, text out" API, they expose an interface where "chat messages" are the inputs and outputs.

You can get chat completions by passing one or more messages to the chat model. The response will be a message. The types of messages currently supported in LangChain are AIMessage, HumanMessage, SystemMessage, and ChatMessage -- ChatMessage takes in an arbitrary role parameter. Most of the time, you'll just be dealing with HumanMessage, AIMessage, and SystemMessage.
'''

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(temperature=0)
res = chat.predict_messages([HumanMessage(content="Translate this sentence from English to French. I love programming")])
print(res)
# >> AIMessage(content="J'aime programmer.", additional_kwargs={})
