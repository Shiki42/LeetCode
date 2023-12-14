/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function (head, left, right) {
  if (right == left) return head;

  let ori = head;
  var reverse = function (head, length) {
    let tail = head;
    let prev = head;
    let temp = null;
    head = head.next;
    for (let i = 1; i <= length; i++) {
      temp = head.next;
      head.next = prev;
      prev = head;
      head = temp;
    }
    tail.next = head;
    return prev;
  };

  let i = 0;
  if (left == 1) {
    let rhead = reverse(head, right - left);
    return rhead;
  }
  while (i != left - 2) {
    head = head.next;
    i++;
  }
  let rhead = reverse(head.next, right - left);
  head.next = rhead;

  return ori;
};
