import java.math.*;
class Solution {
    public int solution(int n) {
        int m = (int) Math.sqrt(n);
        int answer = 0;
        for (int i = 1; i < m + 1; i++){
            if (n % i == 0){
                answer += 2;
            }
        }
        if (Math.pow(m,2) == n){
            answer--;
        }
        return answer;
    }
}