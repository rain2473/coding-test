import java.util.*;
class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        String[] myString = my_string.toLowerCase().split("");
        Arrays.sort(myString);
        for (String s : myString){
            answer.append(s);
        }
        return answer.toString();
    }
}