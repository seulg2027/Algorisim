/*
 * 문자열
 */
import java.io.*;
import java.util.*;

public class softeer_xmakesspot {
    public class Main {
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

            int n = Integer.parseInt(br.readLine());
            StringBuilder sb = new StringBuilder();
            
            for (var i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String s = st.nextToken();
                String t = st.nextToken();

                int p = s.indexOf('x') == -1 ? s.indexOf('X') : s.indexOf('x');
                char str = t.charAt(p);
                sb.append(String.valueOf(str).toUpperCase());
            }
            bw.write(sb.toString());
            
            bw.flush();
            bw.close();
        }
    }
}
