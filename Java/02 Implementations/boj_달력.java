/**
 *
[오름차순, 내림차순]
2 4
4 5
5 7
5 6
7 9
11 12 // 1~3의 마지막 번호와 차이가 2이상 나면, 새로운 배열 생성
12 12

1 9
2 5
3 4
4 6
8 9
 */
import java.io.*;
import java.util.*;

public class boj_달력 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int answer = 0;
        int N = Integer.parseInt(br.readLine());
        int[][] paper = new int[N][2];
        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            paper[i][0] = Integer.parseInt(st.nextToken());
            paper[i][1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(paper, (o1, o2) -> o1[0] == o2[0] ? o2[1] - o1[1] : o1[0] - o2[0]);

        ArrayList<int[]> graph = new ArrayList<>();
        graph.add(paper[0]);
        int minValue = paper[0][0], maxValue = paper[0][1];

        for (int j=1; j<N; j++) { // 일정 하나씩 돌아가면서 검사
            if (paper[j][0] - maxValue >= 2) { // 마지막 번호와 차이가 2이상 나면, 새롭게 일정 박스 생성
                answer += (maxValue - minValue + 1) * graph.size();
                graph = new ArrayList<>();
                graph.add(paper[j]);
                // min, max 변경하기
                minValue = paper[j][0];
                maxValue = paper[j][1];
                continue;
            }

            boolean flag = false;
            for (int k=0; k<graph.size(); k++) {
                if (graph.get(k)[1] < paper[j][0]) {
                    graph.get(k)[1] = paper[j][1];
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                graph.add(paper[j]);
            }
            maxValue = Math.max(paper[j][1], maxValue);
        }

        answer += (maxValue - minValue + 1) * graph.size();
        System.out.println(answer);
    }
}
