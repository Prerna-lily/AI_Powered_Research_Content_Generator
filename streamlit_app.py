import streamlit as st
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit UI
st.title("AI-Powered Research & Content Generator")

# User input for topic
topic = st.text_input("Enter a topic for research:", "Medical Industry - COVID-19")

if st.button("Generate Content"):
    st.write("Running AI Agents for research and writing...")

    # Initialize AI components
    llm = LLM(model="gpt-4")
    search_tool = SerperDevTool(n=10)

    # Define Agents
    analyst = Agent(
        name="Senior Research Analyst",
        role="Research Analyst",
        goal=f"Provide the latest {topic} insights from reliable sources.",
        backstory="Expert in web research and information synthesis.",
        tools=[search_tool],
        llm=llm
    )

    writer = Agent(
        name="Content Writer",
        role="Writer",
        goal="Convert research into engaging blog posts.",
        backstory="Specialist in crafting informative and credible content.",
        llm=llm
    )

    # Define Tasks
    research_task = Task(
        description=f"Conduct in-depth research on {topic}, covering trends, breakthroughs, and references.",
        expected_output="A structured research summary.",
        agent=analyst,
    )

    writing_task = Task(
        description="Convert research into a compelling blog post with proper citations.",
        expected_output="A well-structured and engaging blog post.",
        agent=writer,
    )

    # Run AI Agents
    crew = Crew(agents=[analyst, writer], tasks=[research_task, writing_task])
    result = crew.kickoff(inputs={"topic": topic})

    # Display formatted content
    st.subheader("Generated Content")
    st.markdown(result, unsafe_allow_html=True)
