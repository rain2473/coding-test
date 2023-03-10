class Solution {
    public int solution(int price) {
        int answer = price / 10;
        if (price >= 500_000){
            answer *= 8;
        } else if (price >= 300_000){
            answer *= 9;
        } else if (price >= 100_000){
            answer = answer * 95 / 10;
        } else {
            answer *= 10;
        }
        return answer;
    }
}