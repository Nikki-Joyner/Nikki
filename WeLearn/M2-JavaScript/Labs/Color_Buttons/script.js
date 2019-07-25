// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Use querySelector to store the div in a variable.
let Array = [];


const redButton = document.querySelector('#red');

//RED
redButton.addEventListener('click', (e) => {
responseBox.style.backgroundColor = "red"
  console.log("You clicked the red button!");
});
// GREEN!!!
const greenButton = document.querySelector('#green');
//v1 let responseBox = document.querySelector('#response-box');

greenButton.addEventListener('click', (event2) => {
  responseBox.style.backgroundColor = "green"
  console.log("You clicked the green button!");
 // v1 Array.push('green')
  // v1 Responsebox.InnerHTML = Array;
});
//BLUE!!!
const blueButton = document.querySelector('#blue');
let responseBox = document.querySelector('#response-box');

blueButton.addEventListener('click', (event3) => {
  responseBox.style.backgroundColor = "blue"
  console.log("You clicked the blue button!");
// v2 responseBox.document.write("blue");
});
// v1 Array.push('blue')
// v1 Responsebox.InnerHTML = Array;
// v2responsebox.document.querySelector("#response-box");
//v2responsebox.textContent += 'blue';
// v2 document.getElementById("#response-box")
