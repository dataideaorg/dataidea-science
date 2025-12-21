# Branching and Merging

Learn how to use Git branches to work on multiple features simultaneously without conflicts.

## What is a Branch?

A branch is an independent line of development. Think of it as a separate timeline where you can make changes without affecting the main codebase.

### Why Use Branches?

- **Isolate features** - Work on new features without breaking main code
- **Experiment safely** - Try new ideas without risk
- **Parallel development** - Multiple people work simultaneously
- **Organize work** - Separate bug fixes from new features
- **Code review** - Submit changes for review before merging

## Understanding Branches

```
main:     A --- B --- C --- D
                   \
feature:            E --- F
```

- `main` is the default branch (formerly called `master`)
- `feature` branched off from commit `B`
- Changes on `feature` don't affect `main`

## Branch Basics

### Viewing Branches

```bash
# List local branches
git branch

# List all branches (including remote)
git branch -a

# List remote branches only
git branch -r

# Show current branch
git branch --show-current
```

**Example output:**
```
* main
  feature-login
  bugfix-header
```

The `*` indicates your current branch.

### Creating Branches

```bash
# Create a new branch
git branch feature-name

# Create and switch to new branch
git checkout -b feature-name

# Modern alternative (Git 2.23+)
git switch -c feature-name
```

### Switching Branches

```bash
# Switch to existing branch
git checkout branch-name

# Modern alternative
git switch branch-name

# Switch to previous branch
git switch -
```

!!! warning "Clean Working Directory"
    Commit or stash your changes before switching branches to avoid conflicts.

### Deleting Branches

```bash
# Delete a merged branch
git branch -d branch-name

# Force delete (even if not merged)
git branch -D branch-name

# Delete remote branch
git push origin --delete branch-name
```

## Practical Branching Workflow

### Example: Adding a New Feature

```bash
# 1. Make sure you're on main and up-to-date
git switch main
git pull

# 2. Create feature branch
git switch -c feature-user-authentication

# 3. Make changes
echo "def login():" > auth.py
git add auth.py
git commit -m "Add login function"

# 4. More changes
echo "def logout():" >> auth.py
git add auth.py
git commit -m "Add logout function"

# 5. View branch history
git log --oneline --graph
```

## Merging Branches

Merging combines changes from one branch into another.

### Fast-Forward Merge

When no new commits exist on the target branch:

```bash
# Switch to main
git switch main

# Merge feature branch
git merge feature-user-authentication
```

**Before merge:**
```
main:    A --- B
              \
feature:       C --- D
```

**After merge:**
```
main:    A --- B --- C --- D
```

### Three-Way Merge

When both branches have new commits:

```bash
git switch main
git merge feature-user-authentication
```

**Before merge:**
```
main:    A --- B --- E
              \
feature:       C --- D
```

**After merge:**
```
main:    A --- B --- E --- M
              \           /
feature:       C --- D --
```

`M` is a merge commit that combines both histories.

### Merge with Message

```bash
git merge feature-name -m "Merge feature: user authentication"
```

## Handling Merge Conflicts

Conflicts occur when the same lines were changed in both branches.

### Example Conflict

```bash
# Try to merge
git merge feature-branch
```

**Output:**
```
Auto-merging file.py
CONFLICT (content): Merge conflict in file.py
Automatic merge failed; fix conflicts and then commit the result.
```

### Conflict Markers

Git adds conflict markers to the file:

```python
def calculate_total(items):
<<<<<<< HEAD
    return sum(item.price for item in items)
=======
    return sum(item.cost * item.quantity for item in items)
>>>>>>> feature-branch
```

- `<<<<<<< HEAD` - Your current branch changes
- `=======` - Separator
- `>>>>>>> feature-branch` - Incoming branch changes

### Resolving Conflicts

1. **Open the conflicted file**
2. **Choose which changes to keep** (or combine both)
3. **Remove conflict markers**
4. **Stage the resolved file**
5. **Commit the merge**

```bash
# Edit file to resolve conflict
# Remove <<<<<<, =======, >>>>>>> markers

# Stage resolved file
git add file.py

# Complete the merge
git commit -m "Merge feature-branch, resolve pricing conflicts"
```

### Aborting a Merge

If things go wrong:

```bash
# Cancel the merge
git merge --abort
```

## Branch Management Strategies

### Feature Branch Workflow

```bash
# Always branch from main
git switch main
git pull
git switch -c feature-new-chart

# Work on feature
# ... commits ...

# Merge back to main
git switch main
git pull
git merge feature-new-chart
git push

# Delete feature branch
git branch -d feature-new-chart
```

### Hotfix Workflow

For urgent bug fixes:

```bash
# Create hotfix branch from main
git switch main
git switch -c hotfix-login-bug

# Fix the bug
# ... make changes ...
git commit -am "Fix login validation bug"

# Merge to main
git switch main
git merge hotfix-login-bug
git push

# Delete hotfix branch
git branch -d hotfix-login-bug
```

## Viewing Branch Differences

```bash
# See commits in feature not in main
git log main..feature-branch

# See all differences
git diff main..feature-branch

# See file list
git diff --name-only main..feature-branch
```

## Renaming Branches

```bash
# Rename current branch
git branch -m new-name

# Rename a different branch
git branch -m old-name new-name

# Update remote after renaming
git push origin -u new-name
git push origin --delete old-name
```

## Branch Naming Conventions

Good branch names are descriptive and follow a pattern:

**Common patterns:**
```
feature/user-authentication
bugfix/header-alignment
hotfix/critical-security-patch
refactor/database-queries
docs/api-documentation
```

**Examples:**
```
feature/add-dark-mode
bugfix/fix-csv-export
hotfix/security-vulnerability
refactor/optimize-queries
test/add-unit-tests
```

## Advanced Branching

### Listing Merged Branches

```bash
# Branches merged into current branch
git branch --merged

# Branches not yet merged
git branch --no-merged

# Clean up merged branches
git branch --merged | grep -v "main" | xargs git branch -d
```

### Branch from Specific Commit

```bash
# Create branch from a commit
git branch new-branch commit-hash

# Create and switch
git switch -c new-branch commit-hash
```

### Cherry-Pick

Apply a specific commit from one branch to another:

```bash
# Switch to target branch
git switch main

# Cherry-pick a commit
git cherry-pick abc1234
```

## Common Workflows

### Workflow 1: Parallel Feature Development

```bash
# Developer 1: User authentication
git switch -c feature-auth
# ... work and commits ...

# Developer 2: Dashboard UI (simultaneously)
git switch main
git switch -c feature-dashboard
# ... work and commits ...

# Merge both features
git switch main
git merge feature-auth
git merge feature-dashboard
```

### Workflow 2: Experiment and Decide

```bash
# Try approach A
git switch -c experiment-approach-a
# ... code ...

# Try approach B
git switch main
git switch -c experiment-approach-b
# ... code ...

# Approach A was better
git switch main
git merge experiment-approach-a
git branch -D experiment-approach-b
```

## Practical Example

Complete workflow for adding a feature:

```bash
# 1. Start fresh
git switch main
git pull origin main

# 2. Create feature branch
git switch -c feature-data-export

# 3. Implement feature
cat > export.py << EOF
def export_to_csv(data, filename):
    import csv
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
EOF

git add export.py
git commit -m "Add CSV export function"

# 4. Add tests
cat > test_export.py << EOF
def test_export():
    assert export_to_csv([[1,2]], 'test.csv')
EOF

git add test_export.py
git commit -m "Add export tests"

# 5. Update documentation
echo "## Export Feature" >> README.md
git add README.md
git commit -m "Document export feature"

# 6. Merge to main
git switch main
git merge feature-data-export

# 7. Push to remote
git push origin main

# 8. Clean up
git branch -d feature-data-export
```

## Practice Exercises

Try these in a test repository:

1. Create a new branch called `feature-calculator`
2. Add a calculator function and commit
3. Switch back to main
4. Create another branch `feature-display`
5. Add a display function and commit
6. Merge both branches into main
7. Create a conflict by modifying the same line in two branches
8. Resolve the conflict

??? success "Solutions"
    ```bash
    # 1-2. Create and work on feature-calculator
    git switch -c feature-calculator
    echo "def add(a, b): return a + b" > calc.py
    git add calc.py
    git commit -m "Add calculator function"

    # 3-5. Create and work on feature-display
    git switch main
    git switch -c feature-display
    echo "def display(result): print(result)" > display.py
    git add display.py
    git commit -m "Add display function"

    # 6. Merge both
    git switch main
    git merge feature-calculator
    git merge feature-display

    # 7. Create conflict
    git switch -c branch-a
    echo "version = 1" > config.py
    git add config.py
    git commit -m "Set version to 1"

    git switch main
    git switch -c branch-b
    echo "version = 2" > config.py
    git add config.py
    git commit -m "Set version to 2"

    git switch main
    git merge branch-a
    git merge branch-b  # Conflict!

    # 8. Resolve
    # Edit config.py to choose a version
    echo "version = 2" > config.py
    git add config.py
    git commit -m "Resolve version conflict"
    ```

## Tips and Best Practices

1. **Branch often** - Create branches for every feature or bug fix
2. **Keep branches short-lived** - Merge or delete within days, not weeks
3. **Update regularly** - Merge main into your feature branch frequently
4. **Use descriptive names** - `feature-user-login` not `my-branch`
5. **One feature per branch** - Don't mix multiple features
6. **Delete merged branches** - Keep your branch list clean
7. **Review before merging** - Check `git diff` before merging

---

**Previous:** [Basic Commands](02_basic_commands.md) | **Next:** [GitHub Basics](04_github.md)