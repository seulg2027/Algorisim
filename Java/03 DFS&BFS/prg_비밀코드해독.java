/**
30C5 = 30 * 29 * 28 * 27 * 26 / 5 * 4 * 3 * 2 -> 약 150,000
모든 경우의 수를 계산해도 괜찮다.
*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class prg_비밀코드해독 {
    class Solution {
        int N;
        int[] output = new int[5];
        int[] answers;
        int answer = 0;
        
        public int solution(int n, int[][] q, int[] ans) {
            N = n;
            answers = ans.clone();
            getSecretCode(0, 1, q);
            
            return answer;
        }
        
        private void getSecretCode(int cnt, int start, int[][] q) {
            if (cnt == 5) {
                for (var j = 0; j < q.length; j++) {
                    List<Integer> a = new ArrayList<>(Arrays.asList(Arrays.stream(output).boxed().toArray(Integer[]::new)));
                    List<Integer> b = new ArrayList<>(Arrays.asList(Arrays.stream(q[j]).boxed().toArray(Integer[]::new)));
                    a.retainAll(b); // 교집합 구하기
                    
                    if (a.size() != answers[j]) return;
                }
                answer++;
                return;
            }
            
            for (int i = start; i < N + 1; i++) {
                output[cnt] = i;
                getSecretCode(cnt + 1, i + 1, q);
            }
        }
    }
}
