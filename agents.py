from crewai import Agent, Task, Crew

# Researcher Agent: Gathers information on a topic
def create_researcher():
    return Agent(
        name="Researcher",
        role="Researches the given topic and provides a summary.",
        goal="Find and summarize relevant information.",
        backstory="You are an expert researcher skilled at gathering and summarizing information on any topic.",
        allow_delegation=False,
        max_iter=5
    )

# Creator Agent: Writes an article based on research
def create_creator():
    return Agent(
        name="Creator",
        role="Creates an article from research notes.",
        goal="Write a clear, informative article.",
        backstory="You are a talented writer who can turn research into engaging articles.",
        allow_delegation=False,
        max_iter=5
    )

# Reviewer Agent: Reviews and edits the article
def create_reviewer():
    return Agent(
        name="Reviewer",
        role="Reviews and edits the article for quality.",
        goal="Ensure the article is accurate and well-written.",
        backstory="You are a meticulous editor who ensures clarity, accuracy, and quality.",
        allow_delegation=False,
        max_iter=5
    )

# Publisher Agent: Publishes the article as a Markdown file
def create_publisher():
    return Agent(
        name="Publisher",
        role="Publishes the reviewed article as a .md file.",
        goal="Save the final article to a Markdown file.",
        backstory="You are responsible for publishing articles in Markdown format."
    )
