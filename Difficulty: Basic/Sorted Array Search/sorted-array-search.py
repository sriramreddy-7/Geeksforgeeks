#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        if k in arr:
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        A = [int(x) for x in input().strip().split()]
        k = int(input())
        ob = Solution()
        print("true" if ob.searchInSorted(A, k) else "false")
        print("~")

# } Driver Code Ends