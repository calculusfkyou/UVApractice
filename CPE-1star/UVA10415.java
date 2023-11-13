import java.util.Scanner;

public class UVA10415 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        int cases = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < cases; i++) {
            // 紀錄每個英文字母所會按到的鍵。
            String[] finger = { "c0111001111", "d0111001110", "e0111001100", "f0111001000", "g0111000000",
                    "a0110000000", "b0100000000", "C0010000000", "D1111001110", "E1111001100", "F1111001000",
                    "G1111000000", "A1110000000", "B1100000000" };

            int[] count = new int[10]; // 紀錄每個鍵所按的次數。
            String st = sc.nextLine();
            String current = "0000000000"; // 目前手指所按的鍵。
            for (int j = 0; j < st.length(); j++) {
                String temp = "";
                // 找出目前的英文字母所需要案的鍵
                for (int k = 0; k < finger.length; k++) {
                    if (st.charAt(j) == finger[k].charAt(0)) {
                        temp = finger[k];
                        break;
                    }
                }
                // 判斷次數是否++。
                StringBuilder stB = new StringBuilder(temp);
                temp = stB.substring(1);
                for (int k = 0; k < 10; k++) {
                    if (current.charAt(k) != temp.charAt(k) && temp.charAt(k) == '1')
                        count[k]++;
                }
                current = temp;
            }

            // Output
            for (int j = 0; j < 10; j++) {
                if (j != 9)
                    System.out.print(count[j] + " ");
                else
                    System.out.print(count[j]);
            }
            System.out.println("");
        }
        sc.close();
    }
}