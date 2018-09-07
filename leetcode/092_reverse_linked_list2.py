class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if (m == n):
            return head
        
        frontNode=ListNode(0)
        frontNode.next=head
        pre=frontNode

        for i in range(m-1):
            pre = pre.next

        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            temp = cur.next
            cur.next = reverse
            reverse=cur
            cur=temp

        pre.next.next = cur
        pre.next =reverse

        return frontNode.next 