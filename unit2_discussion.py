"""Unit 2 Discussion: Stacks and Queues.
Author: Bendu Konah
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Adding and removing at the same end makes the newest item leave first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            raise IndexError("Cannot undo: the stack is empty.")
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            raise IndexError("Cannot peek: the stack is empty.")
        # Preview the newest action without changing the stack.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New orders join the back so older orders are served first.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            raise IndexError("Cannot serve: the queue is empty.")
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            raise IndexError("Cannot preview: the queue is empty.")
        # Preview the oldest order without removing it.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def show_empty_operation(operation):
    """Display an expected error and allow the demonstration to continue."""
    try:
        operation()
    except IndexError as error:
        print(error)


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # TODO (Student): STACK DEMO
    # Create a stack, add four values, and demonstrate LIFO.
    # Test empty pop, empty peek, and single-item removal.
    print("\n=== STACK: PRINT DESIGN UNDO HISTORY ===")
    history = Stack()

    actions = [
        "Added customer name",
        "Changed font",
        "Added a picture",
        "Changed background color"
    ]

    for action in actions:
        history.push(action)
        print("Recorded:", action)

    print("Latest action:", history.peek())
    assert len(history.items) == 4  # Peek must not remove anything.

    for expected in reversed(actions):
        actual = history.pop()
        assert actual == expected
        print("Undo:", actual)

    assert history.is_empty()
    show_empty_operation(history.pop)
    show_empty_operation(history.peek)

    history.push("Added a logo")
    assert history.pop() == "Added a logo"
    assert history.is_empty()
    print("Single-item stack empty after removal:", history.is_empty())

    # Additional test: repeated values and interleaved operations.
    history.push("Changed font")
    history.push("Changed font")
    assert history.pop() == "Changed font"
    history.push("Added border")
    assert history.pop() == "Added border"
    assert history.pop() == "Changed font"
    assert history.is_empty()
    print("Additional stack checks passed.")

    # TODO (Student): QUEUE DEMO
    # Create a queue, add four values, and demonstrate FIFO.
    # Test empty dequeue, empty front, and single-item removal.
    print("\n=== QUEUE: CUSTOM PRINTING ORDERS ===")
    orders = Queue()

    requests = [
        "Order 1: T-shirt",
        "Order 2: Mug",
        "Order 3: Tumbler",
        "Order 4: Pillow"
    ]

    for request in requests:
        orders.enqueue(request)
        print("Received:", request)

    print("Next order:", orders.front())
    assert len(orders.items) == 4  # Front must not remove anything.

    for expected in requests:
        actual = orders.dequeue()
        assert actual == expected
        print("Processing:", actual)

    assert orders.is_empty()
    show_empty_operation(orders.dequeue)
    show_empty_operation(orders.front)

    orders.enqueue("Order 5: Cap")
    assert orders.dequeue() == "Order 5: Cap"
    assert orders.is_empty()
    print("Single-item queue empty after removal:", orders.is_empty())

    # Additional test: repeated values and interleaved operations.
    orders.enqueue("Mug")
    orders.enqueue("Mug")
    assert orders.dequeue() == "Mug"
    orders.enqueue("Sticker")
    assert orders.dequeue() == "Mug"
    assert orders.dequeue() == "Sticker"
    assert orders.is_empty()
    print("Additional queue checks passed.")

    print("\nAll demonstration checks passed.")


if __name__ == "__main__":
    main()