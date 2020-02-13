reviews = [
    {
    "id": 1,
    "class": 1,
    "text": "This is the absolute greatest movie ever, I love it!",
    "trini": ""
    },
    {
        "id": 2,
        "class": 0,
        "text": "This is the absolute worst movie ever. I hate it!",
        "trini": ""
    }
];

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