
import java.util.*;
class Solution {
    public String solution(String bin1, String bin2) {
        long answer = 0;
        long tmp = 0;
        long i = 0;
        long b1 = Long.parseLong(bin1);
        long b2 = Long.parseLong(bin2);
        long summation = b1 + b2;
        while (summation != 0){
            tmp = summation % 10;
            summation = summation / 10 + tmp / 2;
            tmp = (tmp % 2) * (long) Math.pow(10, i);
            answer += tmp;
            i++;
        }
        return String.valueOf(answer);
    }
}