import static java.lang.Math.min;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String document = br.readLine();
        String searchKeyword = br.readLine();
        int searchKeywordLength = searchKeyword.length();
        int cnt = 0;
        int prevEnd = -1;
        for(int i=0; i<document.length(); i++){
            if(document.substring(i,min(document.length(),i+searchKeywordLength)).equals(searchKeyword)){
                if(i > prevEnd){
                    cnt++;
                    prevEnd = i+searchKeywordLength -1;
                }
            }
        }
        System.out.println(cnt);
    }
}
