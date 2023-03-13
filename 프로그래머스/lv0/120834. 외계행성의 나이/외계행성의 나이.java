class Solution {
    public String solution(int age) {
        String[] alphabet = "abcdefghij".split("");
        StringBuilder answer = new StringBuilder();
        while (age != 0){
            answer.append(alphabet[age % 10]);
            age = age / 10;
        }
        return answer.reverse().toString();
    }
}