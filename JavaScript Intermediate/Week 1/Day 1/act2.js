
// let params = `scrollbars=no,resizable=no,status=no,location=no,toolbar=no,menubar=no,

// width=600,height=300,left=100,top=100`;

// open('/', 'test', params);
// let newWin = window.open("about:blank", "hello", "width=200,height=200");

// newWin.document.write("Hello, world!");


// document.getElementById('btn12').addEventListener('click');

// function Btn111 (){

// window.open('https://www.w3schools.com/js/js_this.asp');

// }

function Btn1(){

    let newWin = window.open("about:blank", "hello", "width=200,height=200");

newWin.document.write("Hello, world!");
 newWin.close();

}


function Btn2(){

    let newWindow = open('/', 'example', 'width=300,height=300')

    newWindow.focus();
    
    alert(newWin.location.href); // (*) about:blank, loading hasn't started yet

}

//chatgpt
function openWin (){

let newWindow = window.open('https://www.example.com','exampleWindow');



    let html = `<div style="font-size:30px">Welcome!</div>`;
    document.getElementById('myDiv').insertAdjacentHTML('afterbegin', html);

 }


function Btn4(){

    let params = `scrollbars=no,resizable=no,status=no,location=no,toolbar=no,menubar=no,
    width=600,height=300,left=100,top=100`;
    
    open('https://www.w3schools.com/js/js_this.asp', 'test', params);

}



// // Parent window
// let childWindow = window.open("child.html");

// function displayMessage(msg) {
//   alert(msg);
// }

// // // Child window
// window.opener.displayMessage("Hello from the child window!");


//closes window: returns true



// newWindow.onload = function Test1() {

//   newWindow.close();
//   let newWindow = open('/', 'example', 'width=300,height=300');

//   alert(newWindow.closed); // true

// };


function Act3(){

/*
if TodaysDate != ApplicationDate
then
ShowMess('Application closed')
else 
ShowMess('Application open')
btn===== Apply Now!
*/
const TodaysDate = new Date();
const ApplicationDate1 = new Date('2023-01-10');
const ApplicationDate2 = new Date('2023-01-29');

if ((TodaysDate > ApplicationDate1) && (TodaysDate< ApplicationDate2)){



}
}