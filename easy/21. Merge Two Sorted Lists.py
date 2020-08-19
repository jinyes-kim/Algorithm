# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode(None)
        pivot = answer
        while l1 and l2:
            if l1.val <= l2.val:
                new_node = ListNode(l1.val)
                pivot.next = new_node
                pivot = new_node
                try:
                    l1 = l1.next
                except:
                    break
            else:
                new_node = ListNode(l2.val)
                pivot.next = new_node
                pivot = new_node
                try:
                    l2 = l2.next
                except:
                    break

        while l1:
            new_node = ListNode(l1.val)
            pivot.next = new_node
            pivot = new_node
            try:
                l1 = l1.next
            except:
                break

        while l2:
            new_node = ListNode(l2.val)
            pivot.next = new_node
            pivot = new_node
            try:
                l2 = l2.next
            except:
                break

        answer = answer.next
        return answer

    
    
"""
리스트에 전부 넣고 sort를 하는 방법이 조금 더 파이썬스러운 방법일 수는 있지만
링크드 리스트를 링크드 리스트처럼 사용하는 방법은 아니라고 생각했다.

두 링크드 리스트의 value를 비교하면서 값을 추가하고
연결리스트에 남은 value들을 붙여준다.

head 용도인 answer 는 None으로 초기화했으므로
반환 전에 다음 값으로 넘겨준다.
"""
