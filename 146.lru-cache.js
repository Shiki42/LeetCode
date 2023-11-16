/*
 * @lc app=leetcode id=146 lang=javascript
 *
 * [146] LRU Cache
 */

// @lc code=start
/**
 * @param {number} capacity
 */
var LRUCache = function (capacity) {
  this.memo = new Map();
  this.capacity = capacity;
  this.head = null;
};

/**
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function (key) {
  if (!this.memo.has(key)) return -1;
  let node = this.memo.get(key);
  if (node === this.head) return node.val;
  if (node.next) node.next.prev = node.prev;
  if (node.prev) node.prev.next = node.next;
  tail = this.head.prev;
  this.head.prev = node;
  node.next = this.head;
  if (tail !== node) {
    node.prev = tail;
    tail.next = node;
  }
  this.head = node;
  return node.val;
};

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function (key, value) {
  if (!this.memo.has(key)) {
    this.memo.set(key, { val: value, prev: null, next: null });
    let node = this.memo.get(key);
    if (!this.head) {
      this.head = node;
      return;
    }
    if (this.memo.size > this.capacity) {
      let tail = this.head.prev;
      tail.prev.next = this.head;
      this.head.prev = tail.prev;
      this.memo.delete(tail);
    }
  } else {
    this.memo.get(key).val = value;
    let node = this.memo.get(key);
    if (this.head !== node) {
      if (node.next) node.next.prev = node.prev;
      if (node.prev) node.prev.next = node.next;
    }
  }
  let node = this.memo.get(key);
  prev = this.head.prev ? this.head.prev : null;
  this.head.prev = node;
  node.next = this.head;

  if (prev) node.prev = prev;
  if (prev) prev.next = node;
  this.head = node;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
// @lc code=end
