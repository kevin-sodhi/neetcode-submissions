class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        // we want to make sure each string has same charaters 
        // we will use 2 hashmaps : one for s and one for t
        // each hashmap will store char as KEY and Count as VALUE
        // then we compare if each key corsponds to value of s,t
        
        Map<Character,Integer> countS = new HashMap<>();
        Map<Character,Integer> countT = new HashMap<>();

        for(int i=0;i < s.length();i++){
            // store key for each 
            countS.put(s.charAt(i), countS.getOrDefault(s.charAt(i),0) + 1);
            countT.put(t.charAt(i), countT.getOrDefault(t.charAt(i),0) + 1);
        }
        return countS.equals(countT);
        
        /*  Time complexity = sorting O(n log n) and space O(n)
        if(s.length() != t.length()){
            return false;
        }
        char[] sArray = s.toCharArray();
        Arrays.sort(sArray);
        String sortS = new String(sArray);

        char[] tArray = t.toCharArray();
        Arrays.sort(tArray);
        String sortT = new String(tArray);
        
        return sortS.equals(sortT);
        */
    }
}
