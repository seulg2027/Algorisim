/**
 * 11004번 K번째 수
 */
import java.io.*;
import java.util.*;

public class boj_K번째수 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int K = Integer.parseInt(br.readLine().split(" ")[1]);
        
        int[] arrA = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(arrA);

        bw.write(String.valueOf(arrA[K-1]) + "\n");
        
        bw.flush();
        bw.close();
    }
}
