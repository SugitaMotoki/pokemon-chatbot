from langchain.agents import (
  AgentExecutor,
  create_openai_tools_agent
)
from .llms import llm
from .prompts import prompt
from .retrievers import (
  movie_retriever_tool,
  pokemon_retriever_tool,
)

tools = [movie_retriever_tool, pokemon_retriever_tool]
agent = create_openai_tools_agent(llm=llm, tools=tools, prompt=prompt)
agent_executer = AgentExecutor(agent=agent, tools=tools, verbose=False)
