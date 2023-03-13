class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        for (String s : my_string.split("")){
            if (answer.indexOf(s) == -1){
                answer.append(s);
            }
        }
        return answer.toString();
    }
}