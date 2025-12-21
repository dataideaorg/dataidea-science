# GitHub Basics

Learn how to use GitHub to host your code, collaborate with others, and showcase your projects.

## Connecting to GitHub

### Creating a Repository on GitHub

1. Go to [github.com](https://github.com) and sign in
2. Click the **+** icon → **New repository**
3. Fill in repository details:
   - **Name:** `my-awesome-project`
   - **Description:** Brief description
   - **Public** or **Private**
   - Initialize with README (optional)
4. Click **Create repository**

### Connecting Local Repository to GitHub

#### Option 1: Push an Existing Repository

```bash
# Add GitHub as remote
git remote add origin https://github.com/username/repo-name.git

# Push to GitHub
git push -u origin main
```

#### Option 2: Clone from GitHub

```bash
# Clone the repository
git clone https://github.com/username/repo-name.git

# Navigate into it
cd repo-name

# Start working
```

### SSH vs HTTPS

**HTTPS URL:**
```
https://github.com/username/repo-name.git
```

**SSH URL:**
```
git@github.com:username/repo-name.git
```

**Setting up SSH:**

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub:
# Settings → SSH and GPG keys → New SSH key
```

**Change remote to SSH:**
```bash
git remote set-url origin git@github.com:username/repo-name.git
```

## Basic GitHub Workflow

### Pushing Changes

```bash
# Make changes locally
echo "New feature" >> feature.py
git add feature.py
git commit -m "Add new feature"

# Push to GitHub
git push origin main
```

### Pulling Changes

```bash
# Get latest changes from GitHub
git pull origin main

# Or in two steps
git fetch origin
git merge origin/main
```

### Fetching vs Pulling

| Command | What it does |
|---------|-------------|
| `git fetch` | Downloads changes but doesn't merge them |
| `git pull` | Downloads and merges changes (fetch + merge) |

```bash
# Fetch only
git fetch origin

# See what changed
git log origin/main

# Merge when ready
git merge origin/main
```

## Forking Repositories

A fork is your personal copy of someone else's repository.

### How to Fork

1. Go to the repository you want to fork
2. Click **Fork** button (top right)
3. Choose your account
4. Clone your fork:

```bash
git clone https://github.com/YOUR-USERNAME/repo-name.git
```

### Keeping Fork Updated

```bash
# Add original repo as upstream
git remote add upstream https://github.com/ORIGINAL-OWNER/repo-name.git

# Fetch upstream changes
git fetch upstream

# Merge into your main
git checkout main
git merge upstream/main

# Push to your fork
git push origin main
```

## Pull Requests (PRs)

Pull requests let you propose changes to a repository.

### Creating a Pull Request

**Step 1: Create a feature branch**
```bash
git switch -c feature-add-validation
```

**Step 2: Make changes and push**
```bash
# Make changes
echo "def validate_email(email):" > validation.py
git add validation.py
git commit -m "Add email validation function"

# Push branch to GitHub
git push origin feature-add-validation
```

**Step 3: Open PR on GitHub**
1. Go to your repository on GitHub
2. Click **Pull requests** → **New pull request**
3. Select your feature branch
4. Add title and description
5. Click **Create pull request**

### PR Description Template

```markdown
## What does this PR do?
Brief description of changes

## Why is this needed?
Explain the problem this solves

## How was it tested?
- [ ] Unit tests added
- [ ] Manual testing completed

## Screenshots (if applicable)
[Add screenshots]

## Related Issues
Fixes #123
```

### Reviewing Pull Requests

```bash
# Fetch PR locally to test
git fetch origin pull/123/head:pr-123
git switch pr-123

# Test the changes
python test.py

# Switch back
git switch main
```

### Merging Pull Requests

On GitHub, you can merge PRs in three ways:

1. **Merge commit** - Preserves all commits and creates merge commit
2. **Squash and merge** - Combines all commits into one
3. **Rebase and merge** - Applies commits individually without merge commit

## GitHub Issues

Issues track bugs, features, and tasks.

### Creating an Issue

1. Go to repository → **Issues** → **New issue**
2. Add title and description
3. Assign labels (bug, enhancement, documentation)
4. Assign people or milestones
5. Click **Submit new issue**

### Issue Template Example

```markdown
## Bug Report

**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What should happen instead?

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g. macOS 13]
- Python version: [e.g. 3.10]
- Package version: [e.g. 1.2.3]
```

### Referencing Issues

In commits and PRs:

```bash
# Reference issue
git commit -m "Add validation, addresses #45"

# Close issue automatically
git commit -m "Fix login bug, closes #45"
git commit -m "Resolve #45"
```

## GitHub Actions (CI/CD)

Automate testing, building, and deployment.

### Simple Python Test Workflow

Create `.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest

    - name: Run tests
      run: pytest tests/
```

This automatically runs tests on every push and PR.

## README Best Practices

A good README includes:

```markdown
# Project Name

Brief description of what this project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

\```bash
pip install package-name
\```

## Usage

\```python
from package import function

result = function()
\```

## Examples

[Link to examples folder]

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License - see [LICENSE](LICENSE)

## Contact

Your Name - [@twitter](https://twitter.com/handle)
Project Link: https://github.com/username/repo
```

### Badges

Add status badges to your README:

```markdown
![Tests](https://github.com/username/repo/workflows/Tests/badge.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
```

## GitHub Pages

Host websites directly from your repository.

### Quick Setup

1. Go to repository **Settings** → **Pages**
2. Select source: `main` branch, `/docs` folder
3. Save
4. Your site will be at: `https://username.github.io/repo-name`

### Example: Project Documentation

Create `docs/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Project</title>
</head>
<body>
    <h1>Welcome to My Project</h1>
    <p>Documentation goes here</p>
</body>
</html>
```

Push and it's live!

## Releases and Tags

### Creating a Release

**1. Tag a version:**
```bash
git tag -a v1.0.0 -m "First release"
git push origin v1.0.0
```

**2. Create release on GitHub:**
1. Go to **Releases** → **Draft a new release**
2. Choose tag `v1.0.0`
3. Add release notes
4. Attach binaries if needed
5. Click **Publish release**

### Semantic Versioning

Use `MAJOR.MINOR.PATCH` format:

- `MAJOR` - Breaking changes (v2.0.0)
- `MINOR` - New features (v1.1.0)
- `PATCH` - Bug fixes (v1.0.1)

Examples:
- `v1.0.0` - Initial release
- `v1.0.1` - Bug fix
- `v1.1.0` - New feature
- `v2.0.0` - Breaking changes

## GitHub Repository Settings

### Protecting Branches

1. **Settings** → **Branches** → **Add rule**
2. Branch name pattern: `main`
3. Enable:
   - ✅ Require pull request reviews
   - ✅ Require status checks to pass
   - ✅ Require branches to be up to date

### Collaborators

**Add collaborators:**
1. **Settings** → **Collaborators**
2. Click **Add people**
3. Enter GitHub username
4. Choose permission level

### .gitignore Templates

GitHub provides templates when creating repos:

- Python
- Node
- Java
- Ruby
- etc.

Or use [gitignore.io](https://gitignore.io)

## GitHub CLI

Command-line tool for GitHub operations.

### Installation

**macOS:**
```bash
brew install gh
```

**Windows:**
```bash
winget install GitHub.cli
```

**Linux:**
```bash
sudo apt install gh
```

### Authentication

```bash
gh auth login
```

### Common Commands

```bash
# Create repo
gh repo create my-project --public

# Clone repo
gh repo clone username/repo

# Create issue
gh issue create --title "Bug report" --body "Description"

# Create PR
gh pr create --title "Add feature" --body "Description"

# View PR
gh pr view 123

# List PRs
gh pr list

# Check PR status
gh pr status

# Merge PR
gh pr merge 123
```

## Practical Examples

### Example 1: Contributing to Open Source

```bash
# 1. Fork repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/repo-name.git
cd repo-name

# 3. Add upstream remote
git remote add upstream https://github.com/ORIGINAL-OWNER/repo-name.git

# 4. Create feature branch
git switch -c fix-typo-in-readme

# 5. Make changes
# ... edit files ...

# 6. Commit and push
git add README.md
git commit -m "Fix typo in installation instructions"
git push origin fix-typo-in-readme

# 7. Create PR on GitHub
gh pr create --title "Fix README typo" --body "Fixed typo in installation section"
```

### Example 2: Team Collaboration

```bash
# 1. Clone team repository
git clone https://github.com/team/project.git
cd project

# 2. Create feature branch
git switch -c feature-user-dashboard

# 3. Work and commit regularly
git add dashboard.py
git commit -m "Add dashboard layout"

# 4. Push to get feedback
git push origin feature-user-dashboard

# 5. Create draft PR
gh pr create --draft --title "WIP: User dashboard"

# 6. Continue working
# ... more commits ...

# 7. Mark as ready for review
gh pr ready 123

# 8. After approval, merge
gh pr merge 123
```

## Best Practices

### Commit Messages

Follow conventions:
```
type(scope): subject

body

footer
```

Types:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Formatting
- `refactor:` Code restructuring
- `test:` Tests
- `chore:` Maintenance

Example:
```
feat(auth): add password reset functionality

Implement password reset via email with token expiration.
Users can request a reset link that expires after 1 hour.

Closes #45
```

### Project Organization

```
my-project/
├── .github/
│   └── workflows/
│       └── tests.yml
├── docs/
│   └── index.md
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

### Security

**Never commit:**
- API keys
- Passwords
- Private keys
- Database credentials

Use:
- Environment variables
- `.env` files (in `.gitignore`)
- GitHub Secrets (for Actions)

---

**Previous:** [Branching and Merging](03_branching.md) | **Next:** [Collaboration Workflows](05_collaboration.md)