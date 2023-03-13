import java.util.*;
class Solution {
    public int[] solution(int n) {
        Set<Integer> set = new HashSet<>();
        int i = 2;
        while (n != 1){
            while (true){
                if (n % i != 0){
                    break;
                }
                else{
                    n = n / i;
                    set.add(i);
                }
            }
            i++;
        } 
        int[] answer = Arrays.stream(set.toArray(new Integer[0])).mapToInt(Integer::intValue).toArray();
        Arrays.sort(answer);
        return answer;
    }
}