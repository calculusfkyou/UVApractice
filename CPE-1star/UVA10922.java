import java.util.Scanner;

public class UVA10922 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            try {
                String n = sc.next();
                if (n.equals("0"))
                    break;
                int count = 0;
                String temp = n;
                while (true) {
                    int total = 0;
                    for (int i = 0; i < temp.length(); i++) {
                        total = total + temp.charAt(i) - 48;
                    }
                    if (total % 9 == 0) {
                        count++;
                        if (total == 9)
                            break;
                        else
                            temp = Integer.toString(total);
                    } else {
                        break;
                    }
                }
                if (count != 0)
                    System.out.println(n + " is a multiple of 9 and has 9-degree " + count + ".");
                else
                    System.out.println(n + " is not a multiple of 9.");
            } catch (Exception e) {
                break;
            }
        }
        sc.close();
    }
}
