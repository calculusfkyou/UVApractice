import java.util.Scanner;

public class UVA10019 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for(int i = 0; i < n; i++){
            int m = scanner.nextInt();
            int subm = m;
            int count = 0;
            while(subm > 0){
                if(subm % 2 == 1) count += 1;
                subm = subm / 2;
            }
            System.out.printf(count+" ");
            count = 0;
            while(m > 0){
                int temp = m % 10;
                while(temp > 0){
                    if(temp % 2 == 1) count += 1;
                    temp = temp / 2;
                }
                m = m / 10;
            }
            System.out.printf(count+"\n");
        }
        scanner.close();
    }
}