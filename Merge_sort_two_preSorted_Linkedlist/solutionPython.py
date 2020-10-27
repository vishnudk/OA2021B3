def function(head1, head2):
#     the main agenda is to merge sort both the pre sorted linked list
    if head1.data > head2.data:
        tail = head = SinglyLinkedListNode(head2.data)
        head2 = head2.next
    else:
        tail = head = SinglyLinkedListNode(head1.data)
        head1 = head1.next
    while head1 != None and head2!=None:
        if head1.data > head2.data:
            tail.next = SinglyLinkedListNode(head2.data)
            head2 = head2.next
            tail = tail.next
        else:
            tail.next = SinglyLinkedListNode(head1.data)
            head1 = head1.next
            tail = tail.next
    if head1!=None:
        tail.next = head1
    else:
        tail.next = head2
    return head
if __name__ == "__main__": 
   # provide the head pointer to the two sorted linked list for merge sorting 
   print(function(head1,head2))
