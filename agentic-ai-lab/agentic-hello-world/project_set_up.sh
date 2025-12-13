#!/bin/bash
# ============================================================
# project_set_up.sh
# ------------------------------------------------------------
# Purpose:
#   This script sets up the internal folder structure and seeds
#   empty files for the "agentic-hello-world" demo project.
#
# Usage:
#   Run this script from inside the project root folder:
#
# 	chmod +x project_set_up.sh
# 	./project_set_up.sh
# 	
#
# Notes:
#   - All files created are EMPTY placeholders.
#   - This script is verbose and self-explanatory for beginners.
# ============================================================

echo ">>> Setting up Agentic Hello World project structure..."

# ------------------------------------------------------------
# 1. Create top-level folders
# ------------------------------------------------------------
echo ">>> Creating core folders..."
mkdir -p src/agents        # Source code for agent classes
mkdir -p src/utils         # Helper functions and utilities
mkdir -p config            # Configuration files (YAML/JSON)
mkdir -p docs              # Documentation and setup guides
mkdir -p tests             # Unit tests and validation scripts
mkdir -p notebooks         # Jupyter/Colab notebooks for experiments
mkdir -p data/raw          # Raw input data (if any)
mkdir -p data/processed    # Processed data outputs

# ------------------------------------------------------------
# 2. Seed empty files in each folder
# ------------------------------------------------------------
echo ">>> Seeding empty files..."

# Root-level files
touch README.md                     # Project overview
touch requirements.txt              # Python dependencies
touch app.py                        # Streamlit entry point (Hello World agent)
touch LICENSE                       # License placeholder
touch .gitignore                    # Git ignore rules

# Config folder
touch config/settings.yaml          # Placeholder for configuration

# Docs folder
touch docs/setting-up-project-environment-and-configuration.md  # Setup guide

# Source code
touch src/__init__.py               # Marks src as a Python package
touch src/agents/__init__.py        # Marks agents as a package
touch src/agents/hello_agent.py     # Placeholder agent class
touch src/utils/__init__.py         # Marks utils as a package
touch src/utils/helpers.py          # Placeholder utility functions

# Tests
touch tests/__init__.py             # Marks tests as a package
touch tests/test_agent.py           # Placeholder unit test file

# Notebooks
touch notebooks/demo.ipynb          # Placeholder notebook

# Data folders
touch data/raw/.gitkeep             # Keeps empty folder in Git
touch data/processed/.gitkeep       # Keeps empty folder in Git

# ------------------------------------------------------------
# 3. Final message
# ------------------------------------------------------------
echo ">>> Project structure created successfully!"
echo ">>> You can now open README.md or docs/setting-up-project-environment-and-configuration.md to begin."
