class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        #程式差一行  沒檢查到0和-1
        if n <= 0:
            return False
        while n > 1: #到1為止
            if n%3 != 0: #沒辦法被3整除
                return False #失敗
            else:
                n = n // 3

      #經過上面的 while迴圈層層檢查，
        return True #那就是成功