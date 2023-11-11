import java.util.Scanner;

public class UVA10071 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true){
            try{
                int a = sc.nextInt(), b = sc.nextInt();
                System.out.println(a*b*2);
            }catch(Exception e){
                break;
            }
        }
        sc.close();
    }
}
