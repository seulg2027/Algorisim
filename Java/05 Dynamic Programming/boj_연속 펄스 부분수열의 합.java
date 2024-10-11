/**
[2, 3, -6, 1, 3, -1, 2, 4]
 0  1  2   3  4   5  6  7
0, 2, 4, 6 -> 함께 -1 곱할 수 있음
[2, 3, 9, 10, 3, 4, 6, 4] DP?

[1, -1, 1, ...]
[2, -3, -6, -1, 3, 1, 2, -4]
[-1, 1, -1, ...]
[-2, 3, 6, 1, -3, -1, -2, 4]
=> 두 개의 배열에서 큰 값
*/
class Solution {
    public long solution(int[] sequence) {
        long pos = 0, neg = 0, ans = 0;
        int mul = 1;
        
        for (int seq : sequence) {
            pos = Math.max(pos + mul * seq, mul * seq);
            neg = Math.max(neg + (-mul) * seq, -mul * seq);
            ans = Math.max(Math.max(pos, neg), ans);
            mul *= -1;
        }
        
        return ans;
    }
}