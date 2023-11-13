import java.util.Scanner;
import java.util.Stack;
import java.util.Iterator;

public class UVA10190 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNextInt()) {
            long n = sc.nextLong();
            long m = sc.nextLong();

            // Stack因為繼承於Vector，所以Vector的功能也可以使用。
            Stack<Long> stack = new Stack<Long>(); // Ps也可以使用一般陣列紀錄。
            long temp = 1;

            /*
             * 1. m!=0 : 乘數不為零
             * 2. m!=1 : 乘數為1，不管乘上甚麼永遠都是1。
             * 3. n>=m : 因為m^x=n，所以n一定大於等於m。
             * 4. temp<=n : temp會越乘越大，當超過或等於n時即可停止迴圈。
             */
            while (m != 0 && m != 1 && n >= m && temp <= n) {
                stack.push(temp);
                temp = temp * m;
            }

            // Output
            Iterator<Long> it = stack.iterator();
            if (!stack.empty() && stack.lastElement() == n) {
                while (true) {
                    long Stemp = stack.pop();
                    System.out.print(Stemp);
                    if (Stemp != 1)
                        System.out.print(" ");
                    else
                        break;
                }
                System.out.println("");
            } else {
                System.out.println("Boring!");
            }
        }
        sc.close();
    }
}