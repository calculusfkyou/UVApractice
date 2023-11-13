import java.util.Scanner;

public class UVA10812 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        int cases = sc.nextInt();
        for (int i = 0; i < cases; i++) {
            long s = sc.nextLong(), d = sc.nextLong();

            long x = s + d, y = s - d;

            if (x < 0 || y < 0 || (x % 2 != 0 || y % 2 != 0))
                System.out.println("impossible"); // 比數<0 或者 比數不能整除 皆為不可能出現。
            else
                System.out.println(x / 2 + " " + y / 2);
        }
        sc.close();
    }
}