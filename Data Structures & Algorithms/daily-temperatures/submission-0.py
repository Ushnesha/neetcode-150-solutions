class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stk = [n-1]
        for i in range(n-2,-1,-1):
            while(len(stk) > 0 and temperatures[i] >= temperatures[stk[-1]]):
                stk.pop()
            if len(stk) > 0:
                res[i] = stk[-1] - i
            stk.append(i)
        return res

        