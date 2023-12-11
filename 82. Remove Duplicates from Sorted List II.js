/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
  let ori = null;
  let prevHead = null;
  while (head != undefined) {
    if (head.next && head.val === head.next.val) {
      let target = head.val;
      while (head && head.val === target) head = head.next;
      if (!head && prevHead) prevHead.next = null;
    } else {
      if (!ori) ori = head;
      if (prevHead === null) {
        prevHead = head;
      } else {
        prevHead.next = head;
        prevHead = head;
      }
      head = head.next;
    }
  }
  return ori;
};
