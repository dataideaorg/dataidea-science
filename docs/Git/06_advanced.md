# Advanced Git Techniques

Master advanced Git commands and techniques for power users.

## Git Rebase

Rebase moves commits to a new base, creating a linear history.

### Basic Rebase

```bash
# Start on feature branch
git switch feature-branch

# Rebase onto main
git rebase main
```

**Before rebase:**
```
main:     A --- B --- C
               \
feature:        D --- E
```

**After rebase:**
```
main:     A --- B --- C
                       \
feature:                D' --- E'
```

Note: `D'` and `E'` are new commits (different hash) with same changes.

### Interactive Rebase

Modify commit history:

```bash
# Rebase last 3 commits
git rebase -i HEAD~3
```

**Editor opens:**
```
pick abc123 Add feature A
pick def456 Fix typo
pick ghi789 Update docs

# Commands:
# p, pick = use commit
# r, reword = change commit message
# e, edit = edit commit
# s, squash = combine with previous commit
# f, fixup = like squash, but discard message
# d, drop = remove commit
```

### Common Rebase Tasks

**1. Squash commits:**
```
pick abc123 Add feature A
squash def456 Fix typo in feature A
squash ghi789 Add tests for feature A
```

Results in one clean commit.

**2. Reword message:**
```
pick abc123 Add feature A
reword def456 Fix typo
pick ghi789 Update docs
```

**3. Reorder commits:**
```
pick ghi789 Update docs
pick abc123 Add feature A
pick def456 Fix typo
```

### Rebase vs Merge

| Aspect | Merge | Rebase |
|--------|-------|--------|
| History | Preserves all history | Creates linear history |
| Commits | Keeps original commits | Creates new commits |
| Use case | Public branches | Private branches |
| Conflicts | Resolved once | May need multiple resolutions |

**Golden Rule:** Never rebase public branches (shared with others)!

## Git Stash

Temporarily save changes without committing.

### Basic Stash

```bash
# Save changes
git stash

# Or with a message
git stash save "Work in progress on login feature"

# List stashes
git stash list

# Apply most recent stash
git stash apply

# Apply and remove from stash list
git stash pop

# Apply specific stash
git stash apply stash@{2}
```

### Stash Options

```bash
# Stash including untracked files
git stash -u

# Stash including ignored files
git stash -a

# Create branch from stash
git stash branch feature-name stash@{0}

# View stash contents
git stash show -p stash@{0}

# Delete a stash
git stash drop stash@{0}

# Clear all stashes
git stash clear
```

### Practical Stash Example

```bash
# Working on feature
echo "def new_feature():" > feature.py

# Urgent bug reported!
git stash save "WIP: new feature implementation"

# Fix bug
git switch main
echo "fix bug" > bugfix.py
git add bugfix.py
git commit -m "Fix critical bug"

# Back to feature
git switch feature-branch
git stash pop

# Continue working
```

## Cherry-Pick

Apply specific commits from one branch to another.

### Basic Cherry-Pick

```bash
# On target branch
git switch main

# Cherry-pick a commit
git cherry-pick abc1234

# Cherry-pick multiple commits
git cherry-pick abc1234 def5678

# Cherry-pick a range
git cherry-pick abc1234..def5678
```

### Cherry-Pick with Edit

```bash
# Cherry-pick but don't commit yet
git cherry-pick -n abc1234

# Make changes
# ... edit files ...

# Commit when ready
git commit -m "Cherry-picked and modified abc1234"
```

### When to Use Cherry-Pick

- **Hotfix to multiple branches**
```bash
# Fix on main
git switch main
git commit -m "Fix security issue"

# Apply to release branch
git switch release-2.0
git cherry-pick main
```

- **Pull single feature from experimental branch**
- **Apply bug fix to older versions**

## Git Reflog

History of all Git operations (safety net).

### Viewing Reflog

```bash
# Show recent operations
git reflog

# Show for specific branch
git reflog show feature-branch

# Show last 10 entries
git reflog -10
```

**Example output:**
```
abc1234 HEAD@{0}: commit: Add new feature
def5678 HEAD@{1}: checkout: moving from main to feature
ghi9012 HEAD@{2}: commit: Fix bug
```

### Recovering Lost Commits

**Scenario:** Accidentally deleted a branch

```bash
# Oops!
git branch -D important-feature

# Find the commit
git reflog

# Output shows:
# abc1234 HEAD@{5}: commit: Important feature complete

# Recover
git switch -c important-feature abc1234
```

### Undoing a Reset

```bash
# Accidentally reset
git reset --hard HEAD~3

# Find previous state
git reflog
# Output: def5678 HEAD@{1}: reset: moving to HEAD~3

# Recover
git reset --hard HEAD@{1}
```

!!! tip "Reflog Expiration"
    Reflog entries expire after 90 days by default. Use it soon after mistakes!

## Git Reset

Move branch pointer and optionally modify working directory.

### Reset Modes

```bash
# Soft: Move HEAD, keep changes staged
git reset --soft HEAD~1

# Mixed (default): Move HEAD, unstage changes
git reset HEAD~1
git reset --mixed HEAD~1

# Hard: Move HEAD, discard all changes
git reset --hard HEAD~1
```

### Visual Comparison

**Before:**
```
A --- B --- C (HEAD)
        Staged: changes.py
        Working: more-changes.py
```

**After `git reset --soft HEAD~1`:**
```
A --- B (HEAD)
    Staged: changes.py, more-changes.py
```

**After `git reset --mixed HEAD~1`:**
```
A --- B (HEAD)
    Working: changes.py, more-changes.py
```

**After `git reset --hard HEAD~1`:**
```
A --- B (HEAD)
    (all changes lost!)
```

### Common Reset Uses

**1. Undo last commit (keep changes):**
```bash
git reset --soft HEAD~1
```

**2. Unstage files:**
```bash
git reset filename.py
```

**3. Discard all changes:**
```bash
git reset --hard HEAD
```

**4. Move to specific commit:**
```bash
git reset --hard abc1234
```

## Git Revert

Create new commits that undo previous commits.

### Basic Revert

```bash
# Revert a commit (creates new commit)
git revert abc1234

# Revert without committing yet
git revert -n abc1234

# Revert a merge commit
git revert -m 1 merge-commit-hash
```

### Reset vs Revert

| Aspect | Reset | Revert |
|--------|-------|--------|
| Changes history | Yes | No |
| Creates commit | No | Yes |
| Safe for public branches | No | Yes |
| Use when | Fixing local mistakes | Undoing public commits |

**Reset:** "This never happened"
**Revert:** "Let's undo that with a new commit"

## Git Bisect

Find which commit introduced a bug using binary search.

### Basic Bisect

```bash
# Start bisect
git bisect start

# Mark current commit as bad
git bisect bad

# Mark last known good commit
git bisect good abc1234

# Git checks out a middle commit
# Test if bug exists

# If bug exists:
git bisect bad

# If bug doesn't exist:
git bisect good

# Repeat until Git finds the culprit

# End bisect
git bisect reset
```

### Automated Bisect

```bash
# Use a test script
git bisect start HEAD abc1234
git bisect run python test.py

# Git automatically finds the bad commit
```

**test.py example:**
```python
import sys

def test_feature():
    # Your test here
    assert feature_works() == True

if __name__ == "__main__":
    try:
        test_feature()
        sys.exit(0)  # Good
    except:
        sys.exit(1)  # Bad
```

## Git Submodules

Include other Git repositories in your project.

### Adding Submodule

```bash
# Add submodule
git submodule add https://github.com/user/repo.git external/repo

# Commit
git add .gitmodules external/repo
git commit -m "Add submodule"
```

### Cloning with Submodules

```bash
# Clone and initialize submodules
git clone --recurse-submodules https://github.com/user/main-repo.git

# Or if already cloned
git submodule init
git submodule update
```

### Updating Submodules

```bash
# Update to latest
git submodule update --remote

# Or update specific submodule
git submodule update --remote external/repo
```

## Git Worktree

Multiple working directories from one repository.

### Basic Worktree

```bash
# Create new worktree
git worktree add ../project-hotfix hotfix-branch

# Now you have two directories:
# ./project (main)
# ../project-hotfix (hotfix-branch)

# Work in hotfix directory
cd ../project-hotfix
# ... make changes ...

# Remove worktree when done
git worktree remove ../project-hotfix
```

### Use Cases

**1. Review PR while continuing work:**
```bash
# Create worktree for PR review
git worktree add ../review-pr-123 pr-123

# Review in separate directory
cd ../review-pr-123

# Continue working in main directory
```

**2. Test different branches simultaneously**

## Git Filter-Branch

Rewrite history (use carefully!).

### Remove File from History

```bash
# Remove sensitive file from all commits
git filter-branch --tree-filter 'rm -f passwords.txt' HEAD

# Better: use BFG Repo Cleaner instead
# https://rtyley.github.io/bfg-repo-cleaner/
```

### Change Author Email

```bash
git filter-branch --env-filter '
if [ "$GIT_AUTHOR_EMAIL" = "old@email.com" ]; then
    export GIT_AUTHOR_EMAIL="new@email.com"
fi
' HEAD
```

!!! danger "Danger Zone"
    Filter-branch rewrites history. Use only when necessary and never on public branches!

## Advanced Git Configuration

### Useful Config Settings

```bash
# Better diffs for Python
git config --global diff.python.xfuncname "^[ \t]*def .*"

# Auto-correct typos
git config --global help.autocorrect 20

# Reuse recorded conflict resolutions
git config --global rerere.enabled true

# Better merge conflict style
git config --global merge.conflictstyle diff3

# Default pull behavior
git config --global pull.rebase true

# Default push behavior
git config --global push.default simple

# Prune on fetch
git config --global fetch.prune true
```

### Git Aliases

```bash
# View pretty log
git config --global alias.lg "log --graph --oneline --all --decorate"

# Undo last commit
git config --global alias.undo "reset --soft HEAD~1"

# Show aliases
git config --global alias.aliases "config --get-regexp ^alias\."

# Quick commit
git config --global alias.cm "commit -m"

# Push with force-with-lease (safer)
git config --global alias.pushf "push --force-with-lease"
```

## Performance Tips

### Shallow Clone

```bash
# Clone only recent history
git clone --depth 1 https://github.com/user/repo.git

# Fetch more history later
git fetch --depth 100
```

### Sparse Checkout

Work with only part of a repository:

```bash
git clone --filter=blob:none --sparse https://github.com/user/repo.git
cd repo
git sparse-checkout init --cone
git sparse-checkout set docs tests
```

### Maintenance

```bash
# Optimize repository
git gc

# Aggressive optimization
git gc --aggressive

# Verify repository integrity
git fsck

# Clean untracked files
git clean -fdx
```

## Best Practices

1. **Never rewrite public history**
2. **Use rebase for local cleanup**
3. **Use merge for integrating features**
4. **Stash for quick context switches**
5. **Cherry-pick sparingly**
6. **Keep commits atomic**
7. **Write descriptive commit messages**

## Emergency Commands

```bash
# Undo almost anything
git reflog
git reset --hard HEAD@{1}

# Recover deleted branch
git reflog
git switch -c recovered-branch abc1234

# Abort operations
git merge --abort
git rebase --abort
git cherry-pick --abort

# Save work quickly
git stash --include-untracked
```

---

**Previous:** [Collaboration Workflows](05_collaboration.md)