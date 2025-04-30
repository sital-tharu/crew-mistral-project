from crewai import Task

def get_research_task(agent, topic):
    return Task(
        description=f"Research and explain the topic: {topic}",
        agent=agent,
        expected_output=f"A detailed summary of {topic} in clear, simple language."
    )
