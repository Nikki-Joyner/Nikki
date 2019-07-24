const greetPeople = (name1,name2) => {
console.log('Hello,' + name1 + ' and '+ name2 + '!');
}

const getFullName = (firstName, lastName) => {
  return firstName + ' ' + lastName
}

let radius = 10;
let area = Math.PI * radius * radius;
radius= radius *2;
area = Math.PI * Math.pow(radius,2);
let width = Math.round(Math.random() * 100);
let height = Math.round(Math.random() * 50);
let circumference = width * 2 + height * 2;

let n =1
const IncreaseNumber =() => {
  n=n+1
  console.log(n);
}

setInterval (IncreaseNumber, 1000);
