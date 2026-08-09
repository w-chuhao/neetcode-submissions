

class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> map = new HashMap<>();
        int[] ans = new int[2];

        for(int i=0; i<nums.length; i+=1){
            int second = target - nums[i];
            if(map.containsKey(second)){
                ans[0] = map.get(second);
                ans[1] = i;
                return ans;
            }
            else{
                map.put(nums[i],i);
            }

        }

        return ans;
        
    }
}
