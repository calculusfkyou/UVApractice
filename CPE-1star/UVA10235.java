import java.util.Scanner;

public class UVA10235 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            String n = sc.next(); // 讀入數字
            String r = ""; // 反轉後的數字

            // 數字反轉
            for (int i = n.length() - 1; i >= 0; i--) {
                r = r + n.charAt(i);
            }

            if (isPrime(Integer.parseInt(n)) && isPrime(Integer.parseInt(r)) && !n.equals(r))
                System.out.println(n + " is emirp."); // r,n皆為質，且r!=n
            else if (isPrime(Integer.parseInt(n)))
                System.out.println(n + " is prime."); // n為質數
            else
                System.out.println(n + " is not prime."); // 都不是

        }
        sc.close();
    }

    // 質數判斷
    public static boolean isPrime(int n) {
        boolean flag = true;
        // 最多判斷到n/2就可以停止。
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                flag = false;
                break;
            }
        }
        return flag;
    }
}