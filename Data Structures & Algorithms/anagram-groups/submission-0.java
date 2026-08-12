class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {


        /*
            what we will do is : 
            after sorting, we will take a hashMap 
            put the string that are sorted in the hashmap as a key 
            then we'll put the elements from strs in hashmap as values and if the the
        */ 
        Map<String, List<String>> result = new HashMap<>();
        // take one element from the list and sort it
        // java strings are imutuable so, take the string put it in the char list
        // sort the cahr list then -> convert the list in string 
        for(String s : strs){
            char[] chr = s.toCharArray();
            Arrays.sort(chr); // sort the char list then
            String str = new String(chr); // convert the list in string
            result.putIfAbsent(str, new ArrayList<>()); // hashmap(key,value) = [str: [] ]
            result.get(str).add(s); 
        }

        return new ArrayList<>(result.values());
        

    }
}
