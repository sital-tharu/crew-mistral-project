from crewai import Agent
from langchain_community.llms import Ollama

llm = Ollama(model="ollama/mistral")


researcher = Agent(
    role='AI Researcher',
    goal='Research and summarize complex topics in simple terms',
    backstory='An expert in AI with a passion for simplifying knowledge for everyone.',
    verbose=True,
    llm=llm
)
