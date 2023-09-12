import java.util.Scanner;

public class UVA100 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNext()) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int subn = n;
            int subm = m;

            if (n > m) {
                int tempp = n;
                n = m;
                m = tempp;
            }

            int[] temp2 = new int[m - n + 1];

            for (int i = n; i <= m; i++) {
                int num = i;
                int steps = 1;

                while (num != 1) {
                    if (num % 2 != 0) {
                        num = num * 3 + 1;
                    } else {
                        num = num / 2;
                    }
                    steps++;
                }

                temp2[i - n] = steps;
            }

            int maxTemp2 = 0;
            for (int value : temp2) {
                if (value > maxTemp2) {
                    maxTemp2 = value;
                }
            }

            System.out.printf("%d %d %d%n", subn, subm, maxTemp2);
        }

        scanner.close();
    }
}
