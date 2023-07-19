import java.util.Scanner;

public class UVA10055 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            while (true) {
                try {
                    String[] input = scanner.nextLine().split(" ");
                    int n = Integer.parseInt(input[0]);
                    int m = Integer.parseInt(input[1]);
                    System.out.println(Math.abs(m - n));
                } catch (Exception e) {
                    break;
                }
            }
        }
    }
}