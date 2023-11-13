import java.util.Scanner;

public class UVA10268 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            long x = Long.parseLong(sc.nextLine());
            String an[] = sc.nextLine().split("\\s+"); // 跳過多個空白鍵

            long ans = 0;
            long xp = 1;
            for (int i = an.length - 2; i >= 0; i--, xp *= x) {
                ans += Long.parseLong(an[i]) * (an.length - 1 - i) * xp; // 微分計算
            }

            // Output
            System.out.println(ans);
        }
        sc.close();
    }
}