import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Stack<Character> stack = new Stack<>();
        String str = br.readLine();
        String bomb = br.readLine();
        for(int i=str.length()-1; i>=0; i--){
            stack.push(str.charAt(i));
            if(stack.size()>=bomb.length() && stack.peek() == bomb.charAt(0)){
                boolean check = true;
                for(int j=1; j<bomb.length(); j++){
                    if(stack.get(stack.size()-j-1) != bomb.charAt(j)){
                        check = false;
                        break;
                    }
                }
                if(check){
                    for(int j=0; j<bomb.length(); j++){
                        stack.pop();
                    }
                }
            }
        }
        if(stack.isEmpty()) System.out.println("FRULA");
        else{
            while(!stack.isEmpty()){
                sb.append(stack.pop());
            } System.out.println(sb.toString());
        }
    }

}
