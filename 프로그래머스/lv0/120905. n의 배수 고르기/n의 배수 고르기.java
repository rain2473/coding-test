import java.util.*;
import java.lang.*;
class Solution {
    public int[] solution(int n, int[] numlist) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int x : numlist){
            if (x % n == 0){
                answer.add(x);
            }
        }
        return Arrays.stream(answer.toArray(new Integer[answer.size()])).mapToInt(i->i).toArray();
    }
}