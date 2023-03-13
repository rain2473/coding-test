class Solution {
    public int solution(int n) {
        if (n < 4){
            return 0;
        } else{
            int answer = 0;
            for (int i = 4; i < n + 1; i++){
                for (int j = 2; j < i; j++){
                    if (i % j == 0){
                        answer += 1;
                        break;
                    }
                }
            }
            return answer;
        }
        
    }
}