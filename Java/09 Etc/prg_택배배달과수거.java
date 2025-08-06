//import java.util.*;

public class prg_택배배달과수거 {
    // 첫번째 시도 : 시간초과(90점)
    // 먼저 택배를 배달 -> 돌아오면서 수거
    // 1. 택배 배달 지점을 정하기 (배달 > 0, 수거 > 0인 지점)
    // 2. 배달 & 수거 동시에 진행, 뒤에서부터 상자를 없애야 하기 때문

    // class Solution {
    //     public long solution(int cap, int n, int[] deliveries, int[] pickups) {
    //         long answer = 0;
            
    //         while (true) {
    //             int deliveryHome = -1;
                
    //             for (int i=n-1; i>=0; i--) {
    //                 if (deliveries[i] > 0 || pickups[i] > 0) {
    //                     deliveryHome = i;
    //                     break;
    //                 }
    //             }
    //             if (deliveryHome == -1) break;
                
    //             answer += (deliveryHome + 1) * 2;
                
    //             int[] save = new int[2];
    //             // System.out.println(Arrays.toString(deliveries));
    //             // System.out.println(Arrays.toString(pickups));
    //             for (int j=deliveryHome; j>=0; j--) {
    //                 if (save[0] == cap && save[1] == cap) break;
    //                 int remain;
                    
    //                 if (save[0] < cap && deliveries[j] > 0) {
    //                     remain = cap - save[0] > deliveries[j] ? deliveries[j] : cap - save[0];
    //                     save[0] += remain;
    //                     deliveries[j] -= remain;
    //                 }
                    
    //                 if (save[1] < cap && pickups[j] > 0) {
    //                     remain = cap - save[1] > pickups[j] ? pickups[j] : cap - save[1];
    //                     save[1] += remain;
    //                     pickups[j] -= remain;
    //                 }
    //             }
    //             // System.out.println(Arrays.toString(deliveries));
    //             // System.out.println(Arrays.toString(pickups));
    //         }
            
    //         return answer;
    //     }
    // }

    // 누적 합
    // 뒤에서부터 계산 -> cap의 배수만큼 누적합이 계산될 때마다 추가
    class Solution {
        public long solution(int cap, int n, int[] deliveries, int[] pickups) {
            long answer = 0;
            
            int delivery = 0, pickup = 0;
            
            for (int i=n-1; i>=0; i--) {
                delivery += deliveries[i];
                pickup += pickups[i];
                
                while (delivery > 0 || pickup > 0) {
                    delivery -= cap;
                    pickup -= cap;
                    answer += (i+1)*2;
                }
            }
            
            return answer;
        }
    }
}
