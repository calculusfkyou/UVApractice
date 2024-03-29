import java.util.Scanner;

public class UVA10908{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		
		int cases=sc.nextInt();
		for(int CaseCount=0;CaseCount<cases;CaseCount++){
			int m=sc.nextInt(),n=sc.nextInt(),q=sc.nextInt();
			char grid[][]=new char[m][n]; //存放字元。
			for(int i=0;i<m;i++){
				String temp=sc.next();
				for(int j=0;j<n;j++){
					grid[i][j]=temp.charAt(j);
				}
			}
			
			//Output
			System.out.println(m+" "+n+" "+q);
			while((q--)>0){
				int m2=sc.nextInt(),n2=sc.nextInt();
				char cmp=grid[m2][n2]; //需要比較的字元(原點)。
				
				//以原點為中心，比較四周是否跟原點相同。
				int i;
				for(i=0;i<m;i++){
					boolean flag=true;
					for(int j=m2-i;j<=m2+i && flag;j++){
						for(int k=n2-i;k<=n2+i;k++){
							if(j<0 || k<0 || j>=m || k>=n || cmp!=grid[j][k]){
								flag=false;
								break;
							}
						}
					}
					if(!flag) break;
				}
				System.out.println(i*2-1);
			}
		}
        sc.close();
	}
}