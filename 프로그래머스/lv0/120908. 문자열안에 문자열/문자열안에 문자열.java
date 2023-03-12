class Solution {
    public int solution(String str1, String str2) {
        int answer = 1;
        if (str1.equals(str1.replaceAll(str2,""))){
            answer = 2;
        }
        return answer;
    }
}