class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        char[] my_char = my_string.toCharArray();
        char[] temp = new char[my_string.length()];
        
        for(int i = 0; i < queries.length; i++) {
            for (int j = queries[i][1]; j >= queries[i][0]; j--) {
                temp[queries[i][1] - j] = my_char[j];
            }
            for (int j = queries[i][0]; j <= queries[i][1]; j++) {
                my_char[j] = temp[j - queries[i][0]];
            }
        }
        answer = String.valueOf(my_char);
        
        return answer;
    }
}