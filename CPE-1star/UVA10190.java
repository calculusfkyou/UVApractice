import java.util.ArrayList;
import java.util.Scanner;

public class UVA10190 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while (sc.hasNextInt()) {

            long n = sc.nextLong();
            long m = sc.nextLong();

            ArrayList<Long> ans = new ArrayList<>();

            if (m == 0 || m == 1) {
                System.out.println("Boring!");
                continue;
            }

            long temp = 1;
            while (temp <= n) {
                ans.add(temp);
                temp *= m;
            }

            if (ans.get(ans.size() - 1) == n) {
                for (int i = ans.size() - 1; i >= 0; i--) {
                    if (i != 0) {
                        System.out.print(ans.get(i) + " ");
                    } else {
                        System.out.print(ans.get(i));
                    }
                }
                System.out.println();
            } else {
                System.out.println("Boring!");
            }
        }
        sc.close();
    }
}