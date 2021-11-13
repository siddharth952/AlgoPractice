class Solution {
    public int[] dailyTemperatures(int[] temps) {
        Stack<Integer> stk = new Stack<>();
        int[] ret = new int[temps.length];
        for(int i=0; i<temps.length;i++){
            while(!stk.isEmpty() && temps[i] > temps[stk.peek()]) {
                int idx = stk.pop();
                ret[idx] = i-idx;
            }
            stk.push(i);
        }
        return ret;
    }
}