/**
 * 로마 숫자 만들기
 * 
 * 1. 4개의 수 1, 5, 10, 15를 중복조합해서 나올 수 있는 경우의 수
 * 2. 수를 모두 더했을 때, 중복되지 않아야 함
 */
import java.util.*;
import java.io.*;

public class boj_로마숫자만들기 {
    static int[] output;
    static int[] romeNumbers = {1, 5, 10, 50};
    static HashSet<Integer> numberSet = new HashSet<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int r = Integer.parseInt(br.readLine());
        output = new int[r];

        backtracking(0, 0, r);

        bw.write(String.valueOf(numberSet.size()) + "\n");
        bw.flush();
        bw.close();
    }

    private static void backtracking(int x, int start, int r) {
        if (x == r) {
            numberSet.add(Arrays.stream(output).sum());
            return;
        }
        for (int i=start; i<4; i++){ // 4개의 원소 중 중복 순열 계산
            output[x] = romeNumbers[i];
            backtracking(x+1, i, r);
        }
    }
}
