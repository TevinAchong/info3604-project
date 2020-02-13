const express = require('express'); 
const app = express();

app.set('view engine', 'ejs');

const path = require('path');
app.use(express.static(path.join(__dirname, 'public')));

const routes = require('./routes');

app.get('/', routes.home);
app.get('*', routes.notFound);

var port = 3000; 
app.listen(port, () => {
    console.log(`Listening on port ${port}`);
})