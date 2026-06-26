class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            if i in {"[","(","{"}:
                stk.append(i)
            elif i==")":
                if not stk or stk.pop()!="(":
                    return False
            elif i=="}":
                if not stk or stk.pop()!="{":
                    return False
            elif i=="]":
                if not stk or stk.pop()!="[":
                    return False
        return len(stk)==0
        