class Solution {
    public int[] twoSum(int[] nums, int target) {
        if(nums.length == 0 ){
            return null;
        }
        // By using hashMaps
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            // hashmap.put(key, Value);
            hashmap.put(nums[i], i);
        }
        // i + y = target
        // rearrangeing : y = target - i
        for (int i = 0; i < nums.length; i++) {
            int prevVal = target - nums[i];
            if(hashmap.containsKey(prevVal) && hashmap.get(prevVal) !=i ){
                return new int[]{i,hashmap.get(prevVal)};
            }
        }
        return new int[0];
    }
}
