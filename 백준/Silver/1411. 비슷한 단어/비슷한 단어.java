import java.io.*;
import java.util.*;
import java.lang.Math;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashMap<String, Integer> words = new HashMap<>();
        for(int i=0; i<n; i++){
            String str = changeWord(br.readLine());
            if(words.containsKey(str)){
                words.put(str,words.get(str)+1);
            }else{
                words.put(str,1);
            }
        }
        int result = 0;
        for(int value: words.values()){
            result += value*(value-1)/2;
        }
        System.out.println(result);

    }

    public static String changeWord(String str){
        Map<String, String> checkDuplicate = new HashMap<>();
        String changedWord = "";
        for(char c: str.toCharArray()){
            if(checkDuplicate.containsKey(String.valueOf(c))){
                changedWord += checkDuplicate.get(String.valueOf(c));
            }else{
                char newString = (char) (checkDuplicate.size()+'a');
                checkDuplicate.put(String.valueOf(c), String.valueOf(newString));
                changedWord += String.valueOf(newString);
            }
        }
        return changedWord;
    }

}
