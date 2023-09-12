import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class UVA100 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        while (true){
            try{
                ArrayList<Integer> temp = new ArrayList<Integer>();
                ArrayList<Integer> temp2 = new ArrayList<Integer>();
                int n = scanner.nextInt();
                int m = scanner.nextInt();
                int subn = n, subm = m;
                if (n > m){
                    int tempp = n;
                    n = m;
                    m = tempp;
                }
                for (int i = n; i <= m; i++){
                    if (i == 1){
                        continue;
                    }
                    else{
                        temp.add(i);
                        while (true){
                            if (i ==1)
                                break;
                            else{
                                if (i % 2 != 0){
                                    i = i * 3 + 1;
                                    temp.add(i);
                                }
                                else{
                                    i = i / 2;
                                    temp.add(i);
                                }
                            }
                        }
                        temp2.add(temp.size());
                        temp.clear();
                    }
                }
                System.out.printf("%d %d %d\n",subn,subm,Collections.max(temp2));
                temp2.clear();
            }
            catch (Exception e){
                break;
            }
        }
        scanner.close();
    }
}
