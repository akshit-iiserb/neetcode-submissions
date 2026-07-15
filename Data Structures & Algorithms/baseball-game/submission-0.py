class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        for i in range(len(operations)):
            if operations[i]=="+":
                stk.append(int(stk[-1])+int(stk[-2]))
            elif operations[i]=="D":
                stk.append(int(stk[-1])*2)
            elif operations[i]=="C":
                stk.pop()
            else:
                stk.append(int(operations[i]))
        sum=0
        for num in stk:
            sum+=num
        return sum

            
        