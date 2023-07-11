# example 1
from langchain import OpenAI
llm = OpenAI(temperature=0.9)
req = "What would be a good company name for a company that makes colorful socks?"
res = llm.predict(req)
print("Summary")
print("req:", req)
print("res:", res)
