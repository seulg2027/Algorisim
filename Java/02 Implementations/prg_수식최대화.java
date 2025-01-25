/**
연산자 우선순위
+ - *
3가지의 연산자 우선순위를 정해서 먼저 풀이
*/
import java.util.ArrayList;
import java.util.Arrays;

public class prg_수식최대화 {
    class Solution {
        String[] output;
        ArrayList<String[]> expArr = new ArrayList<>();
        
        public long solution(String expression) {
            long answer = 0;
            output = new String[3];
            boolean[] visited = new boolean[3];
            permutations(0, new String[]{"+", "-", "*"}, visited);
            
            ArrayList<String> numArr = new ArrayList<>(Arrays.asList(expression.split("[+]|[-]|[*]")));
            ArrayList<String> calArr = new ArrayList<>();
            
            for (int e = 0; e < expression.length(); e++) {
                if (expression.charAt(e) == '+' || expression.charAt(e) == '-' || expression.charAt(e) == '*') {
                    calArr.add(Character.toString(expression.charAt(e)));
                }
            }
            
            for (String[] exp : expArr) { // 연산자 우선순위별로
                long result = 0;
                
                ArrayList<String> numArr2 = new ArrayList<>(numArr);
                ArrayList<String> calArr2 = new ArrayList<>(calArr);
                
                for (String x : exp) {
                    int i = calArr2.indexOf(x);
                    while (i != -1) {
                        if (x.equals("-")) {
                            result = Long.valueOf(numArr2.get(i)) - Long.valueOf(numArr2.get(i+1));
                        } else if (x.equals("+")) {
                            result = Long.valueOf(numArr2.get(i)) + Long.valueOf(numArr2.get(i+1));
                        } else if (x.equals("*")) {
                            result = Long.valueOf(numArr2.get(i)) * Long.valueOf(numArr2.get(i+1));
                        }
                        numArr2.set(i, String.valueOf(result));
                        numArr2.remove(i+1);
                        calArr2.remove(i);
                        
                        i = calArr2.indexOf(x);
                    }
                }
                answer = Math.max(Math.abs(Long.parseLong(numArr2.get(0))), answer);
            }
            
            return answer;
        }
        
        private void permutations(int x, String[] calculator, boolean[] visited) {
            if (x == 3) {
                expArr.add(Arrays.copyOf(output, 3));
                return;
            }
            
            for (var i = 0; i < 3; i++) {
                if (visited[i]) continue;
                
                output[x] = calculator[i];
                visited[i] = true;
                permutations(x + 1, calculator, visited);
                visited[i] = false;
            }
        }
    }
}
