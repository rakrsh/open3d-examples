# Autonomous Agent Guidelines

This document outlines the operational boundaries, tool usage, and best practices for autonomous AI agents working within this repository.

## Operational Boundaries & Safety
- **Workspace Confinement**: Agents must strictly operate within the project workspace. Do not read, write, or modify files outside of the provided working directory.
- **Non-Destructive Actions**: Avoid deleting files, dropping databases, or overriding substantial existing logic without explicit user confirmation. When in doubt, ask.
- **Safe Commands**: Never auto-run terminal commands that have potentially destructive or irreversible side effects (e.g., system-wide installations, removing directories recursively, making external network requests to unknown APIs). Always wait for user approval for execution.
- **Environment Awareness**: Be mindful of the host operating system (e.g., Windows vs. Linux) and adjust file paths, shell commands (e.g., PowerShell vs. Bash), and scripts accordingly.

## Tool Usage Best Practices
1. **Prioritize Specific Tools**: Always use the most specific tool available for a task. 
   - Use file reading/writing tools instead of running `cat` or `echo >` in a terminal.
   - Use native search tools (like `grep_search`) instead of executing shell searches unless absolutely necessary.
2. **Context Gathering**: Before modifying code, thoroughly analyze the context. View relevant files, search for references, and understand how your changes impact the broader system.
3. **Targeted Edits**: When editing files, use specialized editing tools (like replace/multi-replace) targeting specific line ranges rather than rewriting entire files, to minimize risk and resource usage.

## Workflow Execution
1. **Step-by-Step Execution**: Break down complex requests into smaller, logical steps. Complete and verify one step before moving to the next.
2. **Validate Changes**: After writing code or making configurations, verify correctness. Run linters, unit tests, or build commands if available and safe to do so.
3. **Error Handling**: If a command or tool call fails, analyze the error output carefully. Do not blindly retry the exact same action. Adjust your approach based on the error message.
4. **Clear Communication**: Provide concise, markdown-formatted summaries of the actions taken. If you encounter an obstacle or require a decision, clearly state the issue and ask the user for clarification. Do not make assumptions on critical architectural choices.
