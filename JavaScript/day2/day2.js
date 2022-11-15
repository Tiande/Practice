"use strict";

// let value = true;
// alert(typeof value); //boolean

// value = String(value);
// alert(typeof value); //string


// alert("6" / "2");
// let str = "123";
// alert(typeof str);
// let num = Number(str);
// alert(typeof num);


// let age = Number("an arbitrary string instead of a Number 123");
// alert(age);  //NaN
// alert(Number(" 12 3 ")); //NaN
// alert(Number(undefined)); // NaN


// alert( 5 % 2 );
// alert( 8 % 3 );
// alert( 2 ** 2 );  //求幂
// alert( 2 ** 3 );
// alert( 2 ** 4 );
// alert( 4 ** (1/2) ); //平方根


// let s = "my" + "string";
// let s1 = "my" + 1;  //to string
// alert(2+2+'1'); //41
// alert('1'+2+2); //122
// alert(6-'2'); //4
// alert('6' / '2'); //3


// let x = 1;
// alert( +x ); //1
// let y = -2;
// alert( +y ); //-2
// alert( +true ); //1
// alert( +'' ); //0


let apples = '2';
let oranges = '3';
alert( apples + oranges ); // '23'
alert( +apples + +oranges ); // 5
alert( Number(apples) + Number(oranges) ); // 5

//https://zh.javascript.info/operators