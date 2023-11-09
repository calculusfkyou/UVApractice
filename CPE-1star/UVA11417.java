import java.util.Scanner;

public class UVA11417 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            try {
                int n = sc.nextInt();
                if (n == 0)
                    break;
                int g = 0;
                for (int i = 1; i < n; i++) {
                    for (int j = i + 1; j <= n; j++)
                        g += gcd(i, j);
                }
                System.out.println(g);
            } catch (Exception e) {
                break;
            }
        }
        sc.close();
    }

    public static int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
}
