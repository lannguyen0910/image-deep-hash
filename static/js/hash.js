var el = x => document.getElementById(x);
var detectBtn = document.querySelector("#analyze-button");

function showPicker() {
  $("#file-input").click();
}

function clear() {
  $('#image-display').empty(); // removes upload img
  $('#upload-label').empty(); //removes upload img's filename
  $('#result-content').remove();   //remove result div (image + labels ...)
}

// Upload image
function showPicked(input) {
    var extension = input.files[0].name.split(".")[1].toLowerCase();
    var reader = new FileReader();

    reader.onload = function(e) {
        clear();
        el("upload-label").innerHTML = input.files[0].name;
        var file_url = e.target.result

        if(extension === "jpg" || extension === "jpeg" || extension === "png"){
        var img_html = '<img id="upload-image" src="' + file_url + '" style="display: block;margin-left: auto;margin-right: auto;width: 640px; height: 480px"/>';
        $('#image-display').html(img_html); // replaces previous img
        }  

    };

    detectBtn.removeAttribute("disabled");
    reader.readAsDataURL(input.files[0]);
}

window.onload = function(){
  $('#length-range').on('input', function() {
    $('#length-text span').html(this.value);
    threshold = $('#length-range').val() / 60;
  });
}