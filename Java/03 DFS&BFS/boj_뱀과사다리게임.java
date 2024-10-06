/**
 * HashMap을 사용해서 뱀 / 주사위 넣기
 */
import java.io.*;
import java.util.*;

public class boj_뱀과사다리게임 {
    static class Distance implements Comparable<Distance>{
        int cost;
        int dist;

        public Distance(int cost, int dist) {
            this.cost = cost;
            this.dist = dist;
        }

        @Override
        public int compareTo(Distance d) {
            return this.cost - d.cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        HashMap<Integer, Integer> map = new HashMap<>(); // 시작, 끝 저장
        for (var i=0; i<n+m; i++) {
            st = new StringTokenizer(br.readLine());
            map.put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        int[] dice = {1, 2, 3, 4, 5, 6};
        boolean[] visited = new boolean[101];

        PriorityQueue<Distance> q = new PriorityQueue<>(); // 이동 횟수, 현재 위치 저장
        q.offer(new Distance(0, 1));
        int answer = 100;

        while (!q.isEmpty()) {
            Distance now = q.poll();
            //System.out.println("[" + now.cost + " " + now.dist + "]");
            if (now.dist == 100) {
                answer = now.cost;
                break;
            }

            if (map.containsKey(now.dist)) {
                int end = map.get(now.dist);
                q.offer(new Distance(now.cost, end));
                visited[end] = true;
            } else {
                for (int i=0; i<6; i++) {
                    int nx = now.dist + dice[i];
                    if (nx < 101 && !visited[nx]) {
                        q.offer(new Distance(now.cost+1, nx));
                        visited[nx] = true;
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
