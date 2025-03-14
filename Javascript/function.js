
// 함수 arguments 객체 //
function multiply(x, y) {
    console.log(arguments);
    return x * y;
}

multiply();
multiply(1);
multiply(1, 2);
multiply(1, 2, 3);

// 함수 객체 프로퍼티 //
function square(number) {
    return number * number;
}

square.x = 10;
square.y = 20;

console.log(square.x, square.y);

// 함수 length 프로퍼티 //
function foo() { }
console.log(foo.length) // 0

