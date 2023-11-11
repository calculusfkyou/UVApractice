import java.util.*;

public class UVA10038 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            try {
                int n = sc.nextInt();
                int[] nums = new int[n];
                int[] diff = new int[n - 1];
                for (int i = 0; i < n; i++) {
                    nums[i] = sc.nextInt();
                    if (i != 0)
                        diff[i - 1] = Math.abs(nums[i - 1] - nums[i]);
                }
                Arrays.sort(diff);
                boolean check = true;
                for (int i = 1; i <= diff.length; i++) {
                    if (diff[i - 1] != i) {
                        check = false;
                        break;
                    }
                }
                if (check)
                    System.out.println("Jolly");
                else
                    System.out.println("Not jolly");
            } catch (Exception e) {
                break;
            }
        }
        sc.close();
    }
}
