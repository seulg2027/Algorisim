/**
 * prg_12906
 * 같은 숫자는 싫어
 * Stack을 활용하는 문제
 */
import java.util.*;

public class prg_12906 {

    public int[] solution(int []arr) {
        int[] answer = {};
        Stack<Integer> stack = new Stack<>();
        
        // 이전에 들어갔던 숫자면 넣지 않고, 들어가지 않은 숫자만 넣기
        for (int a=0; a<arr.length; a++) {
            if (!stack.isEmpty()) {
                if (stack.peek() != arr[a]) {
                    stack.push(arr[a]);
                }
            } else {
                stack.push(arr[a]);
            }
        }
        answer = new int[stack.size()];
        
        // 정답 도출하기
        for (int i=0; i<stack.size(); i++) {
            answer[i] = stack.get(i);
        }
        
        return answer;
    }

    // 다른 사람 풀이
    public static int[] main(int []arr) {
        // ArrayList로 해도 시간 초과 안남.
        ArrayList<Integer> answerList = new ArrayList<Integer>();
        
        int value = -1;
        for(int i=0; i<arr.length; i++) {
            if(arr[i] != value) {
                answerList.add(arr[i]);
                value = arr[i];
            }
        }
        return answerList.stream().mapToInt(i->i).toArray();
    }
}