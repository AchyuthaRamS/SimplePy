class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
           if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val % 10)
            curr = curr.next
            carry = int(val / 10)
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next
    
        def dfs(self, candidates, target, path, res):
        if target < 0:
            return   #backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target - candidates[i], path + [candidates[i]], res)
