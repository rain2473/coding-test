class Solution {
    public String solution(String rsp) {
        StringBuilder answer = new StringBuilder();
        String[] newRSP= rsp.split("");
        for (String r : newRSP){
            if (r.equals("0")){
                answer.append("5");
            } else if (r.equals("2")){
                answer.append("0");
            } else{
                answer.append("2");
            }
        }
        return answer.toString();
    }
}