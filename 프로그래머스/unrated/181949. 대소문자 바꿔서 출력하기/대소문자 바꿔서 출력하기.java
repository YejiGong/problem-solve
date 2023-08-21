import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String ans = "";
        for(char x:a.toCharArray()){
            if(Character.isLowerCase(x)){
                ans += Character.toUpperCase(x);
            }else{
                ans += Character.toLowerCase(x);
            }
        }
        System.out.println(ans);
    }
}