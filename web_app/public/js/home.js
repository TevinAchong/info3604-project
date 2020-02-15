$('#trini_translation').val('');
M.textareaAutoResize($('#trini_translation'));


function getText(){
    const
        obj = {
            trini_text: document.getElementById("trini_translation").value,
            untranslated_text: document.getElementById("review_id").textContent
        }
    ;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log('Data sent successfully');
      } else {
          console.log('Connection failed');
      }
    };
    xhttp.open("POST", '/api/v1/update', true);
    xhttp.setRequestHeader("Content-type","application/json");
    xhttp.send(JSON.stringify(obj));
    //console.log('getText 0');
    //console.log(untranslated_text);

   // console.log('getText passed');
}

// $.ajax({
//     type: "POST",
//     url: "/webservices/PodcastService.asmx/CreateMarkers",
//     // The key needs to match your method's input parameter (case-sensitive).
//     data: JSON.stringify({ Markers: markers }),
//     contentType: "application/json; charset=utf-8",
//     dataType: "json",
//     success: function(data){alert(data);},
//     failure: function(errMsg) {
//         alert(errMsg);
//     }
// });