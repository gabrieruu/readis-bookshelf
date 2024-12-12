# Readis

A simple library management system built with Flask and SQLAlchemy.

For information on how to use the API, consult the API Guide.
For other development informations, consult the DEV Guide.

---

## Requirements

To run this project, you will need the following tools installed:

- **Docker**: [Download Docker](https://www.docker.com/products/docker-desktop)
- **Make**: [Download Make](https://www.gnu.org/software/make/)

---

## Usage Guide

Follow these steps to set up and use the development environment:

1. **Build the development environment image**:  
   ```bash
   make build
   ```

2. **Start the development container and enable a shell**:  
   ```bash
   make dev
   ```

Optionally, if you want to start the API from the codebase directly, you can run:
```bash
   python3 run.py
```

--- 

## Commit Standard

### **Standard Format**
- **Type**: A prefix indicating the type of change (e.g., `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`).
- **Scope** (optional): A noun describing the part of the codebase affected (e.g., `auth`, `api`, `ui`).
- **Subject**: A brief description of the change.

**Example:**
```
feat(auth): add login functionality
```

### 2. **Write Clear and Concise Subject Lines**
- Use the imperative mood ("Fix bug" instead of "Fixed bug" or "Fixes bug").
- Keep the subject line under 50 characters if possible.

**Example:**
```
refactor: update user authentication flow
```

### 3. **Provide Detailed Descriptions (Optional)** 
If necessary, include a body with more details about the change. The body should:
- Explain the **why** and **how** of the change.
- Wrap text at 72 characters.
- Separate from the subject line with a blank line.

**Example:**
```
fix: resolve null pointer exception in user service

The null pointer exception was caused by an uninitialized variable in
the user service. Added checks to ensure the variable is initialized
before usage.
```

### 4. **Reference Issues and Pull Requests (Optional)**
If your commit relates to a specific issue or pull request, reference it using a keyword (e.g., `Closes #123` or `Fixes #456`). This creates a link between the commit and the issue.

**Example:**
```
docs: update README with setup instructions

Closes #78
```

### 5. **Use Consistent Terminology**
Stick to a consistent vocabulary and style. For instance, if you use or you see that `add` is used to describe new features, continue using it rather than switching to `implement` or `create`.

<!-- ### 6. **Include Breaking Changes**
If a commit introduces a breaking change, make sure to mention it in the commit message with `BREAKING CHANGE:` followed by a description.

**Example:**
```
feat: remove support for Node.js 10

BREAKING CHANGE: This update removes support for Node.js 10, requiring
users to upgrade to Node.js 12 or higher.
``` -->

### References and Further Reading
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [The seven rules of a great Git commit message](https://chris.beams.io/posts/git-commit/)