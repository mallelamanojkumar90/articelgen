from agents import create_researcher, create_creator, create_reviewer
from publisher_agent import PublisherAgent
from tasks import research_task, create_article_task, review_article_task
from crewai import Crew
from dotenv import load_dotenv
import os

# Orchestrate the workflow with explicit publishing step
def main():
    load_dotenv()  # Load environment variables from .env file

    topic = input("Enter the topic for the article: ")

    researcher = create_researcher()
    creator = create_creator()
    reviewer = create_reviewer()
    publisher = PublisherAgent(
        name="Publisher",
        role="Publishes the reviewed article as a .md file.",
        goal="Save the final article to a Markdown file.",
        backstory="You are responsible for publishing articles in Markdown format."
    )

    # Define tasks
    research = research_task(topic)
    create_article = create_article_task()
    review_article = review_article_task()

    # Assign agents to tasks
    research.agent = researcher
    create_article.agent = creator
    review_article.agent = reviewer

    # Set up CrewAI workflow (excluding publisher)
    crew = Crew(tasks=[research, create_article, review_article])
    results = crew.kickoff()

    # Publisher step: save reviewed article
    # CrewAI's CrewOutput is a dict-like object, not a list. Get the last task's output as a string.
    reviewed_article = None
    if hasattr(results, 'values'):
        last_output = list(results.values())[-1] if results else ""
        # If the last output is a CrewOutput, get its string value
        if hasattr(last_output, 'values'):
            reviewed_article = str(list(last_output.values())[-1])
        else:
            reviewed_article = str(last_output)
    elif isinstance(results, dict):
        reviewed_article = str(list(results.values())[-1]) if results else ""
    else:
        reviewed_article = str(results or "")
    publisher.publish(reviewed_article, filename="article.md")

if __name__ == "__main__":
    main()
