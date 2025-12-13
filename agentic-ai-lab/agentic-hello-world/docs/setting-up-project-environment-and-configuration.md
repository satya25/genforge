## 📄 docs/setting-up-project-environment-and-configuration.md (Step Outline)
 
# Setting Up Project Environment and Configuration

## Step 1: Scaffold the Project
- Copy or fork the previous project folder.
- Edit `project_set_up.sh` to match the new project name.
- Execute the script:
  ```bash
  chmod +x project_set_up.sh
  ./project_set_up.sh
  ```
- This creates the folder structure and seeds empty files.

## Step 2: Create and Activate Virtual Environment
- Windows (Git Bash):
  ```bash
  python -m venv .venv
  source .venv/Scripts/activate
  ```
- Windows (PowerShell):
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- macOS/Linux:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

## Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
 
---
 
## Step 4: Set Up Local Git Environment and Remote Repository

Before running the application, we must prepare Git for version control and connect to a remote repository on GitHub. This ensures that all project files can be tracked, shared, and collaborated on.

### 4.1 Initialize Git Locally
From the project root folder (`agentic-hello-world`), run:
```bash
git init
```
This creates a new local Git repository.

### 4.2 Configure Git User Details
Set your Git username and email (only once per machine, unless you want to change them):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify configuration:
```bash
git config --list
```

### 4.3 Create an Empty Remote Repository on GitHub
1. Log in to your GitHub account.
2. Click **New Repository**.
3. Name the repository (e.g., `agentic-hello-world`).
4. Keep it **empty** (do not add README, .gitignore, or license — these already exist locally).
5. Copy the repository URL (HTTPS or SSH).

Example HTTPS URL:
```
https://github.com/<your-username>/agentic-hello-world.git
```

### 4.4 Link Local Repo to Remote
Back in your terminal, link the local project to the remote repository:
```bash
git remote add origin https://github.com/<your-username>/agentic-hello-world.git
```

Verify the remote:
```bash
git remote -v
```

You should see:
```
origin  https://github.com/<your-username>/agentic-hello-world.git (fetch)
origin  https://github.com/<your-username>/agentic-hello-world.git (push)
```

--- 

## Step 5: Launch Hello World Agent
```bash
streamlit run app.py
```

This will start a local server and open the Hello World agent demo in your browser.
 

--- 

Perfect, Satya ✅ — here’s the **Step 6: Git Remote Push** section for your `docs/setting-up-project-environment-and-configuration.md`. This will guide students through committing their work and pushing it to GitHub after confirming the app runs successfully.

---

## 📄 Step 6: Git Remote Push

Once the Hello World agent application runs successfully, it’s time to save your work and push it to the remote GitHub repository.

### 6.1 Stage All Files
From the project root folder:
```bash
git add .
```
This stages all files (including README.md, LICENSE, app.py, requirements.txt, etc.) for commit.

### 6.2 Commit Changes
Create your first commit with a clear message:
```bash
git commit -m "Initial commit: scaffold + Hello World agent app"
```

### 6.3 Push to Remote Repository
Push the committed changes to the remote GitHub repository:
```bash
git push -u origin main
```

- `-u` sets the upstream branch, so future pushes can be done simply with:
  ```bash
  git push
  ```

### 6.4 Verify on GitHub
1. Open your GitHub repository in a browser.
2. Refresh the page.
3. You should now see all project files (README.md, LICENSE, app.py, etc.) uploaded.

### 6.5 Common Issues
- **Authentication required:**  
  - If using HTTPS, GitHub may prompt for username/password or a personal access token.  
  - If using SSH, ensure your SSH keys are configured (`ssh -T git@github.com` to test).
- **Branch mismatch:**  
  - If your local branch is not `main`, rename it:  
    ```bash
    git branch -M main
    git push -u origin main
    ```

---

✅ At this point, your project is fully version-controlled and published to GitHub.  

---
 
## 📄 Step 7: Run Unit Tests to Validate Scaffold

After launching the Hello World agent, it is important to verify that the scaffolded codebase is functional and testable. This step introduces students to **unit testing** as a professional practice.

---

### 7.1 Why Run Tests?
- Confirms that the scaffolded files are correctly linked.
- Validates that the `HelloAgent` class works as expected.
- Builds good habits: always test before extending functionality.

---

### 7.2 Run Tests Using `unittest`
From the project root folder:
```bash
python -m unittest discover tests
```

- `discover tests` will automatically find and run all test files inside the `tests/` directory.
- By default, it looks for files matching `test*.py`.

---

### 7.3 Expected Output
You should see something like:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

- The single dot (`.`) indicates one test passed.
- `OK` confirms all tests succeeded.

---

### 7.4 Run Tests Using `pytest` (Optional)
If you prefer `pytest` (install separately):
```bash
pip install pytest
pytest
```

Expected output:
```
============================= test session starts ==============================
collected 1 item

tests/test_agent.py .                                                   [100%]

============================== 1 passed in 0.01s ===============================
```

---

### 7.5 What This Proves
- The `HelloAgent.greet()` method returns the expected string.
- The scaffold is functional and ready for extension.
- Students can now safely add new agent logic, knowing the base passes tests.

---
 
