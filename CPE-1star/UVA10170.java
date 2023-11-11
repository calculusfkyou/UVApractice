import java.util.Scanner;

public class UVA10170 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            long S = sc.nextLong();
            long D = sc.nextLong();
            long Stemp = S;
            long count = S;
            while (Stemp < D) {
                count++;
                Stemp += count;
            }
            System.out.println(count);
        }
        sc.close();
    }
}
