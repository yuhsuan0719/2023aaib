class Solution:
    def average(self, salary: List[int]) -> float:
        #算平均的方法: (加起來), 再除(數量)
        N = len(salary)

        ans = (sum(salary) -max(salary) -min(salary)) / (N-2) #先乘除後加減()

        return ans