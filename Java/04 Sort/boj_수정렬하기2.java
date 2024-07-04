/**
 * 수 정렬하기2
 */
import java.io.*;
import java.util.*;

public class boj_수정렬하기2 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        Integer[] numbers = new Integer[N];
        for (int n=0; n<N; n++) {
            numbers[n] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(numbers);
        for (int n=0; n<N; n++) {
            bw.write(String.valueOf(numbers[n]) + "\n");
        }
        bw.flush();
        bw.close();
    }
}
