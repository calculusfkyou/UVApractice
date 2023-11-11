import java.util.Scanner;

public class UVA10783 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();
        for (int i = 0; i < testCase; i++) {
            int a = sc.nextInt(), b = sc.nextInt(), sum = 0;
            for (int j = a; j <= b; j++) {
                if (j % 2 != 0)
                    sum += j;
            }
            System.out.println("Case " + (i + 1) + ": " + sum);
        }
        sc.close();
    }
}