/**
 * 동일한 문자가 3개 나올 때 -> 판별
 * HashMap {E : 1, H : 2, ...}
 */
import java.io.*;
import java.util.*;

public abstract class boj_진짜메시지 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        HashMap<String, Integer> messageMap;

        int n = Integer.parseInt(br.readLine());

        for (var i = 0; i < n; i++) {
            String message = br.readLine();
            boolean isTrue = true;
            String m = "";
            messageMap = new HashMap<>();

            // 0... 3
            for (var j = 0; j < message.length(); j++) {
                m = String.valueOf(message.charAt(j));
                messageMap.put(m, messageMap.getOrDefault(m, 0) + 1);
                if (messageMap.get(m) == 3) {
                    if (message.length() <= j + 1 || !String.valueOf(message.charAt(j+1)).equals(m)) {
                        isTrue = false;
                        break;
                    }
                    messageMap.put(m, -1);
                }
            }
            //System.out.println(messageMap.toString());
            bw.write(isTrue ? "OK\n" : "FAKE\n");
        }

        bw.flush();
        bw.close();
    }
}
