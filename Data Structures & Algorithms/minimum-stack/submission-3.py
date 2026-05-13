class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else: 
            if self.minStack[-1] >= self.stack[-1]:
                self.minStack.append(val)
          
    
        # stack:    1 2 0
        # minStack: 1 0

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1] and len(self.stack) > 0:
            self.stack.pop()
            self.minStack.pop()
        else: 
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]    
