import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        String[] input = scanner.nextLine().split(" ");
        int M = -1;
        double answer = 0;
        for (int i = 0; i < n; i++) {
            int tmp = Integer.parseInt(input[i]);
            answer += tmp;
            if (M < tmp){
                M = tmp;
            }
        }
        answer = answer / n * 100 / M;
        System.out.println(answer);
    }
}
