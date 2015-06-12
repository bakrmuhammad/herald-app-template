//CHANGE HEADER ON SCROLL
var folio = $(".navbar-default"),
    threshold = 20;

$(document).ready(function() {
    folio.css({
        "border-bottom": "1px solid #ddd"
    })
}), $(window).scroll(function() {
    var t = $(this).scrollTop();
    folio.css(t > threshold ? {
        "-moz-box-shadow": "0px 6px 2px rgba(0,0,0,0.2)",
        "-webkit-box-shadow": "0px 6px 2px rgba(0,0,0,0.2)",
        "box-shadow": "0px 6px 2px rgba(0,0,0,0.2)"
    } : {
        "-moz-box-shadow": "0px .25px 2px #ddd",
        "-webkit-box-shadow": "0px .25px 2px #ddd",
        "box-shadow": "0px .25px 2px #ddd"
    })
})






