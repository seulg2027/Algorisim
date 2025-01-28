/**
 * 단축키를 지정할 때 동일한 문자는 지정하면 안됨
 */
import java.io.*;
import java.util.*;

public class boj_단축키지정 {
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        HashSet<String> shortKey = new HashSet<>();
        n = Integer.parseInt(br.readLine());
        
        for (var i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            boolean isToken = false;
            StringBuilder sb = new StringBuilder();

            while (st.hasMoreTokens()) {
                String word = st.nextToken();
                String key = String.valueOf(word.charAt(0));
                // 공백 문자열은 단축키로 지정될 수 없음, 단축키에 없는 문자열만
                if (!isToken && !key.equals(" ") && !shortKey.contains(key.toUpperCase())) {
                    shortKey.add(String.valueOf(word.charAt(0)).toUpperCase());
                    isToken = true;
                    word = setAlphabet(word, 0);
                }
                sb.append(word + " ");
            }

            if (!isToken) {
                String str = sb.toString();
                sb.setLength(0);
                for (var j = 0; j < str.length()-1; j++) {
                    if (!String.valueOf(str.charAt(j)).equals(" ") && !shortKey.contains(String.valueOf(str.charAt(j)).toUpperCase())) {
                        shortKey.add(String.valueOf(str.charAt(j)).toUpperCase());
                        isToken = true;
                        str = setAlphabet(str, j);
                        break;
                    }
                }
                sb.append(str);
            }

            bw.write(sb.toString() + "\n");
        }

        bw.flush();
        bw.close();
    }

    private static String setAlphabet(String str, int idx) {
        StringBuilder sb = new StringBuilder();
        for (var i = 0; i < str.length(); i++) {
            if (i == idx) {
                sb.append("[");
                sb.append(String.valueOf(str.charAt(i)));
                sb.append("]");
            } else {
                sb.append(String.valueOf(str.charAt(i)));
            }
        }
        return sb.toString();
    }
}
