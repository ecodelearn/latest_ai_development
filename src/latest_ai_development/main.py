#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from crewai import Agent
from latest_ai_development.crew import LatestAiDevelopment
from latest_ai_development.tools.enhanced_search_tool import EnhancedSearchTool

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Default topic for searches
default_topic = 'CrewAI with Web Ui Framework'

# Create a global instance of the enhanced search tool
search_tool = EnhancedSearchTool()

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # Configure search with topic
    search_config = search_tool.builder(default_topic)
    search_tool.configure(search_config)
    
    try:
        crew = LatestAiDevelopment()
        crew.researcher = lambda: Agent(
            config=crew.agents_config['researcher'],
            verbose=True,
            tools=[search_tool]
        )
        crew.crew().kickoff(inputs=search_config.as_dict)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    # Configure search with topic
    search_config = search_tool.builder(default_topic)
    search_tool.configure(search_config)
    
    try:
        crew = LatestAiDevelopment()
        crew.researcher = lambda: Agent(
            config=crew.agents_config['researcher'],
            verbose=True,
            tools=[search_tool]
        )
        crew.crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=search_config.as_dict)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        LatestAiDevelopment().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    # Configure search with topic
    search_config = search_tool.builder(default_topic)
    search_tool.configure(search_config)
    
    try:
        crew = LatestAiDevelopment()
        crew.researcher = lambda: Agent(
            config=crew.agents_config['researcher'],
            verbose=True,
            tools=[search_tool]
        )
        crew.crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=search_config.as_dict)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
