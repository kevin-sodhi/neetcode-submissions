class Solution { // Last In First Out
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        if(s.length() % 2 != 0) return false;
            for(char c : s.toCharArray()){
                if(c=='[' || c=='{'|| c=='('){
                    stack.push(c);
                }else{
                    if(stack.isEmpty()) return false;
                    char Top = stack.peek();
                    if((c==']'&& Top =='[')||
                       (c=='}'&& Top == '{')||
                       (c==')'&& Top == '(')){
                        stack.pop();
                    } else return false;
                } 
            }
        return stack.isEmpty();
    }
}
