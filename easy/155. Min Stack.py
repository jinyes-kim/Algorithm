class MinStack:
    def __init__(self):
        self.tmp = []

    def push(self, x: int) -> None:
        self.tmp.append(x)

    def pop(self) -> None:
        self.tmp = self.tmp[:-1]

    def top(self) -> int:
        return self.tmp[-1]

    def getMin(self) -> int:
        try:
            return min(self.tmp)
        except:
            return




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()