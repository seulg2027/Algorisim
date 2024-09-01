/**
 * 2776번 암기왕
 * 
 * 1. 출제된 문제들 -> 정렬
 * 2. 연종이가 기억하는 문제들을 하나씩 이분탐색해서 찾음
 * 3. 결과에 찾지 못하면 0, 찾으면 1 넣기
 */
import java.io.*;
import java.util.*;;

public class boj_암기왕 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<Integer> answer = new ArrayList<>();

        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            int[] noteOne = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int M = Integer.parseInt(br.readLine());
            int[] noteTwo = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            Arrays.sort(noteOne);
            // 이분탐색
            for (int i=0; i<M; i++) {
                int left = 0, right = N-1;
                int mid = -1;
                while (left <= right) {
                    mid = (left + right) / 2;
                    if (noteOne[mid] == noteTwo[i]) {
                        answer.add(1);
                        break;
                    } else if (noteOne[mid] > noteTwo[i]) {
                        right = mid - 1;
                    } else if (noteOne[mid] < noteTwo[i]) {
                        left = mid + 1;
                    }
                }
                // 해당 값을 발견하지 못했다면, 0 넣기
                if (noteOne[mid] != noteTwo[i]) {
                    answer.add(0);
                }
            }
        }

        for (Integer res : answer) {
            bw.write(String.valueOf(res) + "\n");
        }
        bw.flush();
        bw.close();
    }
}
