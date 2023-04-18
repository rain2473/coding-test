class Solution {
    public int solution(String my_string) {
        int answer = 0;
        int num = 0;
        int tmp = 0;
        String[] stringArray = my_string.split("");
        for (String a : stringArray){
            try{
                tmp = Integer.parseInt(a);
                num *= 10;
                num += tmp;
            }
            catch(NumberFormatException e){
                answer += num;
                num = 0;
            }
        }
        return answer += num;
    }
}