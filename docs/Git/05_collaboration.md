# Collaboration Workflows

Learn professional workflows for collaborating with teams using Git and GitHub.

## Git Workflows Overview

Different teams use different workflows based on their needs. Here are the most common:

| Workflow | Best For | Complexity |
|----------|----------|-----------|
| Centralized | Small teams, simple projects | Low |
| Feature Branch | Most teams | Medium |
| Gitflow | Release-based projects | High |
| Forking | Open source | Medium |
| Trunk-based | CI/CD-heavy teams | Low |

## Centralized Workflow

Everyone works on the `main` branch.

### How It Works

```bash
# Morning: Get latest changes
git pull origin main

# Work on features
# ... make changes ...
git add .
git commit -m "Add new feature"

# Share changes
git pull origin main  # Get any new changes
git push origin main
```

### Pros and Cons

**Pros:**
- Simple and straightforward
- Easy to learn
- Good for small teams

**Cons:**
- Risk of breaking main branch
- No isolation for features
- Difficult code review

**Use when:**
- Team size: 1-3 people
- Simple projects
- Rapid prototyping

## Feature Branch Workflow

Each feature gets its own branch.

### How It Works

```bash
# 1. Start from main
git switch main
git pull origin main

# 2. Create feature branch
git switch -c feature-user-profile

# 3. Work on feature
echo "def get_user_profile():" > profile.py
git add profile.py
git commit -m "Add user profile function"

# 4. Push feature branch
git push origin feature-user-profile

# 5. Create pull request on GitHub

# 6. After review and approval, merge
git switch main
git pull origin main
git merge feature-user-profile
git push origin main

# 7. Delete feature branch
git branch -d feature-user-profile
git push origin --delete feature-user-profile
```

### Best Practices

- **One feature per branch**
- **Keep branches short-lived** (days, not weeks)
- **Update from main regularly**
```bash
git switch feature-branch
git merge main  # Or rebase
```
- **Delete merged branches**

### Pros and Cons

**Pros:**
- Features isolated
- Easy code review
- Safe experimentation

**Cons:**
- Slightly more complex
- Merge conflicts possible

**Use when:**
- Most professional projects
- Need code review
- Team size: 3+

## Gitflow Workflow

Structured workflow with multiple long-lived branches.

### Branch Structure

```
main (production)
  ↑
develop (integration)
  ↑
feature/* (new features)
release/* (release prep)
hotfix/* (urgent fixes)
```

### Branch Purposes

- `main` - Production-ready code
- `develop` - Integration branch
- `feature/*` - New features
- `release/*` - Release preparation
- `hotfix/*` - Critical bug fixes

### How It Works

**Starting a feature:**
```bash
# Branch from develop
git switch develop
git pull origin develop
git switch -c feature/user-analytics

# Work on feature
# ... commits ...

# Merge back to develop
git switch develop
git merge feature/user-analytics
git push origin develop
git branch -d feature/user-analytics
```

**Creating a release:**
```bash
# Branch from develop
git switch develop
git switch -c release/1.2.0

# Bug fixes and prep
# ... commits ...

# Merge to main and develop
git switch main
git merge release/1.2.0
git tag -a v1.2.0 -m "Release version 1.2.0"

git switch develop
git merge release/1.2.0

# Cleanup
git branch -d release/1.2.0
```

**Hotfix:**
```bash
# Branch from main
git switch main
git switch -c hotfix/critical-security

# Fix the issue
# ... commits ...

# Merge to both main and develop
git switch main
git merge hotfix/critical-security
git tag -a v1.2.1 -m "Hotfix 1.2.1"

git switch develop
git merge hotfix/critical-security

# Cleanup
git branch -d hotfix/critical-security
```

### Pros and Cons

**Pros:**
- Clear structure
- Supports multiple releases
- Organized release process

**Cons:**
- Complex for beginners
- Overhead for simple projects
- Longer feedback loops

**Use when:**
- Scheduled releases
- Multiple versions supported
- Large teams

## Forking Workflow

Everyone has their own fork of the repository.

### How It Works

**1. Fork the repository on GitHub**

**2. Clone your fork:**
```bash
git clone https://github.com/YOUR-USERNAME/repo.git
cd repo
```

**3. Add upstream remote:**
```bash
git remote add upstream https://github.com/ORIGINAL-OWNER/repo.git
```

**4. Create feature branch:**
```bash
git switch -c feature-new-algorithm
```

**5. Work and commit:**
```bash
# ... make changes ...
git add .
git commit -m "Implement new sorting algorithm"
```

**6. Push to your fork:**
```bash
git push origin feature-new-algorithm
```

**7. Create pull request:**
- From your fork to original repo
- Original maintainers review

**8. Keep fork updated:**
```bash
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

### Pros and Cons

**Pros:**
- Contributors don't need write access
- Perfect for open source
- Maintainers have full control

**Cons:**
- More complex setup
- Fork can get out of sync

**Use when:**
- Open source projects
- External contributors
- No direct write access

## Trunk-Based Development

Everyone commits to main frequently.

### How It Works

```bash
# 1. Pull latest
git pull origin main

# 2. Create short-lived branch
git switch -c quick-fix

# 3. Make small change
# ... one small change ...
git add .
git commit -m "Fix typo in header"

# 4. Merge immediately
git switch main
git pull origin main
git merge quick-fix
git push origin main

# 5. Delete branch
git branch -d quick-fix
```

### Key Principles

- **Very short-lived branches** (hours, not days)
- **Small, frequent commits**
- **Feature flags** for incomplete features
- **Strong CI/CD**
- **Automated testing**

### Feature Flags Example

```python
# Use feature flags for incomplete features
ENABLE_NEW_DASHBOARD = os.getenv('FEATURE_NEW_DASHBOARD', 'false') == 'true'

if ENABLE_NEW_DASHBOARD:
    return render_new_dashboard()
else:
    return render_old_dashboard()
```

### Pros and Cons

**Pros:**
- Fast integration
- Reduced merge conflicts
- Continuous deployment

**Cons:**
- Requires discipline
- Needs strong testing
- Feature flags add complexity

**Use when:**
- Strong CI/CD pipeline
- Experienced team
- Continuous deployment

## Code Review Best Practices

### For Authors

**Before creating PR:**
```bash
# Self-review your changes
git diff main..feature-branch

# Check for common issues
# - Remove debug code
# - Add tests
# - Update documentation
```

**PR Description:**
```markdown
## What
Add email validation to signup form

## Why
Users were entering invalid emails causing 500 errors

## How
- Added regex validation
- Added unit tests
- Updated error messages

## Testing
- [x] Unit tests pass
- [x] Manually tested with 10+ email formats
- [x] Checked error handling

## Screenshots
[Add if UI changes]
```

### For Reviewers

**Review checklist:**
- [ ] Code is understandable
- [ ] Tests included
- [ ] Documentation updated
- [ ] No security issues
- [ ] Follows coding standards
- [ ] Performance considered

**Good review comments:**
```markdown
Good catch on the edge case! 👍

Consider using a constant instead:
\```python
MAX_RETRIES = 3
\```

This could be simplified:
\```python
# Instead of:
if x == True:
    return True
else:
    return False

# Try:
return x
\```
```

### Responding to Reviews

```bash
# Make requested changes
# ... edit files ...

# Commit with descriptive message
git add .
git commit -m "Address review: Add input validation"

# Push to update PR
git push origin feature-branch
```

## Handling Merge Conflicts in Teams

### Minimizing Conflicts

**1. Pull frequently:**
```bash
# Daily or even more often
git switch main
git pull origin main
git switch feature-branch
git merge main
```

**2. Communicate:**
- Announce when working on shared files
- Use draft PRs early
- Break large features into smaller PRs

**3. Keep PRs small:**
- Easier to review
- Less chance of conflicts
- Faster to merge

### Resolving Team Conflicts

**1. Fetch latest:**
```bash
git fetch origin main
```

**2. Try to merge:**
```bash
git merge origin/main
```

**3. If conflicts, communicate:**
```markdown
# In PR or Slack
"Hey @teammate, our changes conflict in auth.py.
Let's hop on a call to resolve together?"
```

**4. Resolve together:**
- Understand both changes
- Decide on best approach
- Test thoroughly

**5. Commit resolution:**
```bash
git add resolved-file.py
git commit -m "Merge main, resolve auth.py conflicts with @teammate"
```

## Team Conventions

### Commit Message Convention

Agree on a format:

```
type(scope): subject

body

footer
```

**Example:**
```
feat(auth): add two-factor authentication

Implement TOTP-based 2FA using pyotp library.
Users can enable in settings.

Closes #234
```

### Branch Naming Convention

```
type/short-description

Examples:
feature/user-dashboard
bugfix/login-redirect
hotfix/security-patch
docs/api-documentation
test/integration-tests
```

### PR Size Guidelines

```
Small:    < 100 lines (ideal)
Medium:   100-300 lines
Large:    300-500 lines
Too big:  > 500 lines (split it!)
```

## Practical Team Scenarios

### Scenario 1: Simultaneous Feature Development

**Developer A:**
```bash
git switch -c feature-payments
# ... work on payments ...
```

**Developer B:**
```bash
git switch -c feature-notifications
# ... work on notifications ...
```

**Both push and create PRs**

**Team lead reviews and merges:**
```bash
# Merge feature-payments
gh pr merge 101

# Merge feature-notifications
gh pr merge 102
```

### Scenario 2: Emergency Hotfix

**Developer on-call:**
```bash
# Pull latest
git switch main
git pull origin main

# Create hotfix branch
git switch -c hotfix/critical-data-leak

# Fix issue
# ... make fix ...
git add .
git commit -m "hotfix: patch data exposure vulnerability"

# Push and create urgent PR
git push origin hotfix/critical-data-leak
gh pr create --title "URGENT: Fix data leak" --assignee @security-team

# After fast review, merge
gh pr merge --squash
```

### Scenario 3: Long-Running Feature

**Week 1:**
```bash
git switch -c feature-ai-recommendations
# ... initial work ...
git push origin feature-ai-recommendations
gh pr create --draft --title "WIP: AI recommendations"
```

**Week 2:**
```bash
# Keep updated with main
git switch feature-ai-recommendations
git fetch origin
git merge origin/main

# Continue work
# ... more commits ...
git push origin feature-ai-recommendations
```

**Week 3:**
```bash
# Mark ready for review
gh pr ready

# After review, merge
gh pr merge feature-ai-recommendations
```

## Tools for Collaboration

### Git Aliases

Add to `~/.gitconfig`:

```ini
[alias]
    co = checkout
    br = branch
    ci = commit
    st = status
    unstage = reset HEAD --
    last = log -1 HEAD
    visual = log --graph --oneline --all
    sync = !git fetch origin && git merge origin/main
```

Usage:
```bash
git st        # instead of git status
git co main   # instead of git checkout main
git visual    # pretty branch visualization
```

### Pre-commit Hooks

Install pre-commit framework:

```bash
pip install pre-commit
```

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
```

Install:
```bash
pre-commit install
```

Now hooks run automatically before each commit!

## Summary: Choosing a Workflow

| Project Type | Recommended Workflow |
|--------------|---------------------|
| Solo project | Centralized or Feature Branch |
| Small team (2-5) | Feature Branch |
| Medium team (5-20) | Feature Branch or Gitflow |
| Large team (20+) | Gitflow |
| Open source | Forking |
| Continuous deployment | Trunk-based |

**Start simple and evolve** - Begin with Feature Branch workflow and adapt as needs grow.

---

**Previous:** [GitHub Basics](04_github.md) | **Next:** [Advanced Git](06_advanced.md)