const express = require('express'); 
const app = express();

app.set('view engine', 'ejs');

const path = require('path');
app.use(express.static(path.join(__dirname, 'public')));

const cors = require('cors');
const bodyParser = require('body-parser');

//app.use(express.json());
app.use(bodyParser.json());
app.use(cors());
app.use(bodyParser.urlencoded({extended: false}));

const routes = require('./routes');

const db = routes.db;

app.get('/', routes.home);
//app.get('*', routes.notFound);
app.get('/review', function(req, res) {
    //console.log("here2");
    var review_arr = [];
    db.collection("reviews").where("translated", "==", false).limit(10)
    .get()
    .then(function(querySnapshot) {
        querySnapshot.forEach(function(doc) {
        console.log(doc.id, " => ", doc.data());
        review_arr.push({"review": doc.data().review,
          "sentiment": doc.data().sentiment,
        "id":doc.id});
        });
        var rand_num = Math.floor(Math.random() * Math.floor(review_arr.length));
        res.json(review_arr[rand_num]);
    })

    .catch(function(error) {
        console.log("Error getting documents: ", error);
  });

  })


var port = 3000; 
app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});

app.post('/update', (req, res) => {
  console.log(req.body);
  //console.log(JSON.stringify(req.body));
    if(!req.body.untranslated_text) {
      return res.status(400).send({
        success: 'false',
        message: 'untranslated_text is required'
      });
    } else if(!req.body.trini_text) {
      return res.status(400).send({
        success: 'false',
        message: 'trini_text is required'
      });
    }
   const
        untranslated_text_id = req.body.untranslated_text,
        trini_text = req.body.trini_text
   ;
   db.collection("reviews").doc(untranslated_text_id).update({"trini_translation": trini_text, "translated": true});
   return res.status(201).send({
     success: 'true',
     message: 'translation added successfully'
   })
});
  


