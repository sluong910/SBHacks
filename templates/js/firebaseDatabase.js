// Initialize Firebase
var config = {
    apiKey: "AIzaSyDLZ672i6TUb9FwpIasc0MzfDhFOMrOYHI",
    authDomain: "sb-hacks-bf124.firebaseapp.com",
    databaseURL: "https://sb-hacks-bf124.firebaseio.com",
    projectId: "sb-hacks-bf124",
    storageBucket: "sb-hacks-bf124.appspot.com",
    messagingSenderId: "544177410232"
  };
  firebase.initializeApp(config);

  var vocab = document.getElementById("vocab");
  var definition = document.getElementById("definition");
  var dbRef = firebase.database().ref().child('vocab');
  dbRef.on('value', snap => definiton.innerText = snap.val);