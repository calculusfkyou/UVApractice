import java.util.ArrayList;
import java.util.Scanner;

public class UVA490 {
    public static void main(String[] args){
        ArrayList<String> sentences = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        while(true){
            try{
                String s = scanner.nextLine();
                sentences.add(s);
            }catch(Exception e){
                break;
            }
        }
        // 計算最長的句子長度
        int longest = 0;
        for (String sentence : sentences) {
            if (sentence.length() > longest) {
                longest = sentence.length();
            }
        }
        // 建立二維字符數組
        char[][] temp = new char[longest][sentences.size()];
        // 將字串轉換為二維字符數組
        for (int i = 0; i < sentences.size(); i++) {
            String subsen = sentences.get(i);
            for (int j = 0; j < subsen.length(); j++) {
                temp[j][i] = subsen.charAt(j);
            }
        }
        // 輸出旋轉後的文本
        for (int i = 0; i < temp.length; i++) {
            for (int j = temp[i].length - 1; j >= 0; j--) {
                if (temp[i][j] == '\0') {
                    System.out.print(" ");
                } else {
                    System.out.print(temp[i][j]);
                }
            }
            System.out.println();
        }
        scanner.close();
    }
}
