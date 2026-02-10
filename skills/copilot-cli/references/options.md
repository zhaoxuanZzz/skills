# Copilot CLI Options Reference

Complete reference for all command-line options and flags.

## Core Options

### -p, --prompt

Execute a prompt in non-interactive mode (exits after completion).

```bash
copilot -p "Fix the bug in main.js" --allow-all-tools
```

**Type:** String  
**Mode:** Non-interactive  
**Requires:** Permission flags for automation

### -i, --interactive

Start interactive mode and automatically execute the provided prompt.

```bash
copilot -i "Review the codebase for security issues"
```

**Type:** String  
**Mode:** Interactive  
**Difference from -p:** Remains in session after executing initial prompt

### -s, --silent

Output only the agent response (no stats, banners, or metadata). Useful for scripting.

```bash
copilot -p "Generate API docs" --allow-all -s > api-docs.md
```

**Type:** Boolean  
**Requires:** Used with `-p` (non-interactive mode)  
**Output:** Clean agent response only

### -v, --version

Show version information.

```bash
copilot -v
copilot --version
```

### -h, --help

Display help information.

```bash
copilot -h
copilot --help
```

## Session Management

### --continue

Resume the most recent session.

```bash
copilot --continue
copilot --continue --allow-all-tools
```

**Behavior:**
- Loads last session automatically
- Restores conversation context
- Can override permissions

### --resume

Resume a previous session (optionally with session ID).

```bash
# Interactive picker
copilot --resume

# Specific session
copilot --resume abc123def456
```

**With ID:** Resumes specific session  
**Without ID:** Shows interactive session picker

## Permission Options

### --allow-all

Enable all permissions (equivalent to `--allow-all-tools --allow-all-paths --allow-all-urls`).

```bash
copilot -p "Implement feature" --allow-all
```

**Grants:**
- All tool permissions
- All file path access
- All URL access

**Alias:** `--yolo`

### --yolo

Shorthand for `--allow-all`.

```bash
copilot -p "Quick fix" --yolo
```

**Use when:** Trusted environment, quick iteration, full automation

### --allow-all-tools

Allow all tools to run automatically without confirmation.

```bash
copilot -p "Deploy changes" --allow-all-tools
```

**Environment variable:** `COPILOT_ALLOW_ALL`  
**Required for:** Non-interactive mode automation

### --allow-tool

Specify individual tools the CLI has permission to use.

```bash
# Allow file writing
copilot --allow-tool write

# Allow all git commands
copilot --allow-tool 'shell(git:*)'

# Multiple tools
copilot --allow-tool write --allow-tool 'shell(npm:*)'
```

**Pattern matching:**
- `write` - File write operations
- `shell(git:*)` - All git commands
- `shell(npm install)` - Specific command
- `MyMCP(tool_name)` - Specific MCP tool

### --deny-tool

Deny specific tools (takes precedence over --allow-tool).

```bash
# Allow all git except push
copilot --allow-tool 'shell(git:*)' --deny-tool 'shell(git push)'

# Deny dangerous commands
copilot --allow-all-tools --deny-tool 'shell(rm *)'
```

**Use for:** Blacklisting dangerous operations while allowing broad access

### --available-tools

Restrict available tools to specific set.

```bash
copilot --available-tools write read shell
```

**Effect:** Only listed tools are available to the model  
**Use for:** Limiting scope for specific tasks

### --excluded-tools

Prevent specific tools from being available.

```bash
copilot --excluded-tools 'shell(rm)' 'shell(dd)'
```

**Difference from --deny-tool:** Tools not shown to model at all

### --allow-all-paths

Disable file path verification and allow access to any path.

```bash
copilot --allow-all-paths
```

**Security:** Use cautiously, only in trusted environments

### --add-dir

Add a directory to the allowed list for file access.

```bash
# Single directory
copilot --add-dir /home/user/projects

# Multiple directories
copilot --add-dir ~/workspace --add-dir /tmp --add-dir ~/shared
```

**Default allowed:** Current working directory  
**Can be used multiple times**

### --disallow-temp-dir

Prevent automatic access to system temporary directory.

```bash
copilot --disallow-temp-dir
```

**Default:** Temp directory is allowed

### --allow-all-urls

Allow access to all URLs without confirmation.

```bash
copilot --allow-all-urls
```

**Use when:** Automation requires web access

### --allow-url

Allow access to specific URLs or domains.

```bash
# Single domain (defaults to HTTPS)
copilot --allow-url github.com

# Multiple URLs
copilot --allow-url github.com --allow-url api.example.com

# Specific protocol
copilot --allow-url https://api.example.com
```

**Can be used multiple times**

### --deny-url

Deny access to specific URLs or domains (takes precedence over --allow-url).

```bash
copilot --deny-url malicious-site.com
copilot --deny-url https://blocked.example.com
```

## Model Selection

### --model

Set the AI model to use.

```bash
copilot --model claude-sonnet-4.5
copilot --model gpt-5
copilot --model claude-opus-4.5
```

**Available models:**
- `claude-sonnet-4.5` (default) - Best for most coding tasks
- `claude-opus-4.5` - Complex reasoning and architecture
- `claude-haiku-4.5` - Fast, lightweight tasks
- `claude-sonnet-4` - Previous generation
- `gpt-5.2-codex` - GPT variant optimized for code
- `gpt-5.2` - Latest GPT model
- `gpt-5.1-codex-max` - Large context GPT codex
- `gpt-5.1-codex` - GPT codex variant
- `gpt-5.1` - GPT variant
- `gpt-5` - GPT base
- `gpt-5.1-codex-mini` - Small GPT codex
- `gpt-5-mini` - Small GPT
- `gpt-4.1` - Previous GPT generation
- `gemini-3-pro-preview` - Google Gemini

**Selection guide:**
- Default/general: `claude-sonnet-4.5`
- Complex/architecture: `claude-opus-4.5`
- Fast/simple: `claude-haiku-4.5`
- Alternative: `gpt-5` or `gemini-3-pro-preview`

## Agent and Behavior

### --agent

Specify a custom agent to use.

```bash
copilot --agent my-custom-agent
```

**Use for:** Custom agent implementations

### --no-ask-user

Disable the ask_user tool (agent works autonomously without asking questions).

```bash
copilot -p "Implement feature" --no-ask-user --allow-all
```

**Effect:** Agent makes decisions without user input  
**Use for:** Full automation, CI/CD

### --experimental

Enable experimental features.

```bash
copilot --experimental
```

**Disable:** `--no-experimental`

## MCP Server Configuration

### --disable-builtin-mcps

Disable all built-in MCP servers (currently: github-mcp-server).

```bash
copilot --disable-builtin-mcps
```

### --disable-mcp-server

Disable a specific MCP server.

```bash
copilot --disable-mcp-server github-mcp-server
copilot --disable-mcp-server custom-server
```

**Can be used multiple times**

### --enable-all-github-mcp-tools

Enable all GitHub MCP server tools instead of the default CLI subset.

```bash
copilot --enable-all-github-mcp-tools
```

**Overrides:** `--add-github-mcp-toolset` and `--add-github-mcp-tool`

### --add-github-mcp-tool

Add a specific tool to enable for the GitHub MCP server.

```bash
# Add single tool
copilot --add-github-mcp-tool create_pull_request

# Add multiple tools
copilot --add-github-mcp-tool create_pull_request \
        --add-github-mcp-tool merge_pull_request

# Enable all tools
copilot --add-github-mcp-tool "*"
```

**Can be used multiple times**

### --add-github-mcp-toolset

Add a toolset to enable for the GitHub MCP server.

```bash
# Add toolset
copilot --add-github-mcp-toolset pull_requests

# Enable all toolsets
copilot --add-github-mcp-toolset all
```

**Can be used multiple times**

### --additional-mcp-config

Additional MCP servers configuration as JSON string or file path.

```bash
# From file (prefix with @)
copilot --additional-mcp-config @~/my-mcp-config.json

# JSON string
copilot --additional-mcp-config '{"myserver": {"command": "node", "args": ["server.js"]}}'

# Multiple configs
copilot --additional-mcp-config @~/config1.json \
        --additional-mcp-config @~/config2.json
```

**Augments:** `~/.copilot/mcp-config.json` for this session  
**Can be used multiple times**

## Custom Instructions

### --no-custom-instructions

Disable loading of custom instructions from AGENTS.md and related files.

```bash
copilot --no-custom-instructions
```

**Use when:** Testing without project-specific instructions

## Output and Sharing

### --share

Share session to markdown file after completion in non-interactive mode.

```bash
# Default path
copilot -p "Implement feature" --allow-all --share

# Custom path
copilot -p "Fix bug" --allow-all --share ./bug-fix-session.md
```

**Default path:** `./copilot-session-<id>.md`  
**Mode:** Non-interactive only

### --share-gist

Share session to a secret GitHub gist after completion.

```bash
copilot -p "Create component" --allow-all --share-gist
```

**Mode:** Non-interactive only  
**Output:** Gist URL

## Display and UI

### --banner

Show the startup banner.

```bash
copilot --banner
```

**Default:** Banner shown in interactive mode

### --no-color

Disable all color output.

```bash
copilot --no-color
```

**Use for:** Logging, CI/CD environments

### --plain-diff

Disable rich diff rendering (use plain text diffs).

```bash
copilot --plain-diff
```

**Effect:** No syntax highlighting in diffs

### --screen-reader

Enable screen reader optimizations.

```bash
copilot --screen-reader
```

**Effect:** Adjusts output for accessibility

### --stream

Enable or disable streaming mode.

```bash
copilot --stream on
copilot --stream off
```

**Choices:** `on`, `off`  
**Default:** Streaming enabled

## Configuration and Logging

### --config-dir

Set the configuration directory.

```bash
copilot --config-dir ~/.my-copilot-config
```

**Default:** `~/.copilot`  
**Contains:** Authentication, settings, MCP configs

### --log-dir

Set log file directory.

```bash
copilot --log-dir ~/copilot-logs
```

**Default:** `~/.copilot/logs/`

### --log-level

Set the log level.

```bash
copilot --log-level debug
copilot --log-level error
copilot --log-level none
```

**Choices:**
- `none` - No logging
- `error` - Errors only
- `warning` - Warnings and errors
- `info` - Informational messages
- `debug` - Detailed debugging
- `all` - Everything
- `default` - Standard logging

## Updates

### --no-auto-update

Disable downloading CLI update automatically.

```bash
copilot --no-auto-update
```

**Default:** Auto-update enabled

## Advanced Options

### --acp

Start as Agent Client Protocol server.

```bash
copilot --acp
```

**Use for:** Integration with ACP-compatible tools

### --disable-parallel-tools-execution

Disable parallel execution of tools.

```bash
copilot --disable-parallel-tools-execution
```

**Effect:** Tools executed sequentially even if LLM requests parallel execution  
**Use when:** Resource constraints or debugging

## Option Combinations

### Full Automation

```bash
copilot -p "task" --allow-all --no-ask-user -s
```

### Safe Automation

```bash
copilot -p "task" \
  --allow-tool write \
  --allow-tool 'shell(git:*)' \
  --deny-tool 'shell(git push)' \
  --add-dir ~/safe-workspace
```

### Development Session

```bash
copilot -i "Implement auth" \
  --model claude-sonnet-4.5 \
  --allow-all-tools \
  --add-dir ~/project
```

### CI/CD Integration

```bash
copilot -p "Run tests and fix failures" \
  --allow-all \
  --no-ask-user \
  -s \
  --no-color \
  --share ./test-results.md
```

## Environment Variables

Options can also be set via environment variables:

- `COPILOT_ALLOW_ALL` - Equivalent to `--allow-all-tools`
- See `copilot help environment` for full list

## Configuration Precedence

1. Command-line flags (highest priority)
2. Environment variables
3. Configuration files in `~/.copilot/`
4. Defaults (lowest priority)
