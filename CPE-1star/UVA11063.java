import java.util.*;

public class UVA11063 {
    public static void main(String[] args) {
        int caseNum = 1;
        Scanner sc = new Scanner(System.in);
        while (true) {
            try {
                int check = 1;
                int n = sc.nextInt();
                int[] nums = new int[n];
                for (int i = 0; i < n; i++) {
                    nums[i] = sc.nextInt();
                    if (nums[i] < 1)
                        check = 0;
                    if (i != 0 && nums[i - 1] >= nums[i])
                        check = 0;
                }
                int[] sum = new int[200001];
                Arrays.fill(sum, 0);
                int temp = 0;
                if (check == 1) {
                    for (int i = 0; i < n; i++) {
                        for (int j = i; j < n; j++) {
                            temp = nums[i] + nums[j];
                            if (sum[temp] == 0) {
                                sum[temp] = 1;
                            } else {
                                check = 0;
                                break;
                            }
                        }
                    }
                }
                if (check == 1)
                    System.out.println("Case #" + caseNum + ": It is a B2-Sequence.");
                else
                    System.out.println("Case #" + caseNum + ": It is not a B2-Sequence.");
                caseNum+=1;
                System.out.println();
            } catch (Exception e) {
                break;
            }
        }
        sc.close();
    }
}
