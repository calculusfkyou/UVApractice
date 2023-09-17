import java.util.Scanner;

public class UVA272 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int count = 0;
        while (true){
            try{
                String text = scanner.nextLine();
                StringBuilder result = new StringBuilder();
                for(int i = 0; i < text.length(); i++){
                    char c = text.charAt(i);
                    if(c == '"'){
                        if(count % 2 == 0){
                            result.append("``");
                        }
                        else{
                            result.append("''");
                        }
                        count++;
                    }
                    else{
                        result.append(c);
                    }
                }
                System.out.println(result.toString());
            }
            catch(Exception e){
                break;
            }
        }
        scanner.close();
    }
}
