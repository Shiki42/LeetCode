/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var numWays = function (n, k) {
  let memo = {};
  let total_way = (i) => {
    if (i === 1) return k;
    if (i === 2) return k * k;
    if (memo[i]) return memo[i];
    memo[i] = total_way(i - 1) * (k - 1) + total_way(i - 2) * (k - 1);
    return memo[i];
  };
  return total_way(n);
};
