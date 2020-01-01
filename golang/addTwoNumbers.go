package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	carry := 0
	curr := &ListNode{Val: 0, Next: nil}
	head := curr

	for l1 != nil || l2 != nil {
		val := carry
		if l1 != nil {
			val += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			val += l2.Val
			l2 = l2.Next
		}
		curr.Next = &ListNode{Val: val % 10, Next: nil}
		curr = curr.Next
		carry = val / 10
		fmt.Println(carry)
	}
	if carry > 0 {
		curr.Next = &ListNode{Val: carry, Next: nil}
	}
	return head.Next
}
