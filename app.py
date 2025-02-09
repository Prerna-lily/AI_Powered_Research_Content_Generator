from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool

from dotenv import load_dotenv

load_dotenv()

topic="Medical Industry - COVID-19"
#tool 1
llm = LLM(model="gpt-4")
#tool 2
search_tool = SerperDevTool(n=10)

#agent 1
senior_research_analyst = Agent(name="Senior Research Analyst",
                                role="Research Analyst",
                                goal=f"To provide the latest information on the {topic} from reliable web sources.",
                                backstory="You're an expert research analyst with advanced web research skills."
                                "you excel at finding, analyzing, and synthesizing information from"
                                "across the internet using search tools. You're skilled at "
                                "distinguishing between reliable and unreliable sources"
                                "fact-checking, cross-referencing, and synthesizing information."
                                "identifiying key patterns and insights. You provide"
                                "wel organized research briefs with proper citations and references.",
                                allow_delegation=False,
                                verbose=True,
                                tools=[search_tool],
                                llm=llm)

#agent 2
content_writer = Agent(name="Content Writer",
                       role="Writer",
                       goal="Transform the research findings into engaging blog posts while maintaining accuracy and credibility.",
                       backstory="You're a skilled content writer specialized in creating"
                       "engaging accessible content from technical research."
                       "You work closely with the senior research analyst and excel at maintaining the perfect"
                       "balance between informative and entertaining writing,"
                       "while ensuring all facts and citations from the research are properly incorporated.",
                        allow_delegation=False,
                        verbose=True,
                        llm=llm)

#Research tasks
research_task = Task(
    description="""1. Conduct comprehensive research on the latest developments in the medical industry related to COVID-19.
    2. Identify key trends, emerging technologies, and breakthroughs in the field.
    3. Include all relevant citations and sources""",
    expected_output="""A well-organized research brief with detailed information on the latest developments in the medical industry related to COVID-19, 
    including key trends, emerging technologies, and breakthroughs, with proper citations and references.""",
    agent=senior_research_analyst,
)

#task 2 
writing_task = Task(
    description="""1. Transform the research findings into an engaging blog post.
    2. Write a blog post that is informative, engaging, and accessible to a general audience.
    3. Ensure all facts and citations from the research are properly incorporated.""",
    expected_output="""An engaging blog post that transforms the research findings into accessible content, maintaining accuracy and credibility, 
    with proper incorporation of facts and citations from the research.""",
    agent=content_writer,
)

crew = Crew(agents=[senior_research_analyst, content_writer], tasks=[research_task, writing_task],verbose=True)

result = crew.kickoff(inputs={"topic":topic})
print(result)