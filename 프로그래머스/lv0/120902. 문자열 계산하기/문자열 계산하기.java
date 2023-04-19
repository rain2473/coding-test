class Solution {
    public int solution(String my_string) {
        int answer = 0;
        int tmp = 0;
        String[] query = my_string.split(" ");
        for (int i = 0; i < query.length; i++){
            String a = query[i];
            if (i == 0){
                answer = Integer.parseInt(a);
                continue;
            }
            if (a.equals("+")){
                tmp = 1;
            }else if (a.equals("-")){
                tmp = -1;
            }else {
                tmp *= Integer.parseInt(a);
                answer += tmp;
            }
        }
        
        return answer;
    }
}