
var slideImg = document.getElementById("slideImg");

var images = new Array(
    "images/canaan_1.jpg",
    "images/canaan_back.jpg",
    "images/jeanfabric.jpg",
    "images/jeanjacket_1.jpg"

   

);

var len = images.length;
var i =0;
function slider(){
    if(i> len-1){
        i =0;
    }
    slideImg.src = images[i];
    i++;
    setTimeout('slider()',2500);
}

