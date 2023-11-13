import java.util.Scanner;

public class UVA10931{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		
		int num;
		while(sc.hasNext() && (num=sc.nextInt())!=0){
			String st=Integer.toBinaryString(num);
			
			//計算有多少1
			int count=0;
			for(int i=0;i<st.length();i++){
				if(st.charAt(i)=='1') count++;
			}
			
			//結果輸出
			System.out.println("The parity of "+st+" is "+count+" (mod 2).");
		}

        sc.close();
	}
}