class Solution {
    public int[] solution(String[] wallpaper) {
        int xmin = 51;
        int ymin = 51;
        int xmax = -1;
        int ymax = -1;
        int idx = -1;
        for (String line : wallpaper){
            idx++;
            if (!line.contains("#")) continue;
            if (line.indexOf("#") < xmin){
                xmin = line.indexOf("#");
            }
            if (line.lastIndexOf("#") + 1 > xmax){
                xmax = line.lastIndexOf("#") + 1;
            }
            if (idx + 1> ymax){
                ymax = idx + 1;
            }
            if (idx < ymin){
                ymin = idx;
            }
        }
        int[] answer = {ymin,xmin,ymax,xmax};
        return answer;
    }
}