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
app.get('*', routes.notFound);

var port = 3000; 
app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});

app.post('/api/v1/update', (req, res) => {
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
        untranslated_text = req.body.untranslated_text,
        trini_text = req.body.trini_text
   ;
   db.collection("reviews").doc(untranslated_text).update({"trini_translation": trini_text, "translated": true});
   return res.status(201).send({
     success: 'true',
     message: 'translation added successfully'
   })
  });
  