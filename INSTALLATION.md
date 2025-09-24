# Installation Verification & Troubleshooting

## ✅ Installation Complete

The ComfyUI Prompt Iterator extension has been installed to:
- `C:\AI_Stuff\ComfyDesktop\custom_nodes\ComfyUI_PromptIterator\`
- `C:\AI_Stuff\ComfyUI\custom_nodes\ComfyUI_PromptIterator\`

## To Use the Extension:

### 1. **Restart ComfyUI Completely**
   - Close ComfyUI completely (not just the browser tab)
   - Make sure no ComfyUI processes are running
   - Start ComfyUI fresh

### 2. **Find the Nodes**
   - Look in the node menu under **"utils/prompt"** category
   - Or right-click and search for:
     - "Prompt Iterator" (basic version)
     - "Prompt Iterator (Advanced)" (full features)

### 3. **If Nodes Don't Appear:**

   **Check ComfyUI Console:**
   - Look for any error messages when ComfyUI starts
   - Look for the line: "ComfyUI Prompt Iterator v1.0.0"
   - Should show: "Loaded 2 custom nodes for prompt iteration"

   **Verify Installation:**
   ```bash
   cd C:\AI_Stuff\ComfyDesktop\custom_nodes\ComfyUI_PromptIterator
   python test_nodes.py
   ```

   **Clear ComfyUI Cache:**
   - Delete any `.pyc` files in the extension folder
   - Clear browser cache (Ctrl+F5)
   - Try a different browser

### 4. **Alternative Installation Locations:**

   If your ComfyUI is installed elsewhere, copy the folder to:
   - `[Your ComfyUI Path]/custom_nodes/ComfyUI_PromptIterator/`

### 5. **Required Files:**
   - `__init__.py` - Extension registration
   - `prompt_iterator.py` - Node implementations

## Quick Test

1. Add "Prompt Iterator Advanced" node
2. Enter test prompts:
   ```
   face front
   face left
   face right
   face back
   ```
3. Set suffixes:
   ```
   _front
   _left
   _right
   _back
   ```
4. Connect outputs:
   - `prompt` → CLIPTextEncode `text` input
   - `filename` → SaveImage `filename_prefix` input
5. Queue workflow 4 times

## Known Issues & Solutions

### "Node not found" Error:
- ComfyUI needs full restart, not just reload
- Check if `__init__.py` exists and isn't empty
- Verify no Python syntax errors in files

### Import Errors:
- Make sure both `__init__.py` and `prompt_iterator.py` are present
- Check Python version compatibility (3.8+)

### State Not Persisting:
- Use consistent `workflow_id` parameter
- Don't change workflow_id between runs

## Support

If issues persist after following these steps:
1. Check ComfyUI GitHub for compatibility
2. Verify your ComfyUI version is recent
3. Try installing in portable ComfyUI version