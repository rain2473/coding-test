import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        int answer = Integer.parseInt(input[0]) + Integer.parseInt(input[1]);

        System.out.println(answer);
    }
}