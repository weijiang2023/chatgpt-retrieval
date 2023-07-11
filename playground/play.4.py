# example 4: Chains
from langchain import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate.from_template("What is a good name for a company that make {product}")
chain = LLMChain(llm=llm, prompt=prompt)
res = chain.run("colorful socks")
print(res)
