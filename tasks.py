from crewai import Task

# Task for the Researcher Agent
def research_task(topic):
    return Task(
        description=f"Research the topic: {topic} and provide a detailed summary.",
        expected_output="A comprehensive summary of the topic."
    )

# Task for the Creator Agent
def create_article_task():
    return Task(
        description="Write an article based on the research summary provided.",
        expected_output="A well-structured article draft."
    )

# Task for the Reviewer Agent
def review_article_task():
    return Task(
        description="Review and edit the article for clarity, accuracy, and grammar.",
        expected_output="A reviewed and improved article."
    )

# Task for the Publisher Agent
def publish_article_task():
    return Task(
        description="Publish the final article as a Markdown (.md) file.",
        expected_output="A Markdown file containing the final article."
    )
