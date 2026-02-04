# Copilot CLI Usage Examples

Common usage patterns and real-world examples for GitHub Copilot CLI.

## Basic Usage

### Start Interactive Session

```bash
# Basic interactive mode
copilot

# Start with a specific question
copilot -i "How do I optimize this database query?"

# Interactive with model selection
copilot --model claude-opus-4.5 -i "Design microservices architecture"
```

### Execute Single Command

```bash
# Basic non-interactive
copilot -p "Fix all TypeScript errors in src/" --allow-all

# Silent mode for scripting
copilot -p "Generate API documentation" --allow-all -s > docs.md

# With output saved
copilot -p "Refactor authentication module" --allow-all --share ./refactor-notes.md
```

## Development Tasks

### Bug Fixing

```bash
# Fix specific bug
copilot -p "Fix the null pointer exception in UserService.java line 45" --allow-all

# Fix test failures
copilot -p "Fix all failing tests in the auth module" --allow-all

# Fix linting errors
copilot -p "Fix all ESLint errors in the codebase" --allow-all

# Fix security vulnerability
copilot -p "Fix the SQL injection vulnerability in the login endpoint" --allow-all
```

### Feature Implementation

```bash
# Implement new feature
copilot -p "Implement password reset functionality with email verification" --allow-all

# Add API endpoint
copilot -p "Create a REST API endpoint for user profile updates" --allow-all

# Add UI component
copilot -p "Create a responsive navigation bar component in React" --allow-all

# Implement with tests
copilot -p "Implement shopping cart with add/remove/update and write unit tests" --allow-all
```

### Code Refactoring

```bash
# Refactor for readability
copilot -p "Refactor src/utils/helpers.js to improve readability and reduce complexity" --allow-all

# Extract functions
copilot -p "Extract reusable functions from the UserController class" --allow-all

# Apply design pattern
copilot -p "Refactor data access layer to use Repository pattern" --allow-all

# Modernize code
copilot -p "Convert all var declarations to const/let in JavaScript files" --allow-all
```

### Testing

```bash
# Generate unit tests
copilot -p "Generate unit tests for src/services/PaymentService.ts" --allow-all

# Generate integration tests
copilot -p "Create integration tests for the authentication flow" --allow-all

# Improve test coverage
copilot -p "Add tests to achieve 90% coverage in the user module" --allow-all

# Generate test data
copilot -p "Create realistic test fixtures for the User model" --allow-all
```

### Documentation

```bash
# Generate API docs
copilot -p "Generate OpenAPI/Swagger documentation for all API endpoints" --allow-all -s > api-docs.yaml

# Add code comments
copilot -p "Add JSDoc comments to all functions in src/utils/" --allow-all

# Create README
copilot -p "Create a comprehensive README.md for this project" --allow-all -s > README.md

# Generate changelog
copilot -p "Generate a changelog from git commits for version 2.0" --allow-all -s > CHANGELOG.md
```

## Advanced Workflows

### Database Operations

```bash
# Create migration
copilot -p "Create a database migration to add a 'verified' column to users table" --allow-all

# Generate schema
copilot -p "Generate database schema SQL from the Sequelize models" --allow-all

# Optimize queries
copilot -p "Analyze and optimize slow database queries in the order service" --allow-all

# Seed data
copilot -p "Create database seed scripts with sample data" --allow-all
```

### DevOps and Configuration

```bash
# Create Dockerfile
copilot -p "Create an optimized Dockerfile for this Node.js application" --allow-all

# Generate CI/CD
copilot -p "Create GitHub Actions workflow for testing and deployment" --allow-all

# Environment config
copilot -p "Generate environment configuration files for dev, staging, and production" --allow-all

# Docker Compose
copilot -p "Create docker-compose.yml for running the app with PostgreSQL and Redis" --allow-all
```

### Code Analysis

```bash
# Security audit
copilot -p "Review the codebase for security vulnerabilities" --allow-all

# Performance analysis
copilot -p "Identify performance bottlenecks in the application" --allow-all

# Code quality review
copilot -p "Review code quality and suggest improvements following SOLID principles" --allow-all

# Dependency audit
copilot -p "Analyze dependencies and suggest updates for security and performance" --allow-all
```

### Migration and Conversion

```bash
# Language conversion
copilot -p "Convert JavaScript files in src/ to TypeScript" --allow-all

# Framework migration
copilot -p "Migrate Express routes to Fastify" --allow-all

# API version migration
copilot -p "Migrate from REST API to GraphQL" --allow-all

# Update dependencies
copilot -p "Update React from v16 to v18 and fix breaking changes" --allow-all
```

## Permission Management Examples

### Granular Permissions

```bash
# Allow only file writes
copilot -p "Format all JSON files" --allow-tool write

# Allow git operations
copilot -p "Create feature branch and commit changes" --allow-tool 'shell(git:*)'

# Allow git except push
copilot -p "Implement feature and commit locally" \
  --allow-tool write \
  --allow-tool 'shell(git:*)' \
  --deny-tool 'shell(git push)'

# Allow npm but not install
copilot -p "Run tests" \
  --allow-tool 'shell(npm test)' \
  --allow-tool 'shell(npm run *)'
```

### Path Restrictions

```bash
# Allow specific directories
copilot -p "Refactor code" \
  --add-dir ~/project/src \
  --add-dir ~/project/tests

# Allow current directory only (default)
copilot -p "Fix bugs in current directory" --allow-tool write

# Allow all paths (caution!)
copilot -p "System-wide refactoring" --allow-all-paths
```

### URL Permissions

```bash
# Allow specific APIs
copilot -p "Fetch and analyze API documentation" \
  --allow-url api.github.com \
  --allow-url docs.example.com

# Allow all HTTPS
copilot -p "Research best practices online" --allow-all-urls

# Block specific domains
copilot -p "Research libraries" \
  --allow-all-urls \
  --deny-url untrusted-site.com
```

## Session Management

### Resume Sessions

```bash
# Resume last session
copilot --continue

# Resume with permissions
copilot --continue --allow-all

# Resume specific session
copilot --resume abc123

# Interactive session picker
copilot --resume
```

### Session Documentation

```bash
# Save session to file
copilot -p "Implement feature" --allow-all --share ./session.md

# Share to GitHub gist
copilot -p "Create component" --allow-all --share-gist

# Get gist URL
# Output: Session shared to: https://gist.github.com/...
```

## Model Selection Examples

### Choosing the Right Model

```bash
# Default - general coding tasks
copilot -p "Implement user authentication" --allow-all

# Opus - complex architecture
copilot --model claude-opus-4.5 -p "Design microservices architecture for e-commerce platform" --allow-all

# Haiku - quick fixes
copilot --model claude-haiku-4.5 -p "Fix formatting in config file" --allow-all

# GPT-5 - alternative
copilot --model gpt-5 -p "Implement ML model training pipeline" --allow-all
```

## Automation and Scripting

### CI/CD Integration

```bash
#!/bin/bash
# ci-auto-fix.sh - Auto-fix issues in CI

# Run Copilot to fix test failures
copilot -p "Analyze test failures and fix them" \
  --allow-all \
  --no-ask-user \
  -s > fix-log.txt

# Check if changes were made
if git diff --quiet; then
  echo "No fixes needed"
  exit 0
else
  echo "Fixes applied, creating PR"
  git add .
  git commit -m "ci: auto-fix test failures"
  git push
  gh pr create --title "Auto-fix: Test failures" --body-file fix-log.txt
fi
```

### Scheduled Maintenance

```bash
#!/bin/bash
# weekly-maintenance.sh

# Update dependencies
copilot -p "Update all dependencies to latest compatible versions and fix breaking changes" \
  --allow-all \
  --no-ask-user \
  --share ./dependency-update.md

# Run tests
npm test

# Create PR if successful
if [ $? -eq 0 ]; then
  git add .
  git commit -m "chore: update dependencies"
  git push origin dependency-updates
  gh pr create --title "chore: Weekly dependency updates" --body-file dependency-update.md
fi
```

### Batch Processing

```bash
#!/bin/bash
# batch-refactor.sh

# List of files to refactor
FILES=(
  "src/controllers/UserController.js"
  "src/controllers/ProductController.js"
  "src/controllers/OrderController.js"
)

for file in "${FILES[@]}"; do
  echo "Refactoring $file..."
  
  copilot -p "Refactor $file to use async/await instead of callbacks" \
    --allow-all \
    --no-ask-user
  
  git add "$file"
  git commit -m "refactor: convert $file to async/await"
done

git push
```

## MCP Integration

### GitHub MCP Tools

```bash
# Enable all GitHub tools
copilot --enable-all-github-mcp-tools -p "Create PR for current changes" --allow-all

# Enable specific tools
copilot --add-github-mcp-tool create_pull_request \
        --add-github-mcp-tool list_pull_requests \
        -p "Review open PRs and create new one" \
        --allow-all

# Custom toolset
copilot --add-github-mcp-toolset pull_requests \
        -p "Manage PRs" \
        --allow-all
```

### Custom MCP Servers

```bash
# Load custom MCP config
copilot --additional-mcp-config @~/my-mcp.json -p "Use custom tools" --allow-all

# Multiple configs
copilot --additional-mcp-config @~/mcp1.json \
        --additional-mcp-config @~/mcp2.json \
        -p "Task" --allow-all
```

## Troubleshooting Examples

### Debug Mode

```bash
# Enable debug logging
copilot --log-level debug -p "Implement feature" --allow-all

# Custom log location
copilot --log-dir ./copilot-debug-logs \
        --log-level debug \
        -p "Debug issue" \
        --allow-all
```

### Handling Errors

```bash
#!/bin/bash
# error-handling.sh

# Capture exit code
copilot -p "Fix errors" --allow-all
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
  echo "Success"
elif [ $EXIT_CODE -eq 2 ]; then
  echo "Authentication error - run: copilot login"
  exit 1
elif [ $EXIT_CODE -eq 3 ]; then
  echo "Permission denied - add --allow-all or specific permissions"
  exit 1
else
  echo "Unknown error: $EXIT_CODE"
  exit 1
fi
```

### Retry Logic

```bash
#!/bin/bash
# retry-logic.sh

MAX_RETRIES=3
RETRY_COUNT=0

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
  copilot -p "Implement feature" --allow-all --no-ask-user
  
  if [ $? -eq 0 ]; then
    echo "Success on attempt $((RETRY_COUNT + 1))"
    break
  else
    RETRY_COUNT=$((RETRY_COUNT + 1))
    echo "Attempt $RETRY_COUNT failed, retrying..."
    sleep 5
  fi
done

if [ $RETRY_COUNT -eq $MAX_RETRIES ]; then
  echo "Failed after $MAX_RETRIES attempts"
  exit 1
fi
```

## Interactive Mode Features

### Within Interactive Session

```
# Inside copilot interactive session

> Implement user login
[Agent implements...]

> /share login-implementation.md
Session saved to login-implementation.md

> /model claude-opus-4.5
Switched to claude-opus-4.5

> Now design the overall auth architecture
[Agent provides architecture...]

> /retry
[Agent retries last response with different approach...]

> /clear
Context cleared

> /help
[Shows available commands...]

> /exit
Goodbye!
```

## Custom Instructions

### Project-Specific Instructions

Create `AGENTS.md` in project root:

```markdown
# Project Instructions

This is a TypeScript monorepo using pnpm workspaces.

## Code Standards
- Use functional programming patterns
- Prefer immutability
- Use strict TypeScript (no any types)
- 100% test coverage required

## Workflow
- Always run tests before committing
- Use conventional commits
- Update changelog for features

## Commands
- `pnpm test` - Run all tests
- `pnpm build` - Build all packages
- `pnpm lint` - Run ESLint
```

Then run Copilot normally:

```bash
# Automatically loads AGENTS.md
copilot -p "Implement new feature" --allow-all

# Disable custom instructions
copilot --no-custom-instructions -p "Implement feature" --allow-all
```

## Real-World Complete Examples

### Example 1: Full-Stack Feature

```bash
# Implement complete feature: backend + frontend + tests + docs

copilot -p "Implement user notification system:

Backend (Node.js/Express):
- POST /api/notifications - Create notification
- GET /api/notifications - List user notifications
- PATCH /api/notifications/:id - Mark as read
- Database: Add notifications table
- Real-time: WebSocket support

Frontend (React):
- Notification bell icon with count
- Dropdown list of notifications
- Mark as read functionality
- Real-time updates

Tests:
- Backend unit tests
- Backend integration tests
- Frontend component tests
- E2E tests for notification flow

Documentation:
- API documentation
- Component documentation
- Setup instructions" \
  --allow-all \
  --share ./notification-feature.md

# Review, commit, and create PR
git add .
git commit -m "feat: implement user notification system"
git push
gh pr create --body-file notification-feature.md
```

### Example 2: Automated Code Review

```bash
# Review PR before merging

copilot -p "Review the code changes in the current branch:

Checks:
- Code quality and maintainability
- Security vulnerabilities
- Performance issues
- Test coverage
- Documentation completeness
- Breaking changes

Provide:
- Summary of changes
- Issues found (severity: critical/high/medium/low)
- Recommendations
- Approval status (approve/request changes)" \
  --allow-all \
  -s > code-review.md

cat code-review.md
```

### Example 3: Codebase Migration

```bash
# Migrate from JavaScript to TypeScript

copilot -p "Migrate the codebase from JavaScript to TypeScript:

Steps:
1. Add TypeScript configuration (tsconfig.json)
2. Install type definitions for dependencies
3. Convert .js files to .ts (one module at a time)
4. Add type annotations
5. Fix type errors
6. Update build scripts
7. Update documentation

Preserve:
- Existing functionality
- Git history
- Tests (convert to TypeScript)

Ensure:
- Strict TypeScript mode
- No 'any' types (use proper types)
- All tests passing" \
  --allow-all \
  --model claude-opus-4.5 \
  --share ./typescript-migration.md
```

## Tips and Best Practices

### 1. Be Specific in Prompts

```bash
# ❌ Vague
copilot -p "Make it better" --allow-all

# ✅ Specific
copilot -p "Refactor UserService class to use dependency injection, improve error handling, and add input validation" --allow-all
```

### 2. Use Silent Mode for Scripting

```bash
# Perfect for parsing output
RESULT=$(copilot -p "Generate config JSON" --allow-all -s)
echo "$RESULT" | jq . > config.json
```

### 3. Chain Commands in Scripts

```bash
#!/bin/bash

# Step 1: Implementation
copilot -p "Implement feature" --allow-all --share ./impl.md

# Step 2: Tests
copilot -p "Add tests for the implemented feature" --allow-all

# Step 3: Docs
copilot -p "Generate documentation" --allow-all -s > DOCS.md

# Step 4: PR
gh pr create --body-file impl.md
```

### 4. Combine with Other Tools

```bash
# Copilot + GitHub CLI
copilot -p "Fix issues" --allow-all && gh pr create

# Copilot + jq
copilot -p "Generate package.json" --allow-all -s | jq .

# Copilot + Docker
copilot -p "Create Dockerfile" --allow-all && docker build .
```
