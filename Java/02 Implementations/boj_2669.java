/*
 * boj 2669번
 * 직사각형 네개의 합집합의 면적 구하기
 */
import java.io.*;
import java.util.*;

public class boj_2669 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] matrix = new int[100][100];
        int answer = 0;

        for (int i = 0; i < 4; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            for (int a = x1; a < x2; a++) {
                for (int b = y1; b < y2; b++) {
                    matrix[a][b] = 1;
                }
            }
        }

        for (int m = 0; m < 100; m++) {
            answer += Arrays.stream(matrix[m]).sum();
        }

        System.out.println(answer);
    }
}
