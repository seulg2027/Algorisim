/*
* 들어오는 간선은 없지만, 나가는 간선은 1개 이상인 노드 : 정점 노드 (전체 그래프 개수를 알 수 있음)
* 들어오는 간선이 2개 이상, 나가는 간선이 2개인 노드 : 8자 모양 그래프의 중앙 노드
* 들어오는 간선은 1개 이상, 나가는 간선은 없는 노드 : 막대모양 그래프의 마지막 노드
*/
import java.util.*;

class Solution {
    public int[] solution(int[][] edges) {
        int[] answer = {};
        int eightGraphCnt=0, stickGraphCnt=0, doughGraphCnt=0, totalGraphcnt=0, rootNode=0;
        HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();
        HashSet<Integer> nodes = new HashSet<>();
        int maxNode = 0;
        
        for (int i=0; i<edges.length; i++) {
            ArrayList<Integer> list = graph.getOrDefault(edges[i][0], new ArrayList<>());
            list.add(edges[i][1]);
            graph.put(edges[i][0], list);
            // node 종류 넣기
            maxNode = Math.max(maxNode, edges[i][0]);
            maxNode = Math.max(maxNode, edges[i][1]);
        }
        
        int[][] inOutGraph = new int[maxNode+1][2];
        
        // in, out 2차원 그래프
        for (int key : graph.keySet()) {
            for (int value : graph.get(key)) {
                inOutGraph[value][0]++;
                inOutGraph[key][1]++;
            }
        }
        
        for (int i=0; i<maxNode+1; i++) {
            if (inOutGraph[i][0] == 0 && inOutGraph[i][1] > 0 && inOutGraph[i][1] > totalGraphcnt) {
                totalGraphcnt = inOutGraph[i][1];
                rootNode = i;
            }
            else if (inOutGraph[i][0] >= 2 && inOutGraph[i][1] == 2) eightGraphCnt++;
            else if (inOutGraph[i][0] >= 1 && inOutGraph[i][1] == 0) stickGraphCnt++;
        }
        doughGraphCnt = totalGraphcnt - eightGraphCnt - stickGraphCnt;
        answer = new int[]{rootNode, doughGraphCnt, stickGraphCnt, eightGraphCnt};
        
        return answer;
    }
}