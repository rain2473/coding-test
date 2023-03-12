class Solution {
    public int solution(int n) {
        String str[] = String.valueOf(n).split("");
        int answer = 0;
        for (String s : str){
            answer += Integer.parseInt(s);
        }
        return answer;
    }
}