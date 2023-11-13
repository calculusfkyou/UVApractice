import java.util.Scanner;

public class UVA10242 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            try {
                // 讀取輸入的 8 個浮點數
                double x1 = scanner.nextDouble();
                double y1 = scanner.nextDouble();
                double x2 = scanner.nextDouble();
                double y2 = scanner.nextDouble();
                double x3 = scanner.nextDouble();
                double y3 = scanner.nextDouble();
                double x4 = scanner.nextDouble();
                double y4 = scanner.nextDouble();

                // 進行點的反射計算
                double x, y;

                if (x1 == x3 && y1 == y3) {
                    x = x2 + x4 - x3;
                    y = y2 + y4 - y3;
                } else if (x1 == x4 && y1 == y4) {
                    x = x2 + x3 - x4;
                    y = y2 + y3 - y4;
                } else if (x2 == x3 && y2 == y3) {
                    x = x1 + x4 - x3;
                    y = y1 + y4 - y3;
                } else {
                    x = x1 + x3 - x4;
                    y = y1 + y3 - y4;
                }

                // 輸出結果
                System.out.printf("%.3f %.3f%n", x, y);
            } catch (Exception e) {
                break;
            }
        }

        scanner.close();
    }
}
