class Solution {
    public int solution(int[] dot) {
        int answer = 1;
        if (dot[1] < 0){
            answer += 2;
        }
        if (dot[0] * dot[1] < 0){
            answer += 1;
        }
        return answer;
    }
}