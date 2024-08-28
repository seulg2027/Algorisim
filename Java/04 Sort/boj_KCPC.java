
/**
 * 3758번 실버2 KCPC
 * class를 만들어서 더 가독성 있게 코드 짜기
 */

import java.io.*;
import java.util.*;

public class boj_KCPC {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            ArrayList<submitForm> form = new ArrayList<>();
            for (int id = 0; id < n; id++) {
                form.add(new submitForm(k, id + 1));
            }

            for (int i = 0; i < m; i++) {
                int[] play = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                int id = play[0] - 1;
                int j = play[1] - 1;

                if (form.get(id).recent == 0) { // 처음 할당하는 점수
                    form.get(id).cnt = 1;
                    form.get(id).score[j] = play[2];
                    form.get(id).total = play[2];
                    form.get(id).recent = i + 1;
                    continue;
                } else if (form.get(id).score[j] < play[2]) { // 이미 점수를 매김, 더 큰 점수일 경우
                    form.get(id).total += (play[2] - form.get(id).score[j]);
                    form.get(id).score[j] = play[2];
                }
                form.get(id).cnt += 1;
                form.get(id).recent = i + 1;
            }

            Collections.sort(form, new submitFormComparator());

            for (int j = 0; j < n; j++) {
                if (form.get(j).id == t) {
                    bw.write(String.valueOf(j + 1) + "\n");
                    break;
                }
            }
        }

        bw.flush();
        bw.close();
    }

    private static class submitForm {
        private int id;
        private int cnt = 0;
        private int[] score;
        private int total;
        private int recent = 0;

        public submitForm(int k, int id) {
            this.id = id;
            this.score = new int[k];
        }
    }

    private static class submitFormComparator implements Comparator<submitForm> {
        @Override
        public int compare(submitForm f1, submitForm f2) {
            // 1. 최종점수 내림차순
            if (f1.total < f2.total) {
                return 1;
            } else if (f1.total > f2.total) {
                return -1;
            } else {
                // 2. 제출 횟수 오름차순
                if (f1.cnt > f2.cnt) {
                    return 1;
                } else if (f1.cnt < f2.cnt) {
                    return -1;
                } else {
                    // 3. 제출 시간 오름차순
                    if (f1.recent > f2.recent) {
                        return 1;
                    } else if (f1.recent < f2.recent) {
                        return -1;
                    }
                }
            }
            return 0;
        }
    }
}