function solution(nums) {
  var kind = new Set(nums);
  var cnt = nums.length / 2;
  var answer = kind.size <= cnt ? kind.size : cnt;
  return answer;
}
