/**
 * 줄 선 순서
 * 1 2 3 4 [키]
 * 2 1 1 0 [왼쪽에 더 큰 사람]
 * 
 * 4 2 3
 * 
 * 1 2 3 4 5 6 7
 * 6 1 1 1 2 0 0
 * 
 * 구현
 */
import java.io.*;
import java.util.*;

public class boj_한줄로서기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[][] list = new int[n][2];

        for (var i = 0; i < n; i++) {
            list[i][0] = i + 1;
            list[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(list, (o1, o2) -> o1[1] == o2[1] ? o1[0] - o2[0] : o1[1] - o2[1]);

        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(list[0][0]);

        for (var i = 1; i < n; i++) {
            int height = list[i][0], leftP = list[i][1];
            int cnt = 0, idx = 0, number = 0;
            boolean stop = false;

            for (var j = 0; j < answer.size(); j++) {
                if (answer.get(j) > height) {
                    cnt ++;
                }
                if (cnt > leftP) {
                    number = answer.get(j);
                    answer.set(j, height);
                    stop = true;
                    idx = j + 1;
                    break;
                }
            }

            if (!stop) {
                answer.add(height);
            } else {
                answer.add(number);
                ArrayList<Integer> newArr = new ArrayList<>(answer);
                for (var k = idx; k < answer.size()-1; k++) {
                    int temp = answer.get(k);
                    newArr.remove(idx);
                    newArr.add(temp);
                }
                answer = new ArrayList<>(newArr);
            }
        }

        for (int i = 0; i < n; i ++) {
            if (i == n - 1) {
                System.out.println(answer.get(i));
                break;
            }
            System.out.print(answer.get(i) + " ");
        }
    }
}
