from collections import deque

class MyStackTwoQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Push element to q2
        self.q2.append(x)
        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1

class MyStackOneQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # Rotate the queue so that the last added element is at the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q



if __name__ == "__main__":
    print("Testing MyStackTwoQueues:")
    stack1 = MyStackTwoQueues()
    stack1.push(1)
    stack1.push(2)
    print(stack1.top())    # Output: 2
    print(stack1.pop())    # Output: 2
    print(stack1.empty())  # Output: False

    print("\nTesting MyStackOneQueue:")
    stack2 = MyStackOneQueue()
    stack2.push(1)
    stack2.push(2)
    print(stack2.top())    # Output: 2
    print(stack2.pop())    # Output: 2
    print(stack2.empty())  # Output: False