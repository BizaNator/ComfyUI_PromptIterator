#!/usr/bin/env python
"""
Test script to verify the Prompt Iterator nodes work correctly
"""

# Test import
try:
    from prompt_iterator import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
    print("[OK] Import successful")
    print(f"  Found nodes: {list(NODE_CLASS_MAPPINGS.keys())}")
    print(f"  Display names: {list(NODE_DISPLAY_NAME_MAPPINGS.values())}")
except ImportError as e:
    print(f"[ERROR] Import failed: {e}")
    exit(1)

# Test node instantiation
try:
    basic_node = NODE_CLASS_MAPPINGS["PromptIterator"]()
    advanced_node = NODE_CLASS_MAPPINGS["PromptIteratorAdvanced"]()
    print("[OK] Node instantiation successful")
except Exception as e:
    print(f"[ERROR] Node instantiation failed: {e}")
    exit(1)

# Test INPUT_TYPES
try:
    basic_inputs = NODE_CLASS_MAPPINGS["PromptIterator"].INPUT_TYPES()
    advanced_inputs = NODE_CLASS_MAPPINGS["PromptIteratorAdvanced"].INPUT_TYPES()
    print("[OK] INPUT_TYPES methods work")
    print(f"  Basic node has: {list(basic_inputs['required'].keys())} required inputs")
    print(f"  Advanced node has: {list(advanced_inputs['required'].keys())} required inputs")
except Exception as e:
    print(f"[ERROR] INPUT_TYPES failed: {e}")
    exit(1)

# Test basic node execution
try:
    result = basic_node.iterate_prompt(
        prompts="test prompt 1\ntest prompt 2",
        mode="sequential",
        base_filename="test",
        filenames="",
        manual_index=0,
        reset=False,
        workflow_id="test"
    )
    print("[OK] Basic node execution successful")
    print(f"  Result: prompt='{result[0][:30]}...', filename='{result[1]}'")
except Exception as e:
    print(f"[ERROR] Basic node execution failed: {e}")
    exit(1)

# Test advanced node execution
try:
    result = advanced_node.iterate_prompt_advanced(
        prompts="face front\nface left\nface right\nface back",
        mode="sequential",
        filename_mode="suffix_list",
        base_filename="character",
        filenames="",
        suffixes="_front\n_left\n_right\n_back",
        filename_template="{base}_{suffix}",
        prepend_text="",
        append_text="",
        manual_index=0,
        loop_mode="loop",
        reset=False,
        random_seed=-1,
        workflow_id="test"
    )
    print("[OK] Advanced node execution successful")
    print(f"  Result: prompt='{result[0][:30]}...', filename='{result[1]}'")
except Exception as e:
    print(f"[ERROR] Advanced node execution failed: {e}")
    exit(1)

print("\n[SUCCESS] All tests passed! The extension should work in ComfyUI.")
print("\nIf ComfyUI still doesn't recognize the nodes:")
print("1. Make sure ComfyUI is fully restarted")
print("2. Check the ComfyUI console for any error messages")
print("3. Verify the custom_nodes directory is correct for your installation")