import java.util.*;

public class UVA10050 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();
        for (int i = 0; i < testCase; i++) {
            int day = sc.nextInt(), hartal = sc.nextInt(), ans = 0;
            int[] record = new int[day + 1];
            Arrays.fill(record, 0);
            for (int j = 0; j < hartal; j++) {
                int h = sc.nextInt();
                for (int k = h; k < day + 1; k += h) {
                    if (record[k] == 0) {
                        if (k % 7 != 6 && k % 7 != 0) {
                            record[k] = 1;
                            ans += 1;
                        }
                    }
                }
            }
            System.out.println(ans);
        }
        sc.close();
    }
}
