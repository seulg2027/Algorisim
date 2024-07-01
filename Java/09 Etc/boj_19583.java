/**
 * 19583번 실버2 싸이버개강총회
 * compareTo 를 잘 활용하쟈!
 */
import java.io.*;
import java.util.*;

public class boj_19583 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] timeLine = br.readLine().split(" ");
        String start = timeLine[0];
        String feEnd = timeLine[1];
        String stEnd = timeLine[2];

        String line = null;
        HashSet<String> memberList = new HashSet<>();
        int answer = 0;

        while (true) {
            line = br.readLine();
            if ("".equals(line) || line == null) { break; }

            String[] record = line.split(" ");

            String time = record[0];
            
            if (start.compareTo(time) >= 0) {
                memberList.add(record[1]);
            } else if (feEnd.compareTo(time) <= 0 && stEnd.compareTo(time) >=0) {
                if (memberList.contains(record[1])) {
                    answer ++;
                    memberList.remove(record[1]);
                }
            }
        }

        bw.write(String.valueOf(answer) + "\n");
        bw.flush();
        bw.close();
    }
}
