// 小心負數的餘數，不是直接mod，而是要取正後mod再加負號
import java.util.*;

public class UVA11321 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true){
            try{
                int n=sc.nextInt(),m=sc.nextInt();
                if(n==0 && m==0) break;
                ArrayList<Integer> numbers=new ArrayList<Integer>();
                for(int i=0;i<n;i++)
                    numbers.add(sc.nextInt());
                Collections.sort(numbers);

                
            }catch(Exception e){
                break;
            }
        }
    }
}
