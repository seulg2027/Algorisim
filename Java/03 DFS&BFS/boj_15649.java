/**
 * boj_15649
 * N과 M(1)
 * java 코테 연습
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_15649 {
    static int n, m;
    static boolean[] visited;
    static int[] arr;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        visited = new boolean[n+1];
        arr = new int[m+1];
        backtracking(1);
    }

    private static void backtracking(int x){
        if (x == m+1) {
            for (int i=1; i < m+1; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        } else {
            for (int i=1; i < n+1; i++) {
                // 방문하지 않으면
                if (!visited[i]) {
                    visited[i] = true;
                    arr[x] = i;
                    backtracking(x+1);
                    arr[x] = 0;
                    visited[i] = false;
                }
            }
        }
    }
}