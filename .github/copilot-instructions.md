# GitHub Copilot / AI Assistant Instructions

Welcome to the repository! When assisting with code in this project, please adhere to the following guidelines and best practices:

## General Principles
- **Clarity over Cleverness**: Write readable, straightforward code. Avoid overly complex one-liners if they hinder readability.
- **Consistency**: Follow the existing code style and patterns established in the repository. Look at surrounding files to match formatting and structure.
- **Documentation**: Provide clear, concise comments for complex logic. Ensure docstrings are added for all new public functions, classes, and modules. Update existing documentation when modifying behavior.
- **Test-Driven Approach**: When writing new features or fixing bugs, consider the testing implications. Suggest or write corresponding test cases to ensure reliability.
- **Security**: Avoid hardcoding secrets, credentials, or sensitive information. Use environment variables or configuration files.

## Language Specifics (General)
- Follow standard linting and formatting guidelines for the primary languages used in the repository (e.g., PEP 8 for Python, Prettier for JS/TS, `gofmt` for Go).
- Utilize modern language features appropriately, but avoid bleeding-edge syntax if it breaks compatibility with the project's supported versions.
- Use explicit type hinting or annotations where supported to improve code maintainability and tooling support.

## Refactoring and Modifications
- Do not remove or alter existing comments or docstrings unless they are directly related to the code you are changing.
- When fixing a bug, explain *why* the original code failed and how the fix addresses the root cause, rather than just providing the corrected code.
- Prefer small, atomic changes over large, monolithic rewrites unless specifically requested.

## Commits & Pull Requests
- Suggest descriptive and concise commit messages summarizing the changes and the reasoning behind them.
- Follow conventional commit formats if the project uses them (e.g., `feat:`, `fix:`, `docs:`).
