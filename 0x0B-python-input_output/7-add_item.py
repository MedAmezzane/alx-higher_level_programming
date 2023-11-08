#!/usr/bin/python3
# 7-add_item.py
"""
A script to add command-line arguments to a Python list and save them to a file
"""

import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    # Add command-line arguments to the existing items
    new_items = sys.argv[1:]
    items = existing_items + new_items

    # Save the updated list to a file
    save_to_json_file(items, "add_item.json")
