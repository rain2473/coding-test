import java.util.*;
class Solution {
    public String solution(String my_string) {
        String answer = "";
        List<String> list = new ArrayList(Arrays.asList(my_string.split("")));
        List<String> reverse = new ArrayList();
        for (int i = list.size()-1; i > -1; i--){
            reverse.add(list.get(i));
        }
        answer = String.join("",reverse);
        return answer;
    }
}