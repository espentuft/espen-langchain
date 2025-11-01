# Git and GitHub Setup

## Initialize Git Repository

Run these commands in the `espen-langchain` directory:

```bash
cd ~/Documents/production/espen-langchain

# Initialize git
git init

# Create initial commit
git add .
git commit -m "Initial commit: LangChain project setup"
```

## Create GitHub Repository

### Option 1: Using GitHub Web Interface

1. Go to https://github.com/new
2. Repository name: `espen-langchain`
3. Description: "LangChain experiments and applications"
4. Visibility: Public or Private (your choice)
5. **Do NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### Option 2: Using GitHub CLI (if installed)

```bash
gh repo create espen-langchain --public --source=. --remote=origin --push
```

## Connect Local to GitHub

After creating the repository on GitHub:

```bash
# Add remote
git remote add origin https://github.com/YOUR_USERNAME/espen-langchain.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Future Commits

```bash
# Make changes, then:
git add .
git commit -m "feat: your feature description"
git push origin main
```

## Branching Strategy (Optional)

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Work on feature, commit changes
git add .
git commit -m "feat: implement feature X"

# Merge back to main
git checkout main
git merge feature/your-feature-name
git push origin main
```

