/**
[1, 4], [3, 7] -> 가장 짧은 4
[4, 5], [4, 8]
[5, 12], [10, 14], [11, 13]
*/
import java.util.Arrays;

public class prg_요격시스템 {
    class Solution {
        public int solution(int[][] targets) {
            int answer = 1;
            Arrays.sort(targets, (o1, o2) -> (o1[0] == o2[0] ? o1[1] - o2[1] : o1[0] - o2[0]));
            int e = targets[0][1];
            
            for (int t = 1; t < targets.length; t++) {
                if (targets[t][0] < e) {
                    if (targets[t][1] < e) e = targets[t][1];
                    continue;
                }
                
                e = targets[t][1];
                answer++;
            }
            
            return answer;
        }
    }
}
