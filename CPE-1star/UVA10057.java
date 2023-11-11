// 每個資料的第一個數字為有多少資料需要被處理(cases)，接下來就是資料(X1、X2 ... Xn)。

// 1. 找出中位數。

// 2. 計算有幾個和中位數一樣的數字。資料(cases)是偶數個時中位數有2個、資料是奇數個時中位數有1個。

// 3. 找出可能有幾種最小值(包含不在所輸入的資料裡面)，資料為奇數個時答案為1，資料為偶數個時答案為2個中位數相減加1。
import java.util.Scanner;
import java.util.Arrays;

public class UVA10057 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {
            int cases = sc.nextInt();

            int arr[] = new int[cases];
            for (int i = 0; i < arr.length; i++) {
                arr[i] = sc.nextInt();
            }
            Arrays.sort(arr);

            // A(中位數)
            int mid = arr[(arr.length - 1) / 2];
            int mid2 = arr[(arr.length) / 2];

            // same as A(相同數字、同是中位數)
            int count = 0;
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] == mid || arr[i] == mid2)
                    count++;
            }

            // 有幾種最小可能
            int D = mid2 - mid + 1;

            // 結果輸出
            System.out.println(mid + " " + count + " " + D);

        }
        sc.close();
    }
}