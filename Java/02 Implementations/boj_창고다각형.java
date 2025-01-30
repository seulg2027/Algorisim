/**
 * 1. 가장 긴 막대를 기준으로!
 * 2. 왼쪽은 왼쪽부터 높아지는
 * 3. 오른쪽은 오른쪽부터 높아지는
 */
import java.io.*;
import java.util.*;

public class boj_창고다각형 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[][] list = new int[n][2];
        int maxValue = 0, idx = 0;

        for (var i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            list[i][0] = Integer.parseInt(st.nextToken());
            list[i][1] = Integer.parseInt(st.nextToken());
            if (maxValue < list[i][1]) {
                maxValue = Math.max(maxValue, list[i][1]);
                idx = list[i][0];
            }
        }

        Arrays.sort(list, (o1, o2) -> o1[0] - o2[0]);
        int loc = 0, len = 0;
        int height = 0;

        // 왼쪽부터 가장 높은 높이까지 다각형 넓이 구하기
        for (var i = 0; i < n; i++) {
            if (i == 0) { // 첫번째인 경우
                len = list[i][1];
            } else {
                height += len * (list[i][0] - list[i-1][0]);
                if (len < list[i][1]) len = list[i][1];
            }
            // 가장 높은 높이
            if (list[i][0] == idx) {
                loc = i;
                break;
            }
        }

        // 오른쪽부터 가장 높은 높이까지 다각형 넓이 구하기
        for (var j = n-1; j >= loc; j--) {
            if (j == n-1) { // 첫번째인 경우
                len = list[j][1];
            } else {
                height += len * (list[j+1][0] - list[j][0]);
                if (len < list[j][1]) len = list[j][1];
            }
            if (j == loc) {
                height += list[j][1];
            }
        }

        bw.write(String.valueOf(height));

        bw.flush();
        bw.close();
    }
}
