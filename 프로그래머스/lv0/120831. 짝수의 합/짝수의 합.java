class Solution {
    public int solution(int n) {
        int m = n / 2;
        int answer = 0;
        for (int i = 0; i < m + 1; i++){
            answer += 2 * i;
        }
        return answer;
    }
}