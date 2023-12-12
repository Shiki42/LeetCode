/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function (head, x) {
  let Fake1 = new ListNode();
  let Fake2 = new ListNode();
  let curS = Fake1;
  let curL = Fake2;
  while (head) {
    if (head.val < x) {
      curS.next = head;
      curS = curS.next;
    } else {
      curL.next = head;
      curL = curL.next;
    }
    head = head.next;
  }
  curS.next = Fake2.next;
  curL.next = null;
  return Fake1.next;
};
