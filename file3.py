class Solution(object):

    def lengthOfLongestSubstring(self, s):
        charMap = {}
        for i in range(256):
            charMap[i] = -1
        ls = len(s)
        i = max_len = 0
        for j in range(ls):
            charMap[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
        return max_len
    
            res=[]
        self.dfs(range(1, n+1), k, [], res)
        return res
    
    def dfs(self, nums, k, path, res):
        if len(path) == k:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k, path+ [nums[i]], res)
