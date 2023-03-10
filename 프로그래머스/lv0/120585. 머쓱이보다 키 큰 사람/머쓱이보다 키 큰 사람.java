import java.util.*;
class Solution {
    public int solution(int[] array, int height) {
        Arrays.sort(array);
        int answer = array.length;
        for (int i = 0; i < array.length; i++){
            if (array[i] <= height){
                answer--;
            }
            else{
                break;
            }
        }
        return answer;
    }
}