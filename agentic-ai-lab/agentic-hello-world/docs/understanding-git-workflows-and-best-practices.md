
---

## 📄 docs/understanding-git-workflows-and-best-practices.md
 
# Understanding Git Workflows and Best Practices

## Overview
This document explains how to use Git effectively beyond the initial setup.  
It introduces branching, committing, pushing, and collaborating — the essential practices for working on agentic projects in a professional way.

---

## 1. Why Git Workflows Matter
- **Version control:** Track changes to your code over time.
- **Collaboration:** Work with teammates without overwriting each other’s work.
- **Experimentation:** Use branches to test new ideas safely.
- **Professional practice:** Mirrors industry standards for software development.

---

## 2. Basic Workflow Cycle
The most common Git workflow follows this cycle:

1. **Pull latest changes**  
   ```bash
   git pull origin main
   ```
   Keeps your local copy up to date.

2. **Create a new branch**  
   ```bash
   git checkout -b feature/my-new-agent
   ```
   Work on features or fixes in isolation.

3. **Make changes and commit**  
   ```bash
   git add .
   git commit -m "Add new agent feature"
   ```

4. **Push branch to remote**  
   ```bash
   git push origin feature/my-new-agent
   ```

5. **Open a Pull Request (PR)**  
   - On GitHub, request to merge your branch into `main`.
   - Team members can review before merging.

---

## 3. Branching Strategy
- **main branch:** Always stable, production-ready code.
- **feature branches:** For new features, experiments, or fixes.
- **hotfix branches:** For urgent bug fixes.

Naming convention:
- `feature/<name>` → e.g., `feature/agent-memory`
- `bugfix/<name>` → e.g., `bugfix/streamlit-ui`
- `hotfix/<name>` → e.g., `hotfix/dependency-error`

---

## 4. Commit Message Best Practices
- Use **imperative mood**: “Add agent class” not “Added agent class.”
- Keep messages concise but descriptive.
- Include context if needed:
  ```bash
  git commit -m "Refactor agent utils for better readability"
  ```

---

## 5. Collaboration Tips
- **Pull before you push:** Always sync with remote before committing new work.
- **Review PRs carefully:** Ensure code quality and clarity.
- **Resolve conflicts promptly:** Communicate with teammates if merge conflicts occur.
- **Use `.gitignore`:** Prevent unnecessary files (logs, cache, venv) from cluttering the repo.

---

## 6. Advanced Practices (Optional)
- **Rebase vs Merge:**  
  - `git rebase` keeps history linear.  
  - `git merge` preserves branch history.  
- **Tags and Releases:**  
  - Use `git tag v1.0.0` to mark stable versions.  
- **Stashing:**  
  - Temporarily save changes without committing:  
    ```bash
    git stash
    git stash pop
    ```

---

## 7. Summary
- Always work on branches, not directly on `main`.
- Write clear commit messages.
- Push regularly and review PRs.
- Keep your repo clean with `.gitignore`.

---

## Next Steps
After mastering this workflow:
- Apply branching strategies in your **agentic-ai-lab** projects.
- Collaborate with peers by opening and reviewing Pull Requests.
- Explore advanced Git features like rebasing, tagging, and stashing.
 

---
 

