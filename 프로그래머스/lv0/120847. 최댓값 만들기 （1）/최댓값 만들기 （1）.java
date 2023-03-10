import java.util.*;
class Solution {
    public int solution(int[] numbers) {
        int m1 = 0, m2 = 0;
        for (int number : numbers){
            if (number > m1 && number > m2){
                m2 = m1;
                m1 = number;
            } else if (number > m2){
                m2 = number;
            }
        }
        int answer = m1 * m2;
        return answer;
    }
}