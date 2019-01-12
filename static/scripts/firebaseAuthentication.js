alert("WORKING");
// Initialize Firebase
const config = {
    apiKey: "AIzaSyDLZ672i6TUb9FwpIasc0MzfDhFOMrOYHI",
    authDomain: "sb-hacks-bf124.firebaseapp.com",
    databaseURL: "https://sb-hacks-bf124.firebaseio.com",
    projectId: "sb-hacks-bf124",
    storageBucket: "sb-hacks-bf124.appspot.com",
    messagingSenderId: "544177410232"
  };
  firebase.initializeApp(config);

  //Get DOM elements
  const email = document.getElementById("email");
  const password = document.getElementById("password");
  const buttonLogin = document.getElementById("login");

buttonLogin.addEventListener('click', e => {alert("CLICK");
    const emailValue = email.value();
    const passwordValue = password.value();
    const auth = firebase.auth();

    const promise =  auth.signInWithEmailAndPassword(email, password);
    promise.catch(e => alert(e.message))
});