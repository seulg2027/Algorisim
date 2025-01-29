/**
1  3
10 2
1. 1 + 10
2. 1 + 2 + 1(이동시간)
3. 3 + 10 + 2(이동시간)
4. 3 + 2
*/
import java.io.*;
import java.util.*;
public class softeer_조립라인 {
    public class Main {
        static int n;
        
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            n = Integer.valueOf(br.readLine());
            
            int[][] aLine = new int[n][2];
            int[][] bLine = new int[n][2];
            
            for (var i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int j = 0;
                while (st.hasMoreTokens()) {
                    int item = Integer.parseInt(st.nextToken());
                    if (j == 0) aLine[i][0] = item;
                    else if (j == 1) bLine[i][0] = item;
                    else if (j == 2) aLine[i][1] = item;
                    else if (j == 3) bLine[i][1] = item;
                    j ++;
                }
            }
    
            int prevA = aLine[0][0];
            int prevB = bLine[0][0];
    
            for (var idx = 1; idx < n; idx++) {
                int newA = Math.min(prevA, prevB + bLine[idx-1][1]) + aLine[idx][0];
                int newB = Math.min(prevB, prevA + aLine[idx-1][1]) + bLine[idx][0];
    
                prevA = newA;
                prevB = newB;
            }
            
            bw.write(String.valueOf(Math.min(prevA, prevB)));
    
            bw.flush();
            bw.close();
        }
    }
}
