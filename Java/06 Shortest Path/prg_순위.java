/**
A > B, B > C
결과 : A > C
플로이드 워셜이래,,
*/
class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        int[][] graph = new int[n+1][n+1];
        
        for (var i=0; i<results.length; i++) {
            graph[results[i][0]][results[i][1]] = 1; // 승리
            graph[results[i][1]][results[i][0]] = -1; // 패배
        }
        
        // 100**3 = 1,000,000 시간복잡도
        for (var k=1; k<=n; k++) {
            for (var i=1; i<=n; i++) {
                for (var j=1; j<=n; j++) {
                    if (graph[i][k] == 1 && graph[k][j] == 1) {
                        graph[i][j] = 1;
                        graph[j][i] = -1;
                    } else if (graph[i][k] == -1 && graph[k][j] == -1) {
                        graph[i][j] = -1;
                        graph[j][i] = 1;
                    }
                }
            }
        }
        
        //System.out.println(Arrays.deepToString(graph));
        
        for (var i=1; i<=n; i++) {
            var cnt = 0;
            for (var j=1; j<=n; j++) {
                if (i == j) continue;
                
                if (graph[i][j] == 1 || graph[i][j] == -1) cnt++;
            }
            if (cnt == n-1) {
                answer += 1;
            }
        }
        
        return answer;
    }
}