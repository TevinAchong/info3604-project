$('#trini_translation').val('');
M.textareaAutoResize($('#trini_translation'));




function loadNewReview(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("here1");
           var json_obj = JSON.parse(this.responseText);
           console.log(JSON.stringify(json_obj));
           document.getElementById("untranslated_text").innerHTML = json_obj.review;
           if (json_obj.sentiment == 1){
                document.getElementById("review_type").innerHTML = "Positive Review";
           } else {
                 document.getElementById("review_type").innerHTML = "Negative Review";
                   }
            document.getElementById("review_id").innerHTML = json_obj.id;

        }
    };
    xhttp.open("GET", "/review", true);
    xhttp.setRequestHeader("Content-type","application/json");
    xhttp.send();
}

function getText(){
    const
        obj = {
            trini_text: document.getElementById("trini_translation").value,
            untranslated_text: document.getElementById("review_id").textContent
        }
    ;

    document.getElementById("trini_translation").value = '';
    document.getElementById("review_type").value = '';
    document.getElementById("untranslated_text").value = '';
    document.getElementById("review_id").value = '';
    loadNewReview();

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 201) {
        console.log('Data sent successfully');
      } else {
          console.log('Connection failed');
      }
    };
    xhttp.open("POST", '/update', true);
    xhttp.setRequestHeader("Content-type","application/json");
    xhttp.send(JSON.stringify(obj));

}

