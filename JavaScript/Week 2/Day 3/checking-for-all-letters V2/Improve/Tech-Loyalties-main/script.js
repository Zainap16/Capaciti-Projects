const myForm = document.getElementById("myForm");
myForm.addEventListener("submit", (e) =>{
  e.preventDefault();
  console.log("Form has been submitted");
  
});
function emptyName() {
  if (document.getElementById("Name").value == "" ){
    
    document.getElementById('Name').style.borderColor = "red";
    return false;
  } else{
    document.getElementById('Name').style.borderColor = "green";
  }
}

function emptySurname(){
  if (document.getElementById("Surname").value == "" ){
    
    document.getElementById('Surname').style.borderColor = "red";
    return false;
  } else{
    document.getElementById('Surname').style.borderColor = "green";
  }
}

function emptyIDNumber(){
  if (document.getElementById("IDNo").value == "" ){
    
    document.getElementById('IDNo').style.borderColor = "red";
    return false;
  } else{
    document.getElementById('IDNo').style.borderColor = "green";
  }
}

function emptyDateOfBirth(){
  if (document.getElementById("DoB").value == "" ){
    
    document.getElementById('DoB').style.borderColor = "red";
    return false;
  } else{
    document.getElementById('DoB').style.borderColor = "green";
  }
}

function emptyAge(){
  if (document.getElementById("Age").value == "" ){
    
    document.getElementById('Age').style.borderColor = "red";
    return false;
  } else{
    document.getElementById('Age').style.borderColor = "green";
  }
}

function emptGrade(){
  if (document.getElementById("Grade").value == "" ){
    
    document.getElementById('Grade').style.borderColor = "red";
    return false;
  } else{
    document.getElementById('Grade').style.borderColor = "green";
  }
}

function emptyEmail(){
  if (document.getElementById("email").value == "" ){
    
    document.getElementById('email').style.borderColor = "red";
    return false;
  } else{
    document.getElementById('email').style.borderColor = "green";
  }
}

function emptyPhoneNumber(){
  if (document.getElementById("phone").value == "" ){
    
    document.getElementById('phone').style.borderColor = "red";
    return false;
  } else{
    document.getElementById('phone').style.borderColor = "green";
  }
}

function emptyAddress(){
  if (document.getElementById("address").value == "" ){
    
    document.getElementById('address').style.borderColor = "red";
    return false;
  } else{
    document.getElementById('address').style.borderColor = "green";
  }
}



