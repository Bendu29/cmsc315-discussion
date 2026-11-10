# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.


Running the Program

Run python unit5_discussion.py from the folder containing the script.

Results

Both searches found 17 at index 2 in the small dataset and returned -1 for the missing value 20. In the 50,000-item dataset, searching for the missing value 50000 required linear search to check all 50,000 elements. Binary search checked 16. Both searches returned -1 for an empty list and 0 for a match in a single-element list.

Real World Example

A store could use these methods to look up an inventory item by product ID. Linear search works for a short, unsorted list of newly received items. Binary search is better suited to repeated lookups in a large inventory list sorted by product ID.
