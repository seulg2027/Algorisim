/**
 * prg_42584
 * 주식가격
 */
import java.util.*;

public class prg_42584 {

    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        // (1,0) (2,1) (3,2) (2,3) (3,4)
        // (5,0) (4,1) (4,2) (2,3) (1,4)
        Stack<List<Integer>> stack = new Stack<>();
        
        for (int p=0; p<n; p++) {
            // 스택이 비지 않았다면 이전 스택 검사해서 떨어진 주가 확인하기
            if (!stack.isEmpty()) {
                while (true) {
                    if (stack.isEmpty()) break;
                    if ((int)stack.peek().get(0) <= prices[p]) break;
                    
                    // 스택의 마지막 주가가 현재 주가보가 클 때만 실행
                    List<?> num = stack.pop();
                    answer[(int)num.get(1)] = p - (int)num.get(1);
                }
            }
            // 현재 주가는 무조건 push
            stack.push(Arrays.asList(prices[p], p));
        }
        
        int m = stack.size();
        
        for (int i=0; i<m; i++) {
            List<?> now = stack.pop();
            answer[(int)now.get(1)] = n-1 - (int)now.get(1);
        }
        
        return answer;
    }
}