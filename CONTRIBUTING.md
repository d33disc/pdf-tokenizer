# Contributing Guidelines

## Getting Started

Thank you for considering contributing to our project! This document provides guidelines and instructions for contributing.

### Prerequisites

- Python 3.8 or higher
- Git
- Understanding of parallel processing and document handling

### Setting Up Development Environment

1. Fork the repository
2. Clone your fork:
 ```bash
 git clone https://github.com/your-username/doc-processor.git
 ```
3. Set up development environment:
 ```bash
 cd doc-processor
 python -m venv venv
 source venv/bin/activate  # or `venv\Scripts\activate` on Windows
 pip install -r requirements-dev.txt
 ```

## Force Committing Changes

To force commit all changes in Git, follow these steps:

1. Stage all changes:
 ```bash
 git add .
 ```

2. Commit with a message and bypass pre-commit hooks:
 ```bash
 git commit -m "Your commit message" --no-verify
 ```

3. Push the changes to the remote repository:
 ```bash
 git push
 ```
