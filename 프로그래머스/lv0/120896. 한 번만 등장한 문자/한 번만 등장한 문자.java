import java.util.*;
class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        String[] alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
        String[] str = s.split("");
        HashMap<String, Integer> dict = new HashMap<>(); 
        for (String a : alphabet){
            dict.put(a, 0);
        }
        for (String key : str){
            dict.replace(key, dict.get(key) + 1);
        }
        for (String key : alphabet){
            if (dict.get(key).equals(1)){
                answer.append(key);
            }
        }
        return answer.toString();
    }
}