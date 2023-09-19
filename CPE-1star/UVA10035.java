import java.util.Scanner;

public class UVA10035 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        while(true){
            try{
                int a = scanner.nextInt();
                int b = scanner.nextInt();
                if(a == 0 & b == 0) break;
                int carry = 0,carrydigit = 0;
                while (a > 0 || b > 0){
                    int digitsum = a % 10 + b % 10 + carrydigit;
                    if(digitsum >= 10){
                        carry+=1;
                        carrydigit = 1;
                    }
                    else carrydigit = 0;
                    a = a / 10;
                    b = b / 10;
                }
                if (carry == 0) System.out.println("No carry operation.");
                else if(carry == 1) System.out.println("1 carry operation.");
                else System.out.printf("%d carry operations.\n",carry);
            }catch(Exception e){
                break;
            }
        }
        scanner.close();
    }
}
