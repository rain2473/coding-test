class Solution {
    public int[] solution(int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < n + 1; i++){
            if (n % i == 0){
                sb.append(String.valueOf(i)+"yeah");
            }
        }
        String[] str = sb.toString().split("yeah");
        int[] answer = new int[str.length];
        for (int i = 0; i < str.length; i++){
            answer[i] = Integer.parseInt(str[i]);
        }
        return answer;
    }
}