class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String[] number = String.valueOf(num).split("");
        for (int i = 0; i < number.length; i++){
            if (k == (Integer.parseInt(number[i]))){
                answer = i + 1;
                break;
            }
        }
        return answer;
    }
}