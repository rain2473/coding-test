class Solution {
    public long solution(int balls, int share) {
        long answer = 1;
        long tmp = 1;
        if (share > balls - share){
            share = balls - share;
        }
        for (long i = 0; i < share; i++){
            answer *= (balls - i);
            if ((answer) % (i + 1) == 0){
                answer /= i + 1;
            }
            else{
                tmp *= i + 1;
            }
        }
        answer /= tmp;
        return answer;
    }
}