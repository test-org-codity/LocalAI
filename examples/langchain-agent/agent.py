## Loosely based from https://gist.github.com/wiseman/4a706428eaabf4af1002a07a114f61d6

import os

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents.tools import Tool
from langchain.llms import OpenAI

base_path = os.environ.get('OPENAI_API_BASE', 'http://api:8080/v1')
model_name = os.environ.get('MODEL_NAME', 'gpt-3.5-turbo')

class PythonREPL:
    """Simulates a standalone Python REPL."""

    def run(self, command: str) -> str:
        """Run command and returns anything printed."""
        # SECURITY WARNING: This is an example only. For production use, implement proper sandboxing.
        # Recommended: Use subprocess with restricted permissions, containers, or a proper sandboxed interpreter.
        raise NotImplementedError(
            "PythonREPL execution is disabled for security reasons. "
            "This pattern allows arbitrary code execution via LLM output, which can be influenced by prompt injection. "
            "For safe execution, use: subprocess with restricted permissions, containers, seccomp, or a sandboxed interpreter."
        )

llm = OpenAI(temperature=0.0, openai_api_base=base_path, model_name=model_name)
python_repl = Tool(
        "Python REPL",
        PythonREPL().run,
        """A Python shell. Use this to execute python commands. Input should be a valid python command.
        If you expect output it should be printed out.""",
    )
tools = [python_repl]
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
agent.run("What is the 10th fibonacci number?")

