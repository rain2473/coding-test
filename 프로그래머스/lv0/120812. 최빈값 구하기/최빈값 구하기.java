import java.util.*;
class Solution {
    public int solution(int[] array) {
        Arrays.sort(array);
        int answer = 0;
        int count = 0;
        int tmpc = -1;
        int tmpn = -1;
        for (int n : array){
            if (n != tmpn){
                if(tmpc > count){
                    answer = tmpn;
                    count = tmpc;
                }
                else if(tmpc == count){
                    answer = -1;
                }
                tmpc = 1;
                tmpn = n;
            }else{
                tmpc += 1;
            }
        }
        if(tmpc > count){
            answer = tmpn;
            count = tmpc;
        }
        else if(tmpc == count){
            answer = -1;
        }
        return answer;
    }
}