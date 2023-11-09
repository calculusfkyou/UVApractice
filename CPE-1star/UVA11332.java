import java.util.*;

public class UVA11332 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            try {
                String n = sc.next();
                if (n.equals("0"))
                    break;

                int sum = 0;
                while (n.length() != 1) {
                    for (int i = 0; i < n.length(); i++)
                        sum += n.charAt(i) - 48;
                    n = Integer.toString(sum);
                    sum = 0;
                }
                System.out.println(n);
            } catch (Exception e) {
                break;
            }
        }
        sc.close();
    }
}