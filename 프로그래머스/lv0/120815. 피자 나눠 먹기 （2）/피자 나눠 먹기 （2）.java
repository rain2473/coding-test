import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 1;
        int [] tmp = {n, 6};
        Arrays.sort(tmp);
        for (int i = tmp[0]; i > 0; i--){
            if (n % i == 0 && 6 % i == 0){
                answer = n / i;
                break;
            }
        }
        return answer;
    }
}