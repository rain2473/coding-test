import java.util.*;
class Solution {
    public int[] solution(String my_string) {
        my_string = my_string.replaceAll("[^0-9]","");
        String[] myString = my_string.split("");
        int[] answer = new int[myString.length];
        for (int i = 0; i < myString.length; i++){
            answer[i] = Integer.parseInt(myString[i]);
        }
        Arrays.sort(answer);
        return answer;
    }
}