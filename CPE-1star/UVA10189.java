import java.util.Scanner;

public class UVA10189 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int field = 0, h, w;
        while (sc.hasNextInt() && (h = sc.nextInt()) != 0 && (w = sc.nextInt()) != 0) {
            if (field != 0)
                System.out.println("");
            char arr[][] = new char[h][w];
            // 讀入地圖
            for (int i = 0; i < h; i++) {
                String temp = sc.next();
                for (int j = 0; j < w; j++) {
                    arr[i][j] = temp.charAt(j);
                }
            }
            // Output
            System.out.println("Field #" + (++field) + ":");
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    int ans = 0;
                    if (i - 1 >= 0 && arr[i - 1][j] == '*')
                        ans++;
                    if (i + 1 < h && arr[i + 1][j] == '*')
                        ans++;
                    if (j - 1 >= 0 && arr[i][j - 1] == '*')
                        ans++;
                    if (j + 1 < w && arr[i][j + 1] == '*')
                        ans++;

                    if ((j + 1 < w && i + 1 < h) && arr[i + 1][j + 1] == '*')
                        ans++;
                    if ((j + 1 < w && i - 1 >= 0) && arr[i - 1][j + 1] == '*')
                        ans++;
                    if ((j - 1 >= 0 && i + 1 < h) && arr[i + 1][j - 1] == '*')
                        ans++;
                    if ((j - 1 >= 0 && i - 1 >= 0) && arr[i - 1][j - 1] == '*')
                        ans++;

                    if (arr[i][j] == '*')
                        System.out.print("*");
                    else
                        System.out.print(ans);
                }
                System.out.println("");
            }
        }
        sc.close();
    }
}