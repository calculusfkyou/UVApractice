import java.util.Scanner;

public class UVA11461 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            try {
                int a = scanner.nextInt(), b = scanner.nextInt();
                if (a == 0 && b == 0)
                    break;
                int countSquareNumbers = 0;
                for (int i = a; i <= b; i++) {
                    double square = Math.sqrt(i);
                    if (square - (int) square == 0)
                        countSquareNumbers += 1;
                }
                System.out.println(countSquareNumbers);
            } catch (Exception e) {
                break;
            }
        }
        scanner.close();
    }
}

// v2

// public class UVA11461 {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);

//         while (true) {
//             int a = scanner.nextInt();
//             int b = scanner.nextInt();

//             if (a == 0 && b == 0) {
//                 break;
//             }

//             int count = 0;

//             // 找出大於等於 a 的最小完全平方數
//             int start = (int) Math.ceil(Math.sqrt(a));
//             // 找出小於等於 b 的最大完全平方數
//             int end = (int) Math.floor(Math.sqrt(b));

//             // 計算位於範圍內的完全平方數的個數
//             count = end - start + 1;

//             System.out.println(count);
//         }

//         scanner.close();
//     }
// }