class Solution:
    def countPrimes(self, n: int) -> int:
        c = 0
        p = 2
        arr = [True for i in range(n+1)]
        while (p*p< n):
            if arr[p]:
                for i in range(p*p, n+1, p):
                    arr[i] = False
            p+=1
        
        for i in range(2, n):
            if arr[i]:
                c+=1
        return c