class MinStack:

    def __init__(self):
        self.stk=[]
        self.mstk=[]
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.mstk or val <= self.mstk[-1]:
            self.mstk.append(val)
        elif val>self.mstk[-1]:
            self.mstk.append(self.mstk[-1])
        

    def pop(self) -> None:
        self.mstk.pop()
        return self.stk.pop()


    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.mstk[-1]
        
