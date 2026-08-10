class Solution {
    public int lengthOfLongestSubstring(String s) {

        char[] chars = s.toCharArray();
        List<Character> current = new ArrayList<>();

        int count = 0;
        int max = 0;

        for(int right=0; right<chars.length; right+=1){
            while(current.contains(chars[right])){
                current.remove(0);
                count-=1;
            }

            current.add(chars[right]);
            count+=1;
            
            if(count>max){
                max = count;
            }
        }
        return max;
        
    }
}
