/*
 * @lc app=leetcode id=119 lang=javascript
 *
 * [119] Pascal's Triangle II
 */

// @lc code=start
/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function (rowIndex) {
  let curRow = [1];
  for (let i = 1; i <= rowIndex; i++) {
    let nextRow = [];
    for (let j = 0; j <= i; j++) {
      nextRow.push((curRow[j - 1] || 0) + (curRow[j] || 0));
    }
    curRow = nextRow;
  }
  return curRow;
};
// @lc code=end
