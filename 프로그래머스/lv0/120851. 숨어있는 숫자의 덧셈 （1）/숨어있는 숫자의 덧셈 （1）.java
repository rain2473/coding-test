class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] my_str = my_string.split("");
        for (int i = 0; i < my_string.length(); i++){
            try{
                answer += Integer.parseInt(my_str[i]);
            }
            catch(NumberFormatException e){
                    continue;
            }
        }
        return answer;
    }
}