from agents import create_researcher, create_creator, create_reviewer
from publisher_agent import PublisherAgent
from tasks import research_task, create_article_task, review_article_task
from crewai import Crew
from dotenv import load_dotenv
import os
import sys

# Increase recursion limit to prevent stack overflow
sys.setrecursionlimit(5000)

def generate_article(topic, progress_callback=None):
    """
    Generate an article on the given topic using CrewAI agents.
    
    Args:
        topic (str): The topic for the article
        progress_callback (callable, optional): Function to call with progress updates.
            Called with (agent_name, status) where status is 'started' or 'completed'
    
    Returns:
        dict: {
            'status': 'success' or 'error',
            'article': article text (if successful),
            'error': error message (if failed)
        }
    """
    try:
        load_dotenv()  # Load environment variables from .env file
        
        if progress_callback:
            progress_callback("Initializing", "Preparing agents...")
        
        # Create agents
        researcher = create_researcher()
        creator = create_creator()
        reviewer = create_reviewer()
        
        # Define tasks
        research = research_task(topic)
        create_article = create_article_task()
        review_article = review_article_task()
        
        # Assign agents to tasks
        research.agent = researcher
        create_article.agent = creator
        review_article.agent = reviewer
        
        # Set up CrewAI workflow with recursion prevention
        crew = Crew(
            tasks=[research, create_article, review_article],
            verbose=False,
            max_rpm=10
        )
        
        # Execute with progress tracking
        if progress_callback:
            progress_callback("Researcher", "Gathering information on the topic...")
        
        results = crew.kickoff()
        
        if progress_callback:
            progress_callback("Publisher", "Finalizing article...")
        
        # Extract the reviewed article from results
        # CrewAI returns results in different formats, handle them safely
        try:
            if hasattr(results, 'raw'):
                reviewed_article = str(results.raw)
            elif isinstance(results, str):
                reviewed_article = results
            else:
                reviewed_article = str(results)
        except Exception as e:
            # Fallback to simple string conversion
            reviewed_article = str(results) if results else "Error extracting article content"
        
        if progress_callback:
            progress_callback("Completed", "Article generation finished!")
        
        return {
            'status': 'success',
            'article': reviewed_article,
            'topic': topic
        }
        
    except Exception as e:
        if progress_callback:
            progress_callback("Error", f"Failed: {str(e)}")
        return {
            'status': 'error',
            'error': str(e)
        }

# CLI interface
def main():
    """Command-line interface for article generation"""
    load_dotenv()
    
    topic = input("Enter the topic for the article: ")
    
    print(f"\n🚀 Starting article generation on: {topic}\n")
    
    def cli_progress(agent, status):
        """Progress callback for CLI"""
        print(f"📍 {agent}: {status}")
    
    result = generate_article(topic, progress_callback=cli_progress)
    
    if result['status'] == 'success':
        # Save the article using publisher
        publisher = PublisherAgent(
            name="Publisher",
            role="Publishes the reviewed article as a .md file.",
            goal="Save the final article to a Markdown file.",
            backstory="You are responsible for publishing articles in Markdown format."
        )
        publisher.publish(result['article'], filename="article.md")
        print("\n✅ Article generation completed successfully!")
    else:
        print(f"\n❌ Error: {result['error']}")

if __name__ == "__main__":
    main()
