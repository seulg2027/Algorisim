/**
반대방향도 함께 칠해주기
U, D -> 같이 칠해주기
R, L -> 같이 칠해주기
*/
public class prg_방문길이 {
    int[] dx = {0, 1, 0, -1}; // U, R, D, L
    int[] dy = {1, 0, -1, 0};
    
    int[][][] roads = new int[11][11][4];
    int answer = 0;
    
    public int solution(String dirs) {
        String[] commands = dirs.split("");
        int[] now = {5, 5};
        int d = 0;
        
        for (String c : commands) {
            if ("U".equals(c)) d = 0;
            else if ("R".equals(c)) d = 1;
            else if ("D".equals(c)) d = 2;
            else if ("L".equals(c)) d = 3;
            
            int nx = now[0] + dx[d];
            int ny = now[1] + dy[d];
            if (0 > nx || nx > 10 || 0 > ny || ny > 10) continue;
            if (roads[nx][ny][d] == 0) {
                roads[nx][ny][d] = 1;
                roads[now[0]][now[1]][(d + 2) % 4] = 1;
                answer++;
            }
            now[0] = nx;
            now[1] = ny;
        }
        return answer;
    }
}
