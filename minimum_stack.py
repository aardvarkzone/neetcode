class MinStack:

    def __init__(self):
        self.stack = []
        self.small = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.small[-1] if self.small else val)
        self.small.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.small.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.small[-1]
