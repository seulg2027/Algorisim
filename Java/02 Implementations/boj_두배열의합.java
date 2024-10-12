/**
 * A {1, 3, 1, 2}
 * B {1, 3, 2}
 * A 반복문 돌다가 -> 중간에
 */
import java.io.*;
import java.util.*;

public class boj_두배열의합 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long t = Long.parseLong(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int[] A_arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int m = Integer.parseInt(br.readLine());
        int[] B_arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        List<Long> A_sum = new ArrayList<>();
        for (var start=0; start<n; start++) {
            long a_total = 0;
            for (var end=start; end<n; end++) {
                a_total += A_arr[end];
                A_sum.add(a_total);
            }
        }

        HashMap<Long, Integer> B_map = new HashMap<>();
        for (var i=0; i<m; i++) {
            long b_total = 0;
            for (var j=i; j<m; j++) {
                b_total += B_arr[j];
                B_map.put(b_total, B_map.getOrDefault(b_total, 0) + 1);
            }
        }

        long total = 0;
        for (long item : A_sum) {
            long remain = t - item;
            total += B_map.getOrDefault(remain, 0);
        }

        System.out.println(total);
    }
}
