const mybutton = document.querySelector("#mybutton");
const mybox = document.querySelector("#box");
mybutton.addEventListener('click', (event) => {
console.log('Like button clicked');
  mybutton.innerHTML = 'Liked';
  mybutton.style.backgroundColor = 'lightgreen';
});
