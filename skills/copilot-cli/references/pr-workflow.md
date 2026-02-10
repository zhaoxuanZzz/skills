# Automated Pull Request Workflows

This guide demonstrates how to use GitHub Copilot CLI to autonomously implement features and create pull requests.

## Complete PR Workflow Overview

```
1. Feature Implementation
   ↓
2. Session Documentation
   ↓
3. PR Creation (via GitHub CLI/MCP)
   ↓
4. Code Review (Optional)
   ↓
5. Merge
```

## Workflow 1: Manual PR Creation

Use Copilot CLI for implementation, then manually create PR.

### Step 1: Create Feature Branch

```bash
# Create and switch to feature branch
git checkout -b feature/user-authentication

# Or from specific branch
git checkout -b feature/auth main
```

### Step 2: Implement with Copilot CLI

Execute the implementation in non-interactive mode:

```bash
copilot -p "Implement user authentication with JWT tokens. Include:
- Login endpoint with email/password
- Token generation and validation
- Protected route middleware
- Unit tests for auth service
- Integration tests for endpoints" \
  --allow-all \
  --share ./implementation-notes.md
```

**Why these flags:**
- `--allow-all`: Grants all permissions for autonomous work
- `--share`: Saves session documentation for PR description

**Expected output:**
- Code implementation completed
- Tests written and passing
- Session saved to `implementation-notes.md`

### Step 3: Review Changes

```bash
# Check what was changed
git status
git diff

# Review implementation notes
cat implementation-notes.md
```

### Step 4: Commit Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: implement JWT-based user authentication

- Add login endpoint with email/password validation
- Implement JWT token generation and validation
- Create protected route middleware
- Add comprehensive unit and integration tests"
```

### Step 5: Push and Create PR

```bash
# Push feature branch
git push origin feature/user-authentication

# Create PR using GitHub CLI
gh pr create \
  --title "feat: Implement JWT-based user authentication" \
  --body-file implementation-notes.md \
  --base main
```

**Alternative: Manual PR creation**
- Push branch: `git push origin feature/user-authentication`
- Visit GitHub repository
- Click "Compare & pull request"
- Use content from `implementation-notes.md` for description

## Workflow 2: Fully Automated PR with GitHub MCP Tools

Use Copilot CLI with GitHub MCP tools for complete automation.

### Prerequisites

Enable GitHub MCP tools:

```bash
# Enable all GitHub MCP tools
copilot --enable-all-github-mcp-tools

# Or enable specific tools
copilot --add-github-mcp-tool create_pull_request \
        --add-github-mcp-tool create_branch
```

### Complete Automated Workflow

Single command for everything:

```bash
copilot -p "Create a new feature branch 'feature/user-profile', implement user profile functionality with CRUD operations and tests, commit the changes, and create a pull request with detailed description" \
  --allow-all \
  --enable-all-github-mcp-tools \
  --no-ask-user
```

**What happens:**
1. Copilot creates the feature branch via GitHub API
2. Implements the feature code
3. Commits changes
4. Creates pull request with description
5. All autonomous, no user intervention

## Workflow 3: CI/CD Integration

Automated PR creation triggered by events (issues, schedules, webhooks).

### Example: Issue-to-PR Automation

When an issue is labeled "copilot-auto":

```bash
#!/bin/bash
# Triggered by GitHub Actions on issue label

ISSUE_NUMBER=$1
ISSUE_TITLE=$(gh issue view $ISSUE_NUMBER --json title -q .title)
ISSUE_BODY=$(gh issue view $ISSUE_NUMBER --json body -q .body)

# Create feature branch name from issue
BRANCH_NAME="feature/issue-${ISSUE_NUMBER}"

# Checkout new branch
git checkout -b "$BRANCH_NAME"

# Run Copilot CLI to implement
copilot -p "Implement the following feature from issue #${ISSUE_NUMBER}:

Title: ${ISSUE_TITLE}

Description:
${ISSUE_BODY}

Requirements:
- Implement all functionality described
- Write comprehensive tests
- Follow project coding standards
- Update documentation if needed" \
  --allow-all \
  --no-ask-user \
  -s > implementation-log.txt

# Check if changes were made
if ! git diff --quiet; then
  # Commit changes
  git add .
  git commit -m "feat: ${ISSUE_TITLE} (#${ISSUE_NUMBER})"
  
  # Push branch
  git push origin "$BRANCH_NAME"
  
  # Create PR
  gh pr create \
    --title "feat: ${ISSUE_TITLE}" \
    --body "Implements #${ISSUE_NUMBER}

## Implementation
$(cat implementation-log.txt)

Closes #${ISSUE_NUMBER}" \
    --base main
  
  echo "PR created successfully"
else
  echo "No changes made"
  git checkout main
  git branch -D "$BRANCH_NAME"
fi
```

### GitHub Actions Workflow

`.github/workflows/copilot-auto-implement.yml`:

```yaml
name: Copilot Auto Implement

on:
  issues:
    types: [labeled]

jobs:
  auto-implement:
    if: github.event.label.name == 'copilot-auto'
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Copilot CLI
        run: |
          # Install Copilot CLI
          curl -fsSL https://cli.github.com/copilot/install.sh | bash
          
      - name: Authenticate
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          copilot login
          
      - name: Implement Feature
        env:
          ISSUE_NUMBER: ${{ github.event.issue.number }}
        run: |
          bash .github/scripts/auto-implement.sh $ISSUE_NUMBER
```

## Workflow 4: Incremental Development

For large features, use sessions to maintain context across multiple commits.

### Day 1: Start Feature

```bash
# Start implementation
copilot -i "Implement user authentication system. Start with the database schema and models." \
  --allow-all

# Session runs, implementation done
# Agent asks if ready to continue or save
# Save session ID for later
```

### Day 2: Continue Implementation

```bash
# Resume previous session
copilot --continue \
  --allow-all

# Or resume specific session
copilot --resume abc123def456 \
  --allow-all

# Continue: "Now implement the API endpoints"
```

### Day 3: Finalize and Create PR

```bash
# Resume and complete
copilot --resume abc123def456 \
  -i "Finalize authentication system: add tests, documentation, and create PR" \
  --allow-all \
  --enable-all-github-mcp-tools
```

## Workflow 5: Batch PR Creation

Create multiple PRs for different features:

```bash
#!/bin/bash
# batch-implement.sh

FEATURES=(
  "Add user profile page"
  "Implement search functionality"
  "Add export to CSV feature"
  "Create admin dashboard"
)

for feature in "${FEATURES[@]}"; do
  # Generate branch name
  BRANCH=$(echo "$feature" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
  
  # Create branch
  git checkout -b "feature/$BRANCH" main
  
  # Implement with Copilot
  copilot -p "Implement: $feature. Include tests and documentation." \
    --allow-all \
    --share "./pr-notes-$BRANCH.md"
  
  # Commit and push
  git add .
  git commit -m "feat: $feature"
  git push origin "feature/$BRANCH"
  
  # Create PR
  gh pr create \
    --title "feat: $feature" \
    --body-file "./pr-notes-$BRANCH.md" \
    --base main
  
  # Return to main
  git checkout main
  
  echo "✓ PR created for: $feature"
done
```

Run batch implementation:

```bash
chmod +x batch-implement.sh
./batch-implement.sh
```

## Best Practices for PR Workflows

### 1. Clear, Specific Prompts

❌ Bad:
```bash
copilot -p "Add authentication" --allow-all
```

✅ Good:
```bash
copilot -p "Implement JWT-based authentication with:
- Login endpoint (POST /auth/login) with email/password
- Token validation middleware
- Refresh token mechanism
- Unit tests for token generation/validation
- Integration tests for protected endpoints
Follow RESTful best practices and project coding standards." \
  --allow-all
```

### 2. Use --share for Documentation

Always save session documentation for PR descriptions:

```bash
copilot -p "..." --allow-all --share ./pr-description.md
```

Then use as PR body:

```bash
gh pr create --body-file pr-description.md
```

### 3. Review Before Pushing

Even with automation, review changes:

```bash
# After Copilot implementation
git diff
git status

# Run tests
npm test  # or your test command

# Then commit and push
```

### 4. Atomic PRs

One feature per PR:

```bash
# ❌ Too broad
copilot -p "Implement entire authentication and authorization system" --allow-all

# ✅ Focused
copilot -p "Implement JWT authentication for login endpoint" --allow-all
# Later: Separate PR for role-based authorization
```

### 5. Descriptive Branch Names

Follow conventions:

```bash
feature/user-authentication
bugfix/login-validation
refactor/auth-middleware
docs/api-documentation
```

### 6. Auto-merge for Trusted Workflows

For CI/CD, auto-merge after tests pass:

```bash
gh pr create \
  --title "..." \
  --body-file notes.md \
  --base main

# Enable auto-merge
gh pr merge --auto --squash
```

### 7. Error Handling in Scripts

```bash
#!/bin/bash
set -e  # Exit on error

# Implement feature
if copilot -p "Implement feature" --allow-all --share ./notes.md; then
  echo "Implementation successful"
else
  echo "Implementation failed with exit code $?"
  exit 1
fi

# Only create PR if changes exist
if ! git diff --quiet; then
  git add .
  git commit -m "feat: implementation"
  git push origin feature-branch
  gh pr create --body-file notes.md
else
  echo "No changes to commit"
  exit 0
fi
```

## Security Considerations

### 1. Limit Permissions in Production

```bash
# ❌ Too permissive for production
copilot -p "..." --allow-all

# ✅ Minimal permissions
copilot -p "..." \
  --allow-tool write \
  --allow-tool 'shell(git:*)' \
  --deny-tool 'shell(git push)' \
  --add-dir ~/workspace/safe-dir
```

### 2. Review Before Auto-merge

Never auto-merge without CI checks:

```yaml
# .github/workflows/pr-checks.yml
on: pull_request

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm test
      - run: npm run lint
      - run: npm run security-scan
```

### 3. Use Branch Protection

Require reviews even for automated PRs:

```bash
# GitHub branch protection settings
- Require pull request reviews before merging
- Require status checks to pass
- Require branches to be up to date
```

## Troubleshooting

### PR Creation Fails

```bash
# Check GitHub CLI auth
gh auth status

# Re-authenticate if needed
gh auth login

# Check permissions
gh pr create --help
```

### Copilot Changes Not Committed

```bash
# Check git status
git status

# Ensure --allow-tool write was granted
copilot -p "..." --allow-tool write

# Or use --allow-all
copilot -p "..." --allow-all
```

### Session Resume Issues

```bash
# List available sessions
copilot --resume

# If session ID lost, check recent sessions
ls ~/.copilot/sessions/

# Resume by ID
copilot --resume <session-id>
```

## Example: Complete Real-World Workflow

Task: Implement a new API endpoint with tests and documentation.

```bash
#!/bin/bash
# implement-api-endpoint.sh

# Configuration
FEATURE_NAME="user-settings-endpoint"
BRANCH_NAME="feature/$FEATURE_NAME"

echo "🚀 Starting implementation: $FEATURE_NAME"

# 1. Create branch
git checkout -b "$BRANCH_NAME" main
echo "✓ Branch created: $BRANCH_NAME"

# 2. Implement with Copilot
echo "🤖 Running Copilot implementation..."
copilot -p "Implement a RESTful API endpoint for user settings:

Path: GET /api/users/:userId/settings
       PUT /api/users/:userId/settings

Requirements:
- GET returns user settings as JSON
- PUT updates settings with validation
- Include authentication middleware
- Add input validation
- Write unit tests (>80% coverage)
- Write API documentation in OpenAPI format
- Follow project coding standards

Database: Use existing User model, add settings field if needed" \
  --allow-all \
  --no-ask-user \
  --share ./implementation-notes.md

echo "✓ Implementation complete"

# 3. Run tests
echo "🧪 Running tests..."
npm test

# 4. Review changes
echo "📝 Changes made:"
git status --short

# 5. Commit
echo "💾 Committing changes..."
git add .
git commit -m "feat: add user settings API endpoint

- Implement GET /api/users/:userId/settings
- Implement PUT /api/users/:userId/settings
- Add authentication and validation middleware
- Add comprehensive unit tests
- Add OpenAPI documentation"

# 6. Push
echo "⬆️  Pushing to remote..."
git push origin "$BRANCH_NAME"

# 7. Create PR
echo "🔀 Creating pull request..."
gh pr create \
  --title "feat: Add user settings API endpoint" \
  --body-file implementation-notes.md \
  --base main \
  --label "enhancement" \
  --label "api"

echo "✅ Workflow complete! PR created."

# 8. Get PR URL
PR_URL=$(gh pr view --json url -q .url)
echo "🔗 PR URL: $PR_URL"
```

Execute:

```bash
chmod +x implement-api-endpoint.sh
./implement-api-endpoint.sh
```

This produces:
- Feature branch
- Complete implementation with tests
- Committed and pushed code
- Pull request with detailed description
- All autonomous, minimal intervention
