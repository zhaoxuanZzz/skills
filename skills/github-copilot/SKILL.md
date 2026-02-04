---
name: github-copilot
description: Use GitHub Copilot CLI to generate code, shell commands, and manage Pull Requests. Use this skill when you need to write code, debug issues, or submit changes via PRs using GitHub's CLI tools.
---

# GitHub Copilot CLI Skill

This skill enables the agent to use GitHub Copilot CLI (`gh copilot`) and GitHub CLI (`gh`) to write code, execute complex shell commands, and manage Pull Requests autonomously.

## Capabilities

1.  **Generate Code & Commands**: Use Copilot to write scripts, functions, or shell one-liners.
2.  **Explain Code**: Understand legacy code or complex errors.
3.  **Manage PRs**: Create, checkout, and merge Pull Requests.

## Prerequisites

-   `gh` (GitHub CLI) must be installed and authenticated.
-   `gh copilot` extension must be installed (`gh extension install github/gh-copilot`).

## Workflow: Autonomous Development Loop

Use this loop to complete coding tasks:

1.  **Setup**:
    ```bash
    git checkout -b feature/task-name
    ```

2.  **Develop**:
    -   Need code? Ask Copilot:
        ```bash
        gh copilot suggest -t generic "python function to calculate fibonacci"
        ```
    -   *Action*: Read the output, extract the code block, and use the `write` tool to save it to a file.
    -   Need a command? Ask Copilot:
        ```bash
        gh copilot suggest -t shell "undo last git commit keeping changes"
        ```
    -   *Action*: Review the command and run it with `exec`.

3.  **Verify**:
    -   Run tests or linters.
    -   Fix issues (repeat step 2).

4.  **Submit**:
    ```bash
    git add .
    git commit -m "feat: complete task description"
    gh pr create --fill --web
    ```

## Troubleshooting

-   **"Command not found"**: Ensure `gh` is in the `$PATH`.
-   **Authentication**: If commands fail with 401/403, run `gh auth login` (requires interactive mode or token).
-   **Copilot Limits**: Copilot provides suggestions, not perfect code. Always review the output before executing `eval` or writing to critical files.
