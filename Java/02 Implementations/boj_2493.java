/**
 * 2493번 골드5 탑
 * 전형적인 스택 문제
 */

import java.io.*;
import java.util.*;

public class boj_2493 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] answer = new int[N];
        answer[0] = 0; // 가장 첫 탑은 레이저 송신을 보낼 곳이 없음
        Stack<int[]> stack = new Stack<>();
        int height;

        for (int i = 0; i < N; i++) {
            height = Integer.parseInt(st.nextToken());
            boolean isResponse = false;
            // 스택이 비지 않았다면
            while (!stack.isEmpty()) {
                int[] tmp = stack.peek();
                if (tmp[0] > height) {
                    answer[i] = tmp[1];
                    isResponse = true;
                    break;
                }
                stack.pop();
            }
            if (!isResponse) { answer[i] = 0; }
            stack.push(new int[]{height, i+1});
        }

        StringBuilder sb = new StringBuilder("");
        for (int a : answer) {
            sb.append(a + " ");
        }
        bw.write(sb + "\n");
        bw.flush();
        bw.close();
    }
}
