import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
        PriorityQueue<Integer> reverseQueue = new PriorityQueue<Integer>(Collections.reverseOrder());
        List<Integer> result = new LinkedList<Integer>();
        for(int i=0; i<operations.length; i++){
            String[] str = operations[i].split(" ");
            int num = Integer.parseInt(str[1]);
            if(str[0].equals("I")){
                queue.add(num);
                reverseQueue.add(num);
            }else{
                if(num == 1){
                    while(!reverseQueue.isEmpty()){
                        int tmp = reverseQueue.poll();
                        if(!result.contains(tmp)){
                            result.add(tmp);
                            break;
                        }
                    }
                }else{
                    while(!queue.isEmpty()){
                        int tmp = queue.poll();
                        if(!result.contains(tmp)){
                            result.add(tmp);
                            break;
                        }
                    }
                }
            }
        }
        ArrayList<Integer> resultList = new ArrayList<>(queue);
        ArrayList<Integer> resultList2 = new ArrayList<>(reverseQueue);
        resultList.retainAll(resultList2);
        resultList.sort(Comparator.reverseOrder());
        int[] answer = {0,0};
        if(resultList.size()==0){
            
        }
        else if(resultList.size()==1){
            answer[0] = resultList.get(0);
            answer[1] = resultList.get(0);
        }else{
            answer[0] = resultList.get(0);
            answer[1] = resultList.get(resultList.size()-1);
        }
        return answer;
    }
}