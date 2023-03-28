import java.util.*;
class Solution {
    public int solution(String before, String after) {
        List<String> tmp1 = Arrays.asList(before.split(""));
        Collections.sort(tmp1);
        List<String> tmp2 = Arrays.asList(after.split(""));
        Collections.sort(tmp2);
        if (tmp1.equals(tmp2)) return 1;
        return 0;
    }
}