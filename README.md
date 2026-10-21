# \# Unit 2 Discussion: Stacks and Queues

# 

# Author: Bendu Konah

# 

# \## Overview

# 

# I implemented a stack and a queue in Python using a custom

# printing business scenario. The stack tracked print-design

# changes, while the queue managed incoming customer orders.

# 

# \## Implementation

# 

# I used a Python list for the stack. The push method added

# an action to the end, and pop removed the most recent action.

# The peek method previewed the latest action without removing it.

# These operations demonstrated last-in, first-out (LIFO) behavior.

# 

# I used collections.deque for the queue. The enqueue method

# added an order to the back, and dequeue removed the oldest

# order from the front using popleft(). The front method

# previewed the next order without removing it. These operations

# demonstrated first-in, first-out (FIFO) behavior.

# 

# I kept the TODO prompts and added comments explaining the logic.

# 

# \## Real-World Applications

# 

# The stack demonstrated undoing changes to a customer's print

# design. The most recent change was undone first.

# 

# The queue demonstrated processing T-shirt, mug, tumbler, and

# pillow orders in the order they were received.

# 

# \## Testing and Results

# 

# I ran the program and verified that all demonstration checks

# passed. I tested:

# 

# \- LIFO and FIFO removal order with four items each.

# \- Preview operations that did not remove items.

# \- Removal and preview operations on empty structures.

# \- Single-item structures becoming empty after removal.

# \- Repeated values.

# \- Additions mixed with removals.

# 

# Empty operations raised IndexError exceptions with clear

# messages. The demonstration caught those exceptions and

# continued running.

# 

# The program ended with:

# All demonstration checks passed.

# 

# \## Memory and Efficiency

# 

# Both structures used O(n) storage for n stored references.

# The stored objects also required memory, depending on their

# size. Memory requirements increased as more items were added.

# 

# Stack push and pop took amortized O(1) time. Queue enqueue

# and dequeue took O(1) time. Using popleft() avoided shifting

# the remaining queue items.

# 

# \## Reflection

# 

# I learned how insertion and removal positions determined

# whether a structure followed LIFO or FIFO order. Connecting

# these operations to printing orders and design changes helped

# me understand their practical uses.

# 

# One challenge was running the file from the terminal.

# The terminal initially looked in the wrong location.

# I resolved this by saving the file and running it with its

# correct path.

# 

# I also learned why empty structures needed explicit handling.

# Clear exceptions explained invalid operations, while exception

# handling allowed the demonstration to continue.

# 

# \## Execution

# 

# I ran the program with Python 3 using:

# 

# python unit2\_discussion.py

