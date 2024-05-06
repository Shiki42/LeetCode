class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<> ();
        result.add(new ArrayList<>());
        for (int i = 0; i < nums.length; ++i) {
            List<List<Integer>> newResult = new ArrayList<>();
            for (List<Integer> L: result) {
                L = new ArrayList<>(L);
                L.add(nums[i]);
                newResult.add(L);
            }
            result.addAll(newResult);
        }
        return result;
    }
}