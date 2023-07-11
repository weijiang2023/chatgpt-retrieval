# example 5: Chains
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI

# The language model we are going to use to control the agent.
llm = OpenAI(temperature=0)

# The tools we will give the agent access to. Note that the 'llm-math' tool uses an LLM, so we need to pass that in.
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Let's test it out
res = agent.run("What was the high temperature in guangzhou yesterday? What is that number raised to the .023 power?")
print(res)

'''
> Entering new AgentExecutor chain...
 I need to find the temperature first, then use the calculator to raise it to the .023 power.
Action: Search
Action Input: "High temperature in guangzhou yesterday"
Observation: https://www.timeanddate.com/weather/@8540398/historic
Thought: I can use the temperature from this website
Action: Calculator
Action Input: 32 raised to the .023 power
Observation: Answer: 1.0829750455259248
Thought: I now know the final answer
Final Answer: 1.0829750455259248

> Finished chain.
1.0829750455259248
'''
