class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minimum = min(self.stack)
        return minimum


m1 = MinStack()
m1.push(10)
m1.push(3)
m1.push(1)
m1.push(2)
print(m1.pop())
print(m1.top())
print(m1.getMin())
