import java.lang.*;
import java.util.*;
class Solution {
    public String solution(String my_string, int n) {
        String[] myString = my_string.split("");
        StringBuilder sb = new StringBuilder();
        for (String str : myString){
            sb.append(sol(str, n));
        }
        String answer = sb.toString();
        return answer;
    }
    public String sol(String s, int n){
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++){
            sb.append(s);
        }
        String result = sb.toString();
        return result;
    }
}