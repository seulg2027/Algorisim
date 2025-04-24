/**
 * 1, 2, 3
 * 12, 21, 13, 31, 23, 32
 * 1, 2, 4
 * 3 5 6
 */
import java.io.*;
import java.util.*;

public class boj_링크와스타트 {
    static int n, minValue;
    static int[][] capacities;
    static boolean[] isvisited;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new BufferedReader(new InputStreamReader(System.in)));
        BufferedWriter bw = new BufferedWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

        n = Integer.parseInt(br.readLine());
        minValue = Integer.MAX_VALUE;

        capacities = new int[n+1][n+1];
        isvisited = new boolean[n+1];

        for (var i = 1; i < n+1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (var j = 1; j < n+1; j++) {
                capacities[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (var z = 1; z < n/2 + 1; z++) {
            combination(1, 0, z);
        }
        bw.write(String.valueOf(minValue) + "\n");

        bw.flush();
        bw.close();
    }

    static void combination(int idx, int cnt, int num) {
        if (cnt == num) {
            calculateDiff();
            return;
        }

        for (var i = idx; i < n+1; i++) {
            if (!isvisited[i]) {
                isvisited[i] = true;
                combination(i + 1, cnt + 1, num);
                isvisited[i] = false;
            }
        }
    }

    static void calculateDiff() {
        int linkTeamCapacity = 0, startTeamCapacity = 0;

        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < i; j++) {
                // 스타트 팀인 경우
                if (isvisited[i] && isvisited[j]) {
                    startTeamCapacity += (capacities[i][j] + capacities[j][i]);
                // 링크 팀인 경우
                } else if (!isvisited[i] && !isvisited[j]) {
                    linkTeamCapacity += (capacities[i][j] + capacities[j][i]);
                }
            }
        }

        minValue = Math.min(minValue, Math.abs(startTeamCapacity - linkTeamCapacity));

        if (minValue == 0) {
            System.out.println(minValue);
            System.exit(0);
        }
    }
}