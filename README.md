**AI-Powered Research & Content Generator**

Overview

This project is an AI-powered research and content generation tool built using Streamlit. It utilizes CrewAI for task delegation and Serper API for fetching the latest web research. The application allows users to input a topic and generates a well-structured blog post based on AI-driven research.

**Features**

AI-driven research: Uses CrewAI to automate research tasks.

Content generation: Converts research findings into an engaging blog post.

Streamlit UI: Simple and interactive web-based user interface.

Serper API: Retrieves real-time web data for research.

GPT-4 LLM: Ensures high-quality text generation.

**Technologies Used**

Python

Streamlit

CrewAI

Serper API

OpenAI GPT-4

Dotenv (for environment variables)

**Installation**

1. Clone the repository

2. Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows

3. Install dependencies

pip install -r requirements.txt

4. Set up environment variables

Create a .env file in the root directory and add:

SERPER_API_KEY=your_serper_api_key
OPENAI_API_KEY=your_openai_api_key

5. Run the Streamlit app

streamlit run app.py

**How It Works**

The user inputs a topic in the Streamlit app.

CrewAI assigns research tasks to the Senior Research Analyst agent.

The analyst fetches information using Serper API.

The Content Writer agent transforms research findings into a structured blog post.

The result is displayed on the Streamlit interface.
