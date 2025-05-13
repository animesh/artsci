from google.adk import Agent
papers_agent = Agent(
    name="papers_agent",
    model="gemini-2.0-flash-exp",
    description="Finds paper based on topic, type, creation and quality.",
    instruction="""
                  You are a paper finding agent:
                  - topic
                  - creation
                  - quality
                  
                  show options including:
                  - name of paper
                  - types of data included in the paper
                  - creation date
                  - quantity of data
                  - quality of data
                  
                  Make sure paper and data is high quality.
                 """
)
