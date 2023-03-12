class Solution {
    public String solution(String my_string, int num1, int num2) {
        String[] result = my_string.split("");
        String tmp = result[num1];
        result[num1] = result[num2];
        result[num2] = tmp;
        return String.join("",result);
    }
}