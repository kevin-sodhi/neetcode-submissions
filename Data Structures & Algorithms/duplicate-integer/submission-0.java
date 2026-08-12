class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for (int x : nums) {
            if (!seen.add(x)) {   // add returns false if x already exists
                return true;      // duplicate found
            }
        }
        return false;             // no duplicates
    }
}