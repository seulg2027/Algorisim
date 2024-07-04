/**
 * 11651번 좌표 정렬하기2
 * 파이썬으로 너무너무나 쉽지만 자바로 한 번 해줘야함..
 */
import java.io.*;
import java.util.*;

public class boj_좌표정렬하기2 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][2];

        for (int i=0; i<N; i++) {
            int[] inner = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            arr[i] = inner;
        }

        // 오름차순 정렬
        // y가 우선, x는 후순위
        Arrays.sort(arr, (o1, o2) -> (o1[1] == o2[1] ? o1[0] - o2[0] : o1[1] - o2[1]));

        for (int i=0; i<N; i++) {
            bw.write(arr[i][0] + " " + arr[i][1] + "\n");
        }

        bw.flush();
        bw.close();
    }
}
