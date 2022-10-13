class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        ls1, ls2 = len(nums1), len(nums2)
        if ls1 < ls2:
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0, ls2 * 2
        while l <= r:
            mid2 = (l + r) >> 1
            R1 = sys.maxint if mid1 == 2 * ls1 else nums1[mid1 >> 1]
            R2 = sys.maxint if mid2 == 2 * ls2 else nums2[mid2 >> 1]
            if L1 > R2:
                l = mid2 + 1
            elif L2 > R1:
                r = mid2 - 1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0

            
                     res = []
        dt = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        def helper(index,string):
            if index==len(digits):
                res.append(string)
                return True
            for ele in (dt[digits[index]]):
                string+=ele
                helper(index+1,string)
                string = string[:-1]
        helper(0,"")
        return res
            

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.findMedianSortedArrays([1, 1], [1, 2])
