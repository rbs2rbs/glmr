$(window).scroll(function() {
    var winScrollTop = $(window).scrollTop();
    var winHeight = $(window).height();
    var floaterHeight = $('#whats').outerHeight(true);
    var fromBottom = 10;
    var top = winScrollTop + winHeight - floaterHeight - fromBottom;
	$('#whats').css({'top': top + 'px'});
});

$("#whats").on({
    mouseenter :function(){
        $("#whats").css("background-color","#202d40");
    } ,
    mouseleave :function(){
        $("#whats").css("background-color","#55849D");
    }
});

$(document).ready(function(){
    var fale = $("#fale");
    var iconWhats = $("#iconWhats");
    var whats = $("#whats");
    if(screen.width < 769){
        fale.text('');
        iconWhats.addClass("fa-2x").css({'margin-top': '-3px','margin-left': '-2px'});
        whats.css({'border-radius': '50%','width':'45px','height':'45px', 'padding': '2.5%'});
    }
})
