# GitHub Repository Setup

## Creating the Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `ComfyUI_PromptIterator`
3. Description: "ComfyUI custom node for iterating through multiple prompts with automatic filename generation"
4. Set to **Public** (or Private if preferred)
5. **DO NOT** initialize with README, .gitignore, or license (we already have them)
6. Click "Create repository"

## Pushing to GitHub

After creating the empty repository on GitHub, run these commands:

```bash
# Navigate to the repository
cd C:\AI_Stuff\ComfyDesktop\custom_nodes\ComfyUI_PromptIterator

# Add the remote origin (replace USERNAME with your GitHub username)
git remote add origin https://github.com/BiloxiStudios/ComfyUI_PromptIterator.git

# Push to GitHub
git push -u origin master
```

## Alternative: Using GitHub CLI

If you have GitHub CLI installed:

```bash
# Create and push in one command
gh repo create BiloxiStudios/ComfyUI_PromptIterator --public --source=. --push
```

## Repository Features to Enable

After pushing, consider enabling these GitHub features:

1. **Issues** - For bug reports and feature requests
2. **Discussions** - For community Q&A
3. **Wiki** - For detailed documentation
4. **Actions** - For automated testing (optional)

## Recommended Repository Settings

1. Go to Settings → General
2. Features:
   - ✅ Issues
   - ✅ Preserve this repository
   - ✅ Discussions (optional)

3. Go to Settings → Pages (optional)
   - Source: Deploy from branch
   - Branch: master
   - Folder: / (root)

## Adding Topics

Add these topics to help people find your extension:
- `comfyui`
- `comfyui-nodes`
- `comfyui-custom-nodes`
- `prompt-engineering`
- `batch-processing`
- `workflow-automation`

## README Badge

Add this badge to your README.md:

```markdown
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Node-blue)](https://github.com/comfyanonymous/ComfyUI)
```

## Installation Instructions for Users

Once published, users can install with:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/BiloxiStudios/ComfyUI_PromptIterator.git
# Restart ComfyUI
```