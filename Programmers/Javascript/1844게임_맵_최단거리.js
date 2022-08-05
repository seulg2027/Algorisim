// 기본 큐 생성 //
class Queue {
  constructor() {
    this._arr = [];
  }
  push(item) {
    this._arr.push(item);
  }
  pop() {
    return this._arr.shift();
  }
  length() {
    return this._arr.length;
  }
}

function solution(maps) {
  var n = maps.length;
  var m = maps[0].length;
  var visited = new Array(n).fill(0).map(() => new Array(m).fill(0));

  // 큐에 할당 //
  var q = new Queue();
  q.push([0, 0, 0]);
  visited[0][0] = 1;

  const dx = [0, 1, 0, -1],
    dy = [1, 0, -1, 0];
  while (q.length() != 0) {
    var dist = q.pop();
    var x = dist[0],
      y = dist[1],
      d = dist[2];
    if (x === n - 1 && y === m - 1) {
      var answer = d + 1;
      break;
    }
    // bfs 코드 //
    for (var i = 0; i < 4; i++) {
      var rx = dx[i] + x;
      var ry = dy[i] + y;
      if (0 <= rx && rx < n && 0 <= ry && ry < m) {
        if (visited[rx][ry] === 0 && maps[rx][ry] === 1) {
          q.push([rx, ry, d + 1]);
          visited[rx][ry] = 1;
        }
      }
    }
  }
  return answer != undefined ? answer : -1;
}
