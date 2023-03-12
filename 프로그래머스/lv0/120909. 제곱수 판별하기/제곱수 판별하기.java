import java.math.*;
class Solution {
    public int solution(int n) {
        int answer = 1;
        int det = (int) Math.pow((int) Math.sqrt(n),2);
        if (det != n){
            answer = 2;
        }
        return answer;
    }
}