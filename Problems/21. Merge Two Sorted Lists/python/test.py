from merge_two_sorted_lists import Solution, ListNode

def create_list(vals):
    dummy = ListNode()
    cur = dummy 
    for val in vals:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

def test_answer():
    list1 = create_list([1,2,4])
    list2 = create_list([1,3,4])
    assert Solution().mergeTwoLists(list1, list2) == [1,1,2,3,4,4]