class Solution {
    public int solution(int[] box, int n) {
        int answer = 1;
        for (int x : box){
            answer *= x / n;
        }
        return answer;
    }
}