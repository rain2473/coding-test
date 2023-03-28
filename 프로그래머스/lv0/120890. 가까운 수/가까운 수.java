import java.util.*;
class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int sub = 101;
        for (int a : array){
            if (Math.abs(n - a) < sub){
                sub = Math.abs(n - a);
                answer = a;
            } else if(Math.abs(n - a) == sub){
                if (a < answer){
                    answer = a;
                }
            }
        }
        return answer;
    }
}