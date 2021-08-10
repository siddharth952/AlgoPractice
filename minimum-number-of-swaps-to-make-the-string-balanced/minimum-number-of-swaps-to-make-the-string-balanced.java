class Solution {
    public int minSwaps(String s) {
        Stack <Character> sk = new Stack();
        int mismatch = 0;
        for (int i = 0; i< s.length();i++) {
            char ch = s.charAt(i);
            if (ch == '[')
                sk.push(ch);
            else {
                if (!sk.empty())
                    sk.pop();
                else
                    mismatch++;
            }
        }
        return (mismatch +1) / 2; 
    }
}