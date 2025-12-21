# Introduction to Git and GitHub

Learn version control with Git and collaborate with GitHub - essential skills for modern software development and data science.

## What is Git?

Git is a distributed version control system that tracks changes in your code over time. It allows you to:

- **Save snapshots** of your project at different points in time
- **Collaborate** with others without overwriting each other's work
- **Experiment** with new features without breaking working code
- **Revert** to previous versions when things go wrong
- **Track** who made what changes and when

## What is GitHub?

GitHub is a cloud-based hosting service for Git repositories. It provides:

- **Remote storage** for your Git repositories
- **Collaboration tools** (pull requests, issues, discussions)
- **Code review** features
- **Project management** tools
- **CI/CD** integration
- **Portfolio** for showcasing your work

## Why Learn Git?

### For Data Scientists
- Track changes to data analysis notebooks
- Collaborate on machine learning projects
- Version datasets and model configurations
- Share reproducible research
- Manage experiment tracking

### For Developers
- Industry standard for version control
- Required for most tech jobs
- Essential for open-source contribution
- Enables team collaboration
- Facilitates code review processes

## Key Concepts

### Repository (Repo)
A folder that Git tracks. Contains all your project files and the complete history of changes.

### Commit
A snapshot of your project at a specific point in time. Like saving your game progress.

### Branch
An independent line of development. Allows you to work on features without affecting the main code.

### Remote
A version of your repository hosted on the internet (usually on GitHub).

### Clone
Creating a local copy of a remote repository on your computer.

### Push
Uploading your local commits to a remote repository.

### Pull
Downloading changes from a remote repository to your local machine.

## Git vs GitHub

| Git | GitHub |
|-----|--------|
| Version control system | Hosting service for Git repositories |
| Installed on your computer | Cloud-based platform |
| Command-line tool | Web interface + additional features |
| Works offline | Requires internet connection |
| Free and open-source | Free for public repos, paid for advanced features |

## Installing Git

### Windows
1. Download from [git-scm.com](https://git-scm.com/)
2. Run the installer
3. Use default settings (or customize as needed)
4. Verify: Open Git Bash and run `git --version`

### macOS
```bash
# Using Homebrew
brew install git

# Or download from git-scm.com
```

Verify installation:
```bash
git --version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install git
```

Verify installation:
```bash
git --version
```

## Initial Git Configuration

After installing Git, configure your identity:

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email
git config --global user.email "your.email@example.com"

# Check your configuration
git config --list
```

!!! tip "Use Your GitHub Email"
    If you plan to use GitHub, use the same email address you'll use for your GitHub account.

## Creating a GitHub Account

1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Follow the registration process
4. Verify your email address
5. Complete your profile

## Basic Workflow Overview

Here's a typical Git workflow:

```
1. Initialize or clone a repository
   ↓
2. Make changes to files
   ↓
3. Stage changes (git add)
   ↓
4. Commit changes (git commit)
   ↓
5. Push to remote (git push)
   ↓
6. Repeat steps 2-5
```

## Your First Git Repository

Let's create your first Git repository:

```bash
# Create a new folder
mkdir my-first-repo
cd my-first-repo

# Initialize Git
git init

# Check status
git status
```

You should see:
```
Initialized empty Git repository in /path/to/my-first-repo/.git/
```

## Creating Your First Commit

```bash
# Create a file
echo "# My First Repo" > README.md

# Check status
git status

# Stage the file
git add README.md

# Commit
git commit -m "Initial commit: Add README"

# View commit history
git log
```

## Common Git Terms Explained

### Working Directory
The folder on your computer where you're currently working. Contains your actual files.

### Staging Area (Index)
A intermediate area where you prepare files before committing. Think of it as a "preview" of your next commit.

### Local Repository
The `.git` folder in your project that stores all commits and history on your computer.

### Remote Repository
A version of your project hosted on a server (like GitHub).

### HEAD
A pointer to your current branch and commit. Think of it as "you are here."

## Git Workflow Diagram

```
Working Directory  →  Staging Area  →  Local Repository  →  Remote Repository
                   git add          git commit          git push

                   ←                 ←                   ←
                   git restore      git reset           git pull
```

## Best Practices

1. **Commit Often** - Make small, focused commits
2. **Write Clear Messages** - Explain what and why, not how
3. **Pull Before Push** - Always sync before sharing your changes
4. **Use Branches** - Don't work directly on main/master
5. **Review Changes** - Check `git status` and `git diff` before committing
6. **.gitignore** - Don't commit sensitive data or generated files

## What Not to Commit

Never commit:
- Passwords or API keys
- Large binary files (use Git LFS instead)
- Dependencies (node_modules, venv, etc.)
- Personal configuration files
- Temporary files
- Compiled code (unless necessary)

Create a `.gitignore` file to exclude these automatically.

## Getting Help

```bash
# General help
git help

# Help for a specific command
git help commit
git commit --help

# Quick reference
git <command> -h
```

## Resources

- [Official Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Pro Git Book](https://git-scm.com/book/en/v2) (Free online)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

## What's Next?

In the following tutorials, you'll learn:

1. **Basic Git Commands** - add, commit, status, log
2. **Branching and Merging** - Create and manage branches
3. **GitHub Basics** - Push, pull, clone, fork
4. **Collaboration** - Pull requests, code review
5. **Advanced Topics** - Rebase, cherry-pick, stash

!!! success "You're Ready!"
    You now understand the basics of Git and GitHub. Let's dive deeper into the commands and workflows.

---

**Next Tutorial:** [Basic Git Commands](02_basic_commands.md)