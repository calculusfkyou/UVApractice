import java.util.Scanner;

public class UVA12019 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int cases = sc.nextInt();
        for (int i = 0; i < cases; i++) {
            int[] month = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 }; // 每個月天數。
            String[] week = { "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" }; // 星期表。
            int M = sc.nextInt();
            int D = sc.nextInt();

            D = D + 4; // 調整成0=Monday 1=Tuesday ... // 2011/1/1 禮拜六
            for (int j = 1; j < M; j++) {
                D = D + month[j - 1];
            }

            // Output
            System.out.println(week[D % 7]);
        }
        sc.close();
    }
}