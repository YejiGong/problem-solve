import java.util.*;

class Solution {
     public String solution(String p) {
        if (check(p)) return p;
        else return dfs(p);
    }

    private static boolean check(String s) {
        Deque<Character> queue = new LinkedList<Character>();
        for(int i=0; i<s.length(); i++){
            char str = s.charAt(i);
            if(str=='('){
                queue.offer(str);
            }else{
                if(queue.isEmpty()){
                    return false;
                }
                else{
                    queue.pollLast();
                    continue;
                }
            }
        }
        return true;
    }

    private static String dfs(String s) {
        if(s.length()==0) return s;
        
        String u =""; String v="";
        int cnt1=0; int cnt2=0;
        for(int i=0; i<s.length(); i++){
            char str = s.charAt(i);
            if(str=='('){
                cnt1++;
            }else{
                cnt2++;
            }
            if((cnt1>0 && cnt2>0) && (cnt1==cnt2)){
                u = s.substring(0, i+1);
                if (i<s.length()-1) v = s.substring(i+1,s.length());
                break;
            }
        }
        
        if (check(u)) return u+dfs(v);
        else{
            String tmp = "(";
            tmp += dfs(v);
            tmp += ")";
            u = u.substring(1,u.length()-1);
            u = u.replace("(",".");
            u = u.replace(")","(");
            u = u.replace(".",")");
            tmp += u;
            return tmp;
        }
    }
}