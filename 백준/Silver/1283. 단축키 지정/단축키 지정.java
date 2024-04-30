import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] input = new String[N];
        HashMap<String, String> dc = new HashMap<>();
        for(int i=0; i<N; i++){
            String tmp = br.readLine();
            input[i] = tmp;
            String[] splitInput = tmp.split(" ");
            int indexNum = 0;
            boolean flag = false;
            for(int j=0; j<splitInput.length; j++){ //첫번째 숫자가 단축키가 될 수 있는지 확인
                if(!dc.containsKey(splitInput[j].substring(0,1).toLowerCase())){
                    dc.put(splitInput[j].substring(0,1).toLowerCase(), tmp);
                    flag = true;
                    break;
                }
                indexNum += (splitInput[j].length()+1);
            }
            if(!flag){
                indexNum = 0;
                for(int j=0; j<splitInput.length; j++){
                    for(int k=1; k<splitInput[j].length(); k++){
                        if(!dc.containsKey(splitInput[j].substring(k,k+1).toLowerCase())){
                            dc.put(splitInput[j].substring(k,k+1).toLowerCase(), tmp);
                            indexNum += 1;
                            flag = true;
                            break;
                        }
                        indexNum += 1;
                    }
                    if(flag){
                        break;
                    }
                    indexNum += 2;
                }

            }

            if(!flag){
                System.out.println(tmp);
            }else{
                String result = tmp.substring(0,indexNum)+"["+tmp.substring(indexNum,indexNum+1)+"]"+tmp.substring(indexNum+1,tmp.length());
                System.out.println(result);
            }
        }


    }

}
