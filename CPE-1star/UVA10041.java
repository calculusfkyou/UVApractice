import java.util.Scanner;
import java.util.Arrays;

public class UVA10041 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testCase = scanner.nextInt();
        for (int i = 0; i < testCase; i++) {
            int relatives = scanner.nextInt();
            int[] streetNumber = new int[relatives];
            for (int j = 0; j < relatives; j++) {
                streetNumber[j] = scanner.nextInt();
            }
            Arrays.sort(streetNumber);
            int length = streetNumber.length;
            int medianDistance = 0;
            if (length % 2 == 0) {
                medianDistance = (streetNumber[length / 2] + streetNumber[length / 2 - 1]) / 2;
            } else {
                medianDistance = streetNumber[length / 2];
            }
            int sumOfDistance = 0;
            for (int j = 0; j < length; j++) {
                sumOfDistance += Math.abs(medianDistance - streetNumber[j]);
            }
            System.out.println(sumOfDistance);
        }
        scanner.close();
    }
}