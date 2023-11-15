/*
 * @lc app=leetcode id=77 lang=javascript
 *
 * [77] Combinations
 */

// @lc code=start
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
//  The right way is push and pop on the same array, so no cost of copying array.
var combine = function (n, k) {
  function backtrack(start, cur) {
    if (cur.length === k) {
      res.push([...cur]);
      return;
    }
    for (let i = start; i <= n; i++) {
      if (k - cur.length <= n - i + 1) {
        cur.push(i);
        backtrack(i + 1, cur);
        cur.pop();
      }
    }
  }
  let res = [];
  backtrack(1, []);
  return res;
};
// The wrong way
var combine = function (n, k) {
  function backtrack(start, cur) {
    if (cur.length === k) {
      res.push(cur);
      return;
    }
    for (let i = start; i <= n; i++) {
      if (k - cur.length <= n - i + 1) {
        backtrack(i + 1, [...cur, i]);
      }
    }
  }
  let res = [];
  backtrack(1, []);
  return res;
};
// @lc code=end
