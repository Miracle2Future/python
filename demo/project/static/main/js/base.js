$(document).ready(function(){
    document.documentElement.style.fontSize = innerWidth / 10 + "px";
    $(".home").click(function(){
        $(this).css("background","url(/static/main/imgs/home1.png) no-repeat");
    });
})