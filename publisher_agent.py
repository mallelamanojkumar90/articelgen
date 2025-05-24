from crewai import Agent, Task
import os
import subprocess

class PublisherAgent(Agent):
    def publish(self, article_text, filename="article.md"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(article_text)
        print(f"Article published as {filename}")
        # Open the folder and select the file in Windows Explorer
        abs_path = os.path.abspath(filename)
        subprocess.run(["explorer", "/select,", abs_path], check=False)
