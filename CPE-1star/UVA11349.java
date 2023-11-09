// 要用long，因為數字可能很多。
// 把2維矩陣變成1維矩陣，判斷首尾數值是否相同。
import java.util.Scanner;

public class UVA11349{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		
		int cases=Integer.parseInt(sc.next()); //總共多少Case。
		for(int i=0;i<cases;i++){
			String temp1=sc.next(),temp2=sc.next(); //進行假抓(N、=)。
			
			int n=Integer.parseInt(sc.next()); //矩陣大小。
			long[] arr=new long[n*n];
			
			int size=n*n;
			for(int j=0;j<size;j++) 
                arr[j]=Long.parseLong(sc.next()); //把數值讀到矩陣。
			
			//進行判斷。
			boolean flag=true;
			for(int j=0;j<size;j++){
				if(arr[j]<0 || (arr[j]!=arr[size-1-j])){
					flag=false;
					break;
				}
			}
			
			//結果輸出。
			if(flag) System.out.println("Test #"+(i+1)+": Symmetric.");
			else System.out.println("Test #"+(i+1)+": Non-symmetric.");
		}
        sc.close();
	}
}