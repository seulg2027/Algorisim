/**
 * prg_140107
 * bfs로 시도해보았으나, 구냥 찐 구현.. 생각을 더 했었어야했음
 */
import java.util.*;

public class prg_140107 {
    public long solution(int k, int d) {
        long answer = 0;
        
        // x 좌표를 k 배수만큼 증가
        for(int i=0; i<=d; i+=k){
            int yMaxDistance = yPossibleDistance(i, d);
            answer += yPossibleCount(yMaxDistance, k);
        }
        
        return answer;
    }
    
    // 가능한 y 거리 구하기
    private static int yPossibleDistance(int x, int d) {
        int result = (int) Math.sqrt(Math.pow(d, 2) - Math.pow(x, 2)); 
        
        return result;
    }
    
    // y/k 구하기
    private static int yPossibleCount(int y, int k) {
        int res = (y/k);
        return res+1;
    }
}

// 내가 풀었던 코드
// 시간초과,,
class Solution {
    public long solution(int k, int d) {
        long answer = 0;
        
        int[] dx = {0, 1};
        int[] dy = {1, 0};
        
        Queue<List> queue = new LinkedList<>();
        queue.add(Arrays.asList(0, 0));
        ArrayList<List> res = new ArrayList<>();
        
        while (!queue.isEmpty()) {
            List<?> now = queue.poll();
            if (!res.contains(now)) {
                //System.out.println(now);
                res.add(now);
            }
            
            for (int i=0; i<2; i++) {
                double nx = dx[i]*k + (int)now.get(0);
                double ny = dy[i]*k + (int)now.get(1);
                double dist = Math.sqrt(Math.pow(nx, 2) + Math.pow(ny, 2));
                
                if ((int) Math.ceil(dist) <= d) {
                    queue.add(Arrays.asList((int)nx, (int)ny));
                }
            }
        }
        answer = res.size();
        
        return answer;
    }
}