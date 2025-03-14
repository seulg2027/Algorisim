/**
 * 구현
 * 4 3 6 8 7 5 2 1
 * 
 * 1 2 3 [4]
 * 1 2 [3]
 * 1 2 5 [6]
 * 1 2 5 7 [8]
 * 1 2 5 [7]
 */
import java.io.*;
import java.util.*;

public class boj_스택수열 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        int[] sequences = new int[n];
        
        for (var i = 0; i < n; i++) {
            sequences[i] = Integer.parseInt(br.readLine());
        }

        int idx = 0, num = 1;
        while (idx < n) {
            if (stack.isEmpty() || stack.peek() < sequences[idx]) {
                if (num > n) break;
                stack.add(num);
                sb.append("+\n");
                num++;
                continue;
            }
            
            if (stack.peek() == sequences[idx]) {
                stack.pop();
                sb.append("-\n");
                idx++;
            } else if (stack.peek() > sequences[idx]) {
                stack.pop();
                sb.append("-\n");
            }
        }

        if (idx != n) {
            sb.setLength(0);
            sb.append("NO\n");
        }

        bw.write(sb.toString());

        bw.flush();
        bw.close();
    }
}