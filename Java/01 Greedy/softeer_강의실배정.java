/**
N <= 1,000,000
오름차순, 오름차순(우선순위) -> 그리디
1. 강의실 배정
2. 그 다음 강의실 배정 가능하면 배정
*/
import java.io.*;
import java.util.*;

public class softeer_강의실배정 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[][] classList = new int[n][2];

        for (var i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            classList[i][0] = Integer.parseInt(st.nextToken());
            classList[i][1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(classList, (o1, o2) -> o1[1] == o2[1] ? o1[0] - o2[0] : o1[1] - o2[1]);
        
        int maxTime = classList[0][1];
        int answer = 1;
        
        for (var i = 1; i < n; i++) {
            if (maxTime <= classList[i][0]) {
                maxTime = classList[i][1];
                answer++;
            }
        }
        bw.write(String.valueOf(answer));
        
        bw.flush();
        bw.close();
    }
}
