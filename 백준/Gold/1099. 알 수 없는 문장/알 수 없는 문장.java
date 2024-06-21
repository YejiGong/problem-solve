import java.io.*;
import java.util.*;

public class Main {
    public static String fullWord;
    public static int N;
    public static HashMap<String, List<String>> map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        fullWord = br.readLine();
        N = Integer.parseInt(br.readLine());
        map = new HashMap<>();
        for(int i=0; i<N; i++){
            String word = br.readLine();
            char[] tmpWord = word.toCharArray();
            Arrays.sort(tmpWord);
            String tmp = String.valueOf(tmpWord);
            if(map.containsKey(tmp)){
                List<String> lst = new LinkedList<String>();
                lst.addAll(map.get(tmp));
                lst.add(word);
                map.put(tmp, lst);
            }else{
                map.put(tmp, List.of(word));
            }
        }
        int[] dp = new int[fullWord.length()];
        Arrays.fill(dp, Integer.MAX_VALUE);
        if(fullWord.length()==1){
            int result = getScore(fullWord);
            if(result!=Integer.MAX_VALUE){
                dp[0] = result;
            }
        }else {
            for (int i = 0; i < fullWord.length(); i++) {
                for (int j = 0; j <= i; j++) {
                    String substr = fullWord.substring(j, i+1);
                    int result = getScore(substr);
                    if (result != Integer.MAX_VALUE) {
                        if (j == 0) {
                            dp[i] = Math.min(dp[i], result);
                        } else if (dp[j - 1] != Integer.MAX_VALUE) {
                            dp[i] = Math.min(dp[i], dp[j - 1] + result);
                        }
                    }
                }
            }
        }
        if(dp[fullWord.length()-1]!=Integer.MAX_VALUE) {
            System.out.println(dp[fullWord.length() - 1]);
        }else{
            System.out.println(-1);
        }


    }
    public static int getScore(String word){
        char[] tmp = word.toCharArray();
        Arrays.sort(tmp);
        String tmpWord = String.valueOf(tmp); //정렬값
        int result = Integer.MAX_VALUE;
        for(Map.Entry<String, List<String>> entry : map.entrySet()){
            if(entry.getKey().equals(tmpWord)){
                for(String w : entry.getValue()){
                    result = Math.min(result, calcul(w, word));
                }
            }
        }
        return result;
    }

    public static int calcul(String word, String tmpWord){
        int result=0;
        for(int i=0; i<word.length(); i++){
            if(word.charAt(i) != tmpWord.charAt(i)){
                result++;
            }
        }

        return result;
    }


}

