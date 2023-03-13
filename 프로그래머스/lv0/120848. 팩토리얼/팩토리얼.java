class Solution {
    public int solution(int n) {
        int answer = 0;
        int i = 2;
        while (n >= i) {
            n = n / i;
            i++;
        }
        answer = i - 1;
        return answer;
    }
}