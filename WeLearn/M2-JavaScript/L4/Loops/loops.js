//const names = ['Alice',
//'Bob',
//'Charlie',
//'Debroah',
//'Evan';
/*
 const names = ["I really love Book 1 ", "I really love Book4 ","I really love Book2 ",
"I really love Book3 ", "I really love Book4 "];
for (let i=0; i < 5; i++)
{ console.log(names[i]);
};

names.forEach((name) => {
  console.log(name);
});
*/
let sum = 0;
let numbers = [0,1,2,3,4,5,6,7,8,9,10];
const findTotal =((item) => {
sum = sum + item })

 numbers.forEach(findTotal);

const buttons = document.querySelectorAll ('button');
const box = document.querySelector('#box');

buttons.forEach((button) => {
  button.addEventListener('click', () => {
  const color = button.innerHTML;
  box.stlyle.background = color;
  });
});
