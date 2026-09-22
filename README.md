# Week 7 Assignment: Shopping List Manager

This assignment practices Python lists, indexing, `.append()`, `.remove()`, membership checking with `in`, and loops.

* `list_warmup.py` — Demonstrates basic list operations including index access, adding and removing fruits, and counting items.
* `shopping_list.py` — Provides an interactive shopping list manager for adding, removing, showing, and finishing a shopping list.
* `list_report.py` — Prints a numbered shopping list, counts item names with more than four letters, and finds the longest item name using a loop.

It is safer to check `in` before calling `.remove()` because `.remove()` causes an error if the item is not in the list. Checking first allows the program to handle a missing item safely and display a helpful message instead of crashing. This makes the shopping list manager more reliable for users.
