class Solution {
    public int solution(int i, int j, int k) {
        StringBuilder tmp = new StringBuilder();
        for (int a = i; a < j + 1; a++){
            tmp.append(String.valueOf(a));
        }
        int answer = tmp.length();
        String replaced = tmp.toString().replace(String.valueOf(k),"");
        answer -= replaced.length();
        return answer;
    }
}