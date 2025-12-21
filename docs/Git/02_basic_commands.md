# Basic Git Commands

Master the essential Git commands for everyday version control.

## Repository Initialization

### Creating a New Repository

```bash
# Create and navigate to project folder
mkdir my-project
cd my-project

# Initialize Git
git init
```

This creates a hidden `.git` folder that stores all Git data.

### Cloning an Existing Repository

```bash
# Clone from GitHub
git clone https://github.com/username/repo-name.git

# Clone to a specific folder
git clone https://github.com/username/repo-name.git my-folder

# Clone a specific branch
git clone -b branch-name https://github.com/username/repo-name.git
```

## Checking Repository Status

### git status

Shows the current state of your working directory and staging area.

```bash
git status
```

**Example output:**
```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  modified:   file1.py

Untracked files:
  file2.py

no changes added to commit
```

**Short format:**
```bash
git status -s
```

Output:
```
M  file1.py
?? file2.py
```

Symbols:
- `??` - Untracked file
- `M` - Modified file
- `A` - Added file
- `D` - Deleted file

## Staging Changes

### git add

Add files to the staging area (prepare for commit).

```bash
# Stage a specific file
git add filename.py

# Stage multiple files
git add file1.py file2.py

# Stage all changes in current directory
git add .

# Stage all changes in repository
git add -A

# Stage all Python files
git add *.py

# Stage all files in a folder
git add folder/
```

### Interactive Staging

```bash
# Choose what to stage interactively
git add -p filename.py
```

This lets you stage parts of a file (hunks) individually.

## Committing Changes

### git commit

Save staged changes to the repository.

```bash
# Commit with inline message
git commit -m "Add user authentication feature"

# Commit with detailed message (opens editor)
git commit

# Stage and commit in one command
git commit -am "Fix bug in data processing"
```

!!! warning "The -a flag"
    `git commit -a` only stages **modified** files, not **new** (untracked) files.

### Writing Good Commit Messages

**Bad:**
```
git commit -m "fixed stuff"
git commit -m "updates"
git commit -m "asdfgh"
```

**Good:**
```
git commit -m "Fix null pointer exception in user login"
git commit -m "Add data validation for email field"
git commit -m "Update README with installation instructions"
```

**Best Practice Format:**
```
Short summary (50 chars or less)

Detailed explanation if needed. Wrap at 72 characters.
Explain WHAT changed and WHY, not HOW.

- Bullet points are okay
- Use present tense: "Add" not "Added"
- Reference issues: Fixes #123
```

## Viewing History

### git log

View commit history.

```bash
# Full log
git log

# One line per commit
git log --oneline

# Last 5 commits
git log -5

# Show file changes
git log --stat

# Show actual changes
git log -p

# Graphical view
git log --graph --oneline --all

# Filter by author
git log --author="John Doe"

# Filter by date
git log --since="2024-01-01"
git log --after="2 weeks ago"
```

**Example output:**
```
commit a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
Author: Your Name <your.email@example.com>
Date:   Sat Jan 20 10:30:00 2024 +0000

    Add user authentication feature
```

### Viewing a Specific Commit

```bash
# Show commit details
git show a1b2c3d

# Show files changed
git show --name-only a1b2c3d

# Show changes in a file
git show a1b2c3d:path/to/file.py
```

## Viewing Changes

### git diff

See what changed in your files.

```bash
# Changes in working directory (not staged)
git diff

# Changes in staging area (staged but not committed)
git diff --staged
# or
git diff --cached

# Compare specific files
git diff filename.py

# Compare commits
git diff commit1 commit2

# Compare branches
git diff main feature-branch
```

**Example output:**
```diff
diff --git a/app.py b/app.py
index 1234567..abcdefg 100644
--- a/app.py
+++ b/app.py
@@ -10,7 +10,7 @@ def hello():
-    return "Hello World"
+    return "Hello, World!"
```

Legend:
- `-` Red line (removed)
- `+` Green line (added)
- Context lines (unchanged)

## Undoing Changes

### Unstaging Files

```bash
# Unstage a file (keep changes)
git restore --staged filename.py

# Unstage all files
git restore --staged .
```

### Discarding Changes

```bash
# Discard changes in working directory
git restore filename.py

# Discard all changes
git restore .
```

!!! danger "Warning"
    `git restore` (without --staged) **permanently discards** changes that aren't committed!

### Amending the Last Commit

```bash
# Fix the last commit message
git commit --amend -m "New commit message"

# Add forgotten files to last commit
git add forgotten-file.py
git commit --amend --no-edit
```

!!! warning "Don't Amend Pushed Commits"
    Only amend commits that haven't been pushed to a remote repository.

## Removing Files

### git rm

Remove files from Git and your working directory.

```bash
# Remove a file
git rm filename.py

# Remove from Git but keep locally
git rm --cached filename.py

# Remove all .log files
git rm *.log

# Remove folder
git rm -r folder-name/
```

Then commit:
```bash
git commit -m "Remove old log files"
```

## Moving/Renaming Files

### git mv

```bash
# Rename a file
git mv old-name.py new-name.py

# Move a file
git mv file.py folder/file.py
```

This is equivalent to:
```bash
mv old-name.py new-name.py
git rm old-name.py
git add new-name.py
```

## Ignoring Files

### .gitignore

Create a `.gitignore` file to specify files Git should ignore.

**Example .gitignore:**
```
# Python
*.pyc
__pycache__/
.venv/
venv/
*.egg-info/

# Jupyter
.ipynb_checkpoints/

# Environment
.env
.env.local

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Data
*.csv
data/raw/
!data/processed/important.csv
```

Patterns:
- `*.ext` - All files with extension
- `folder/` - Entire folder
- `!file` - Exception (don't ignore this)
- `#` - Comments

### Ignoring Already Tracked Files

```bash
# Stop tracking but keep file
git rm --cached filename

# Update .gitignore
echo "filename" >> .gitignore

# Commit
git commit -m "Stop tracking filename"
```

## Working with Remotes

### git remote

Manage remote repositories.

```bash
# View remotes
git remote

# View remote URLs
git remote -v

# Add a remote
git remote add origin https://github.com/username/repo.git

# Change remote URL
git remote set-url origin https://github.com/username/new-repo.git

# Remove a remote
git remote remove origin

# Rename a remote
git remote rename old-name new-name
```

## Practical Examples

### Example 1: Starting a New Project

```bash
# Initialize
mkdir data-analysis-project
cd data-analysis-project
git init

# Create files
echo "# Data Analysis Project" > README.md
echo "*.csv" > .gitignore

# First commit
git add .
git commit -m "Initial commit: Add README and gitignore"
```

### Example 2: Making Changes

```bash
# Create a new file
echo "import pandas as pd" > analysis.py

# Check status
git status

# Stage and commit
git add analysis.py
git commit -m "Add initial analysis script"

# Make more changes
echo "df = pd.read_csv('data.csv')" >> analysis.py

# View changes
git diff

# Commit
git add analysis.py
git commit -m "Add data loading code"
```

### Example 3: Fixing a Mistake

```bash
# Oops, made a typo
echo "improt pandas" > analysis.py

# Check status
git status

# Discard the mistake
git restore analysis.py

# Or if you already staged it
git add analysis.py
git restore --staged analysis.py
git restore analysis.py
```

## Practice Exercises

Try these exercises in a test repository:

1. Create a new repository
2. Add a README.md file and commit it
3. Create a Python file and commit it
4. Modify the Python file and view the diff
5. Stage and commit the changes
6. View the commit history
7. Create a .gitignore file for Python projects
8. Add and commit the .gitignore file

??? success "Solutions"
    ```bash
    # 1. Create repository
    mkdir git-practice
    cd git-practice
    git init

    # 2. Add README
    echo "# Practice Repository" > README.md
    git add README.md
    git commit -m "Add README"

    # 3. Create and commit Python file
    echo "print('Hello Git')" > hello.py
    git add hello.py
    git commit -m "Add hello script"

    # 4. Modify and view diff
    echo "print('Learning Git')" >> hello.py
    git diff

    # 5. Stage and commit
    git add hello.py
    git commit -m "Add second print statement"

    # 6. View history
    git log --oneline

    # 7. Create .gitignore
    cat > .gitignore << EOF
    *.pyc
    __pycache__/
    .venv/
    EOF

    # 8. Commit .gitignore
    git add .gitignore
    git commit -m "Add Python gitignore"
    ```

## Common Workflows

### Daily Workflow

```bash
# Start of day: Get latest changes
git pull

# Work on files
# ... make changes ...

# Check what changed
git status
git diff

# Stage and commit
git add .
git commit -m "Descriptive message"

# Share your work
git push
```

### Before Going Home

```bash
# Save all work
git add .
git commit -m "WIP: End of day checkpoint"
git push
```

!!! tip "Commit Early, Commit Often"
    Don't wait until you have "perfect" code. Commit logical chunks of work frequently. You can always reorganize commits later if needed.

---

**Previous:** [Introduction](01_introduction.md) | **Next:** [Branching and Merging](03_branching.md)