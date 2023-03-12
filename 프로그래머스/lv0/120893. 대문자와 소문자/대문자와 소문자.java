class Solution {
    public String solution(String my_string) {
        String[] myString = my_string.split("");
        StringBuilder answer = new StringBuilder();
        for (String str : myString){
            if (str.equals(str.toUpperCase())){
                answer.append(str.toLowerCase());
            } else{
                answer.append(str.toUpperCase());
            }
        }
        return answer.toString();
    }
}