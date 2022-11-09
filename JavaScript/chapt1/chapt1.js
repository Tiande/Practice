"use strict";

console.log('sdgfd');

let user = 'John';
// let user = 'two';
user = 'hello';

let message = 'world';

message = user;

let $ = 1;
let _ = 2;
alert($ + _);

const myBirthday = '07.10.1995';


const COLOR_RED = "#F00";
const COLOR_GREEN = "#0F0";
const COLOR_BLUE = "#00F";
const COLOR_ORANGE = "#FF7F00";

// ……当我们需要选择一个颜色
let color = COLOR_ORANGE;
alert(color); // #FF7F00

console.log(9007199254740991 + 1); // 9007199254740992
console.log(9007199254740991 + 2); // 9007199254740992

// 尾部的 "n" 表示这是一个 BigInt 类型
const bigInt = 1234567890123456789012345678901234567890n;

let myName = "John";

// 嵌入一个变量
alert( `Hello, ${myName}!` ); // Hello, John!

// 嵌入一个表达式
alert( `the result is ${1 + 2}` ); // the result is 3

let nameFieldChecked = true; // yes, name field is checked
let ageFieldChecked = false; // no, age field is not checked

let isGreater = 4 > 1;

alert( isGreater ); // true（比较的结果是 "yes"）

let age1 = null;

let age2;
age2 = undefined;
alert(age2); // 弹出 "undefined"

typeof undefined // "undefined"

typeof 0 // "number"

typeof 10n // "bigint"

typeof true // "boolean"

typeof "foo" // "string"

typeof Symbol("id") // "symbol"

typeof Math // "object"  (1)

typeof null // "object"  (2)

typeof alert // "function"  (3)

let age = prompt('How old are you?', 100);

alert(`You are ${age} years old!`); // You are 100 years old!
