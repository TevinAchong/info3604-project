// reviews = [
//     {
//     "id": 1,
//     "class": 1,
//     "text": "This is the absolute greatest movie ever, I love it!",
//     "trini": ""
//     },
//     {
//         "id": 2,
//         "class": 0,
//         "text": "This is the absolute worst movie ever. I hate it!",
//         "trini": ""
//     }
// ];

var firebase = require('firebase');
// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyBiAwsFiDIHldyp2CFUzSF9qdmwiZC-r5M",
    authDomain: "final-project-data-collection.firebaseapp.com",
    databaseURL: "https://final-project-data-collection.firebaseio.com",
    projectId: "final-project-data-collection",
    storageBucket: "final-project-data-collection.appspot.com",
    messagingSenderId: "320036326310",
    appId: "1:320036326310:web:ae1cb4e32a6d53713c1d67"
};
  // Initialize Firebase
firebase.initializeApp(firebaseConfig);

const db = firebase.firestore();
db.settings({timestampsInSnapshots:true});

// Pull reviews from firebase and store them in reviews array
var reviews = [];
db.collection('reviews').onSnapshot(snapshot => {
    let changes = snapshot.docChanges();
    changes.forEach(change => {
        reviews.push(change.doc.data());
    });
});

exports.home = (req, res) => {
    res.render('home', {
        title: 'Home Page',
        reviews: reviews
    });
};

exports.notFound = (req, res) => {
    res.render('notFound', {
        title: '404 - Page Not Found'
    });
};