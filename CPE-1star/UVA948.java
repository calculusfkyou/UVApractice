import java.util.Scanner;
import java.util.ArrayList;

public class UVA948 {
    public static void main(String[] args) {
        ArrayList<Integer> fibList = new ArrayList<>();
        fibList.add(0);
        fibList.add(1);

        // 創建 Fibonacci 數列
        for (int i = 2; i < 1000; i++) {
            int fib = fibList.get(i - 1) + fibList.get(i - 2);
            if (fib > 1000000000) {
                break;
            }
            fibList.add(fib);
        }   

        Scanner scanner = new Scanner(System.in);

        while (true) {
            try {
                int N = scanner.nextInt();
                for (int i = 0; i < N; i++) {
                    int ans = 0;
                    int num = scanner.nextInt();
                    int NUM = num;
                    
                    for (int j = fibList.size() - 1; j >= 0; j--) {
                        if (fibList.get(j) <= num && (j == fibList.size() - 1 || fibList.get(j + 1) >= num)) {
                            for (int k = j + 2; k >= 0; k--) {
                                if (fibList.get(k) <= num && (k == fibList.size() - 1 || fibList.get(k + 1) >= num)) {
                                    num -= fibList.get(k);
                                    ans += Math.pow(10, k - 2);
                                }
                                if (num == 0) {
                                    break;
                                }
                            }
                        }
                    }

                    System.out.printf("%d = %d (fib)%n", NUM, ans);
                }
            } catch (Exception e) {
                break;
            }
        }
    }
}
