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
//firebase.initializeApp(firebaseConfig);
//const db = firebase.firestore();

const firebaseApp = firebase.initializeApp(firebaseConfig);
db = firebase.firestore(firebaseApp);


// Pull reviews from firebase and store them in reviews array
var reviews = [];

db.collection("reviews").where("translated", "==", false).limit(1)
    .get()
    .then(function(querySnapshot) {
        querySnapshot.forEach(function(doc) {
            reviews.push(doc);
            console.log(doc.id, " => ", doc.data());
        });
    })
    .catch(function(error) {
        console.log("Error getting documents: ", error);
});

exports.db = db;

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

