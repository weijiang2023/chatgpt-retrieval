# example 3: prompt templates
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("What is a good name for a company that make {product}")
prompt.format(product="colorful socks")
