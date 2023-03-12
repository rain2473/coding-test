class Solution {
    public String solution(String cipher, int code) {
        StringBuilder answer = new StringBuilder();
        String[] ciphers = cipher.split("");
        for (int i = 0; i < ciphers.length; i++){
            if (i % code == code - 1){
                answer.append(ciphers[i]);
            }
        }
        return answer.toString();
    }
}