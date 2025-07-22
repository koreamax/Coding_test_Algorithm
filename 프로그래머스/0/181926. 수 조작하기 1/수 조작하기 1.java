class Solution {
    public int solution(int n, String control) {
        int answer = 0;
        char[] temp = control.toCharArray();
        for (int i = 0 ; i < temp.length; i++) {
            if (temp[i] == 'w') {
                n++;
            }
            else if (temp[i] == 's') {
                n--;
            }
            else if (temp[i] == 'd') {
                n += 10;
            }
            else if (temp[i] == 'a') {
                n -= 10;
            }
        }
        answer = n;
        return answer;
    }
}