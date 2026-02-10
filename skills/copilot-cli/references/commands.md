# Copilot CLI Commands Reference

This document provides detailed information about all GitHub Copilot CLI commands.

## Main Commands

### login

Authenticate with GitHub Copilot via OAuth device flow.

```bash
copilot login [options]
```

**When to use:**
- First-time setup
- Re-authentication after token expiration
- Switching GitHub accounts

**Example:**
```bash
copilot login
```

### init

Initialize Copilot instructions for the current repository.

```bash
copilot init
```

**What it does:**
- Creates `.copilot/AGENTS.md` or `AGENTS.md` in the repository
- Allows you to define custom instructions for this project
- Instructions are automatically loaded when running Copilot in this directory

**When to use:**
- Setting up project-specific guidelines
- Defining coding standards for a team
- Creating custom workflows for a repository

**Example:**
```bash
cd ~/my-project
copilot init
# Edit AGENTS.md with project-specific instructions
```

### update

Download and install the latest version of Copilot CLI.

```bash
copilot update
```

**When to use:**
- Manually updating to the latest version
- When auto-update is disabled

**Note:** Auto-update is enabled by default. Use `--no-auto-update` to disable.

### version

Display version information and check for available updates.

```bash
copilot version
```

**Output includes:**
- Current CLI version
- Update availability status
- Installation path

### help

Display help information for Copilot CLI or specific topics.

```bash
copilot help [topic]
```

**Available topics:**
- `config` - Configuration settings
- `commands` - Interactive mode commands
- `environment` - Environment variables
- `logging` - Logging configuration
- `permissions` - Permission system details

**Examples:**
```bash
copilot help
copilot help config
copilot help permissions
```

### plugin

Manage plugins and plugin marketplaces.

```bash
copilot plugin [subcommand]
```

**Note:** Plugin system allows extending Copilot CLI with additional functionality. See plugin documentation for details.

## Interactive Mode Commands

When inside an interactive Copilot session, the following slash commands are available:

### /help

Display available interactive commands.

### /share

Share the current session to a markdown file or GitHub gist.

```
/share [path]
/share gist
```

### /clear

Clear the current conversation context while remaining in the session.

### /exit or /quit

Exit the interactive session.

### /model

Switch the AI model during an interactive session.

```
/model claude-sonnet-4.5
/model gpt-5
```

### /retry

Retry the last agent response with a different approach.

## Command Execution Modes

### Interactive Mode

Start a persistent conversation session:

```bash
# Basic interactive
copilot

# Start with a prompt
copilot -i "Fix the authentication bug"

# Interactive with specific model
copilot --model claude-opus-4.5 -i "Design the new API architecture"
```

**Characteristics:**
- Maintains conversation context
- Allows multiple back-and-forth interactions
- Can resume later
- Supports slash commands
- Ideal for exploration and complex tasks

### Non-Interactive Mode

Execute a single prompt and exit:

```bash
copilot -p "Fix the bug in main.js" --allow-all-tools
```

**Characteristics:**
- Single execution, then exits
- Returns exit code (0 = success, non-zero = failure)
- Perfect for automation and scripting
- Requires explicit permission grants
- Can save output with `--share`

### Session Resume

Continue a previous session:

```bash
# Resume most recent
copilot --continue

# Resume with picker
copilot --resume

# Resume specific session
copilot --resume <session-id>
```

**Characteristics:**
- Restores full conversation context
- Continues from last message
- Maintains permissions from original session (unless overridden)

## Command-Line Execution Flow

1. **Authentication Check**: Verifies GitHub Copilot access
2. **Permission Setup**: Applies --allow-*, --deny-* flags
3. **Custom Instructions**: Loads AGENTS.md if present and not disabled
4. **Model Initialization**: Loads specified model (or default)
5. **MCP Server Setup**: Initializes enabled MCP servers
6. **Execution**: Runs prompt or starts interactive session
7. **Cleanup**: Saves session, logs, shares output if requested

## Exit Codes

- `0`: Success
- `1`: General error
- `2`: Authentication error
- `3`: Permission denied
- `4`: Invalid arguments
- `130`: User interrupt (Ctrl+C)

Use exit codes for error handling in scripts:

```bash
if copilot -p "Run tests" --allow-all; then
    echo "Tests passed"
else
    echo "Tests failed with code $?"
fi
```

## Environment Integration

### Working Directory

Copilot CLI uses the current working directory as context:

```bash
cd ~/my-project
copilot -p "Fix all TypeScript errors" --allow-all
```

### Git Integration

Automatically detects:
- Current branch
- Repository status
- Recent commits
- Staged/unstaged changes

Use this for branch-aware operations:

```bash
git checkout -b feature/new-auth
copilot -p "Implement OAuth2 authentication" --allow-all
```

### Custom Instructions

Place `AGENTS.md` or `.copilot/AGENTS.md` in your repository:

```markdown
# Project Instructions

This is a TypeScript project using React and Node.js.

## Code Standards
- Use functional components with hooks
- Prefer async/await over promises
- Write tests for all features

## Development Workflow
- Create feature branches from main
- Write tests before implementation
- Run linter before committing
```

Copilot will automatically apply these instructions in this directory.
