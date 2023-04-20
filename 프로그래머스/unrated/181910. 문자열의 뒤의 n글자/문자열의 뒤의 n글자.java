class Solution {
    public String solution(String my_string, int n) {
        StringBuilder answer = new StringBuilder();
        String[] str = my_string.split("");
        int len = my_string.length() - n;
        for (int i = len; i < str.length; i++){
            answer.append(str[i]);
        }
        return answer.toString();
    }
}