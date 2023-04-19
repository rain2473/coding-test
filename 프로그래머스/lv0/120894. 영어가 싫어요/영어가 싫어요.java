class Solution {
    public long solution(String numbers) {
        String[] number = "zero,one,two,three,four,five,six,seven,eight,nine".split(",");
        for (int i = 0; i < number.length; i++){
            numbers = numbers.replace(number[i], String.valueOf(i));
        }
        long answer = Long.parseLong(numbers);
        return answer;
    }
}