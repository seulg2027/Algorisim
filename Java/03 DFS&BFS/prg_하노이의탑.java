/**
3 (1, 2, 3)
1 3
1 2
3 2
1 3
2 1
2 3
1 3
*/
import java.util.*;

public class prg_하노이의탑 {
    class Solution {
        ArrayList<int[]> result;
        
        public int[][] solution(int n) {
            result = new ArrayList<>();
            
            Hanoi(n, 1, 2, 3);
            
            return result.toArray(new int[result.size()][]);
        }
        
        public void Hanoi(int n, int start, int mid, int to) {
            if (n == 1) {
                result.add(new int[]{start, to});
                return;
            }
            
            Hanoi(n-1, start, to, mid);
            result.add(new int[]{start, to});
            Hanoi(n-1, mid, start, to);
        }
    }
}
