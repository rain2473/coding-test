class Solution {
    public int solution(int angle) {
        int answer = 2 * (angle / 90);
        if (angle % 90 != 0){
            answer += 1;
        }
        return answer;
    }
}