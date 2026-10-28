"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Existing elements at and after the insertion position shift right.
    # Python lists store references, so these references are shifted.
    # Beginning and middle insertions take O(n) time due to shifting.
    # End insertion takes amortized O(1) time, but resizing can take O(n).
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Accept nonnegative indexes that identify an existing element.
    # Validation prevents IndexError and protects an empty list.
    if 0 <= index < len(lst):
        # Remove the selected value and return it to the caller.
        # Elements after this position shift left to fill the gap.
        return lst.pop(index)

    # Leave the list unchanged when the index is invalid.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Examine elements sequentially because the list is not assumed sorted.
    # This linear search takes O(n) time in the worst case.
    for index, item in enumerate(lst):
        if item == value:
            # Return the index of the first matching value.
            return index

    # No matching value was found after checking every element.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # Use a playlist to demonstrate an ordered collection of songs.
    playlist = ["Song A", "Song B", "Song C", "Song D"]
    print("Original playlist:", playlist)

    # Insert at the beginning, shifting all existing songs right.
    insert_at(playlist, 0, "Opening Song")
    print("After insertion at the beginning:", playlist)

    # Insert at the middle, shifting the remaining songs right.
    middle_index = len(playlist) // 2
    insert_at(playlist, middle_index, "Middle Song")
    print("After insertion at the middle:", playlist)

    # Insert at the end without shifting existing songs.
    insert_at(playlist, len(playlist), "Closing Song")
    print("After insertion at the end:", playlist)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # Remove the first song; remaining songs shift left.
    removed = delete_at(playlist, 0)
    print("Removed from the beginning:", removed)
    print("Updated playlist:", playlist)

    # Calculate the current middle index and remove that song.
    middle_index = len(playlist) // 2
    removed = delete_at(playlist, middle_index)
    print("Removed from the middle:", removed)
    print("Updated playlist:", playlist)

    # Remove the last song; no remaining songs need to shift.
    removed = delete_at(playlist, len(playlist) - 1)
    print("Removed from the end:", removed)
    print("Updated playlist:", playlist)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # Search for a song that remains in the playlist.
    found_index = search_value(playlist, "Song C")
    print("Index of Song C:", found_index)

    # Search for a missing song; -1 indicates no match.
    missing_index = search_value(playlist, "Missing Song")
    print("Index of Missing Song:", missing_index, "(-1 means not found)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # An index equal to the length is invalid for deletion.
    removed = delete_at(playlist, len(playlist))
    print("Delete using an out-of-range index:", removed)
    print("Playlist remains unchanged:", playlist)

    # This implementation rejects negative deletion indexes.
    removed = delete_at(playlist, -1)
    print("Delete using a negative index:", removed)
    print("Playlist remains unchanged:", playlist)

    # Deleting from an empty list safely returns None.
    empty_playlist = []
    print("Delete from an empty playlist:", delete_at(empty_playlist, 0))

    # Searching an empty list returns -1 without entering the loop.
    print("Search an empty playlist:", search_value(empty_playlist, "Song A"))

    # Inserting at index 0 creates the first element in an empty list.
    insert_at(empty_playlist, 0, "First Song")
    print("After insertion into an empty playlist:", empty_playlist)


if __name__ == "__main__":
    main()