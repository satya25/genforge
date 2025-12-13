"""
============================================================
 File: app.py
 Project: Agentic Hello World (GenForge Workshop Series)
 Author: Satya Prakash Nigam
 Created: December 2025
============================================================

Purpose:
--------
This is the entry point for the Agentic Hello World demo
application. It uses Streamlit to provide a simple web UI
and integrates with a lightweight Ollama model to generate
a basic response.

The goal is to demonstrate:
1. How to launch a minimal agent application.
2. How to connect to a local Ollama model.
3. How to display agent responses in a Streamlit app.

Notes:
------
- This file is intentionally simple and verbose for
  pedagogical clarity.
- All code is PEP8 compliant and heavily documented.
============================================================
"""

import streamlit as st
import subprocess


def run_ollama_query(model_name: str, prompt: str) -> str:
    """
    Run a query against a local Ollama model.

    Parameters
    ----------
    model_name : str
        The name of the Ollama model to use (e.g., "phi3:mini").
    prompt : str
        The text prompt to send to the model.

    Returns
    -------
    str
        The model's response as plain text.
    """
    try:
        # Call Ollama CLI with subprocess and capture output
        result = subprocess.run(
            ["ollama", "run", model_name],
            input=prompt.encode("utf-8"),
            capture_output=True,
            check=True
        )
        return result.stdout.decode("utf-8").strip()
    except subprocess.CalledProcessError as error:
        return f"Error running Ollama model: {error}"


def main():
    """
    Main function to launch the Streamlit app.

    Provides:
    - A title and description.
    - A text input box for user prompts.
    - A button to trigger the agent.
    - Display of the agent's response.
    """
    st.title("🤖 Agentic Hello World")
    st.write(
        """
        Welcome to the **Agentic Hello World** demo!
        This is your first agent application in the GenForge series.
        Type a prompt below and let the agent respond.
        """
    )

    # Default lightweight model for demo
    default_model = "phi3:mini"

    # User input
    user_prompt = st.text_input("Enter your prompt:", "Hello, Agent!")

    if st.button("Run Agent"):
        st.write("Running agent... please wait.")
        response = run_ollama_query(default_model, user_prompt)
        st.success("Agent Response:")
        st.write(response)


if __name__ == "__main__":
    main()
