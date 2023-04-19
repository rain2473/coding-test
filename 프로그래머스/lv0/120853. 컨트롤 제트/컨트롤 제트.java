class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] commend = s.split(" ");
        int tmp = 0;
        for (String now : commend){
            now = now.toLowerCase();
            if (now.equals("z")){
                answer -= tmp;
            }
            else{
                tmp = Integer.parseInt(now);
                answer += tmp;
            }
        }
        return answer;
    }
}