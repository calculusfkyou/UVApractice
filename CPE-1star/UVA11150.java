import java.util.Scanner;

public class UVA11150 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        while(true){
            try{
                int n=sc.nextInt();
                System.out.println((n*3)/2);    
            }catch(Exception e){
                break;
            }
        } 
        sc.close();   
    }
}
