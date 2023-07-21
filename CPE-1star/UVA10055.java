import java.util.Scanner;

public class UVA10055 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            try {
                String input = scanner.nextLine();
                if (input.isEmpty()) {
                    break;
                }
                String[] inputs = input.split(" ");
                int n = Integer.parseInt(inputs[0]);
                int m = Integer.parseInt(inputs[1]);
                System.out.println(Math.abs(m - n));
            } catch (Exception e) {
                break;
            }
        }
    }
}
