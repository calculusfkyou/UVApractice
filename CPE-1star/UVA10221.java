import java.util.Scanner;

public class UVA10221 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double s, distance;
        while (scanner.hasNext()) {
            double r = Double.parseDouble(scanner.next());
            double degree = Double.parseDouble(scanner.next());
            String unit = scanner.next();
            if (unit.equals("min")) {
                degree /= 60;
            }
            s = 2 * Math.PI * (r + 6440) * (degree / 360);
            distance = 2 * (r + 6440) * Math.sin(Math.toRadians(degree / 2));

            System.out.printf("%.6f %.6f%n", Math.round(s * 1e6) / 1e6, Math.round(distance * 1e6) / 1e6);
        }

        scanner.close();
    }
}
