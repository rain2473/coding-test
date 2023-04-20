import java.util.*;
class Solution {
    public String[] solution(String my_str, int n) {
        String[] answer = null;
        String[] str = my_str.split("");
        StringBuilder tmp = new StringBuilder();
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < str.length; i++){
            tmp.append(str[i]);
            if (i % n == n - 1){
                result.append(tmp.toString() + " ");
                tmp.setLength(0);
            }
        }
        result.append(tmp.toString());
        answer = result.toString().split(" ");
        return answer;
    }
}