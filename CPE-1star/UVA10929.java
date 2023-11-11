import java.util.*;

public class UVA10929 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            try {
                String n = sc.next();
                if (n.equals("0"))
                    break;
                int sum = 0;
                for (int i = 0; i < n.length(); i++) {
                    if (i % 2 == 1)
                        sum += n.charAt(i) - '0';
                    else
                        sum -= (n.charAt(i) - '0');
                }
                if (sum % 11 == 0)
                    System.out.println(n + " is a multiple of 11.");
                else
                    System.out.println(n + " is not a multiple of 11.");
            } catch (Exception e) {
                break;
            }
        }
        sc.close();
    }
}
