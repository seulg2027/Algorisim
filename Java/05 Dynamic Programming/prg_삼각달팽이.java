/**
n개 배열
n = 4
4 3 2 1 = 10
*/
public class prg_삼각달팽이 {
    class Solution {
        public int[] solution(int n) {
            int[] answer = new int[n * (n+1) / 2];
            int[][] dp = new int[n][n];
            int cnt = 1, row = n; // cnt : 몇번째인지, row : 해당 줄에 몇 개가 넣어져야하는지
            int arrow = 0; // 0 : 아래로, 1 : 오른쪽으로, 2 : 위로
            int a = 0, b = 0;
            dp[a][b] = 1;
            
            for (int i = 1; i < n * (n+1) / 2; i++)  {
                cnt += 1;
                if (arrow == 0) {
                    a += 1;
                    if (cnt == row) {
                        arrow = 1;
                    }
                } else if (arrow == 1) {
                    b += 1;
                    if (cnt == row) {
                        arrow = 2;
                    }
                } else if (arrow == 2) {
                    a -= 1;
                    b -= 1;
                    if (cnt == row) {
                        arrow = 0;
                    }
                }
                dp[a][b] = i + 1;
                
                if (cnt == row) {
                    cnt = 0;
                    row -= 1;
                }
            }
            
            int z = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j <= i; j++) {
                    if (dp[i][j] != 0) {
                        answer[z] = dp[i][j];
                        z++;
                    }
                }
            }
            
            return answer;
        }
    }
}
