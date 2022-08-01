// var person = {
//     name: 'Lee',
//     gender: 'male',
//     sayHello: function() {
//         console.log('Hi! My name is ' + this.name);
//     }
// };

// console.log(typeof person);
// console.log(person);

// person.sayHello();

const obj = { a: 1 };
const copy = Object.assign({}, obj);
console.log(copy);
console.log(obj === copy); // false

// 타겟 객체 변경하기
const o1 = { a: 1 };
const o2 = { b: 2 };
const o3 = { c: 3 };

const merge1 = Object.assign(o1, o2, o3);
console.log(merge1); // { a: 1, b: 2, c: 3 }
console.log(o1);     // { a: 1, b: 2, c: 3 } (타겟 객체가 변경됨)
console.log(o2);     // { b: 2 }

// 타겟 객체 유지하기
const o4 = { a: 1 };
const o5 = { b: 2 };
const o6 = { c: 3 };

const merge2 = Object.assign({}, o4, o5, o6);
console.log(merge2); // { a: 1, b: 2, c: 3 }
console.log(o4);     // { a: 1 } (타겟 객체가 변경되지 않음)
