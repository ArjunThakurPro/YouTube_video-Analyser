from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools
from textwrap import dedent

load_dotenv()


def youtubeAnalyzer():
    return Agent(
        name="YouTube Agent",
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[YouTubeTools()],
        instructions=dedent("""\
        "You are a concise YouTube video analyst. "
        "Analyze the video URL or transcript. "
        "Return: overview, summary, key points, important insights, and takeaways. "
        "Be factual, brief, and note missing details instead of guessing."
    """),
        add_datetime_to_context=True,
        markdown=True,
    )
