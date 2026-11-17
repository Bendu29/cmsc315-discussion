"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Create an empty dictionary for Crafted Identity's inventory.
    # Product SKUs are unique keys, and stock quantities are values.
    inventory = {}

    # A dictionary uses a key's hash to help locate its entry.
    # Python resolves collisions internally so different keys remain distinct.
    # Insertions and lookups typically take O(1) average time.
    inventory["TUMBLER-20"] = 25
    inventory["MUG-11"] = 40
    inventory["SHIRT-M"] = 18
    inventory["GLASS-16"] = 12
    inventory["PILLOW-14"] = 0

    print("Crafted Identity inventory:", inventory)
    print("Number of product types:", len(inventory))

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # Access each quantity using its exact SKU.
    # The dictionary locates the entry without scanning every product.
    print("TUMBLER-20 quantity:", inventory["TUMBLER-20"])
    print("MUG-11 quantity:", inventory["MUG-11"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print("Before update:", inventory)

    # Assigning a value to an existing key replaces its previous quantity.
    # It does not add a duplicate key or increase the dictionary's size.
    inventory["TUMBLER-20"] = 30

    print("After updating TUMBLER-20 to 30:", inventory)
    print("Number of product types:", len(inventory))

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("Before deletion:", inventory)

    # Remove the known existing SKU and its associated quantity.
    # Other inventory entries remain available.
    del inventory["SHIRT-M"]

    print("After deleting SHIRT-M:", inventory)
    print("Number of product types:", len(inventory))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Look up a missing SKU safely.
    # get() returns None when the key is absent instead of raising KeyError.
    # None is distinguishable from zero, which is a valid stock quantity.
    missing_quantity = inventory.get("HAT-01")
    print("Missing SKU HAT-01:", missing_quantity)
    print("None means this SKU is not in the inventory.")

    # Edge case 2: Delete a missing SKU safely.
    # Providing a default to pop() avoids KeyError when the key is absent.
    size_before = len(inventory)
    removed_quantity = inventory.pop("HAT-01", None)

    print("Removing missing SKU HAT-01:", removed_quantity)
    print("No item was removed.")
    print("Inventory size unchanged:", len(inventory) == size_before)

    # Edge case 3: An existing product can have zero stock.
    # Check explicitly for None rather than using a truth-value check.
    pillow_quantity = inventory.get("PILLOW-14")

    if pillow_quantity is None:
        print("PILLOW-14 was not found.")
    else:
        print("PILLOW-14 exists. Quantity:", pillow_quantity)
        print("Zero means out of stock, not a missing SKU.")


if __name__ == "__main__":
    main()