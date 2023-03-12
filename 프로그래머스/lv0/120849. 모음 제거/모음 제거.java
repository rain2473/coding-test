class Solution {
    public String solution(String my_string) {
        String[] vowels= {"a","e","i","u","o"};
        for (String v : vowels){
            my_string = my_string.replaceAll(v,"");
        }
        return my_string;
    }
}