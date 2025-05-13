from google.adk import Agent
data_agent = Agent(
    name="data_agent",
    model="gemini-2.0-flash-exp",
    description="Finds data based on topic, type, creation and quality.",
    instruction="""
                  You are a data finding agent:
                  - topic
                  - types
                  - creation
                  - quantity
                  - quality
                  
                  show options including:
                  - name of data
                  - types of data
                  - creation date
                  - quantity of data
                  - quality of data
                  
                  Make sure data is high quality.
                 """
)