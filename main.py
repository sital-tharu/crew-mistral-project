from crewai import Crew
from agents.researcher_agent import researcher
from tasks.research_task import get_research_task

# Define your topic
topic = input("Enter a topic to research: ")

# Create the task
task = get_research_task(researcher, topic)

# Create the crew and run
crew = Crew(agents=[researcher], tasks=[task])
result = crew.kickoff()

print("\n\n--- Final Output ---\n")
print(result)
