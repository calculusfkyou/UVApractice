import java.util.Scanner;

public class UVA299 {
    public static int bbsort(int[] subnum) {
        int count = 0;
        for (int k = 0; k < subnum.length - 1; k++) {
            for (int j = 0; j < subnum.length - 1; j++) {
                if (subnum[j] > subnum[j + 1]) {
                    int temp = subnum[j + 1];
                    subnum[j + 1] = subnum[j];
                    subnum[j] = temp;
                    count++;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            try {
                int n = scanner.nextInt();
                for (int i = 0; i < n; i++) {
                    int l = scanner.nextInt();
                    int[] nums = new int[l];
                    for (int j = 0; j < l; j++) {
                        nums[j] = scanner.nextInt();
                    }
                    System.out.println("Optimal train swapping takes " + bbsort(nums) + " swaps.");
                }
            } catch (Exception e) {
                break;
            }
        }
        scanner.close();
    }
}
