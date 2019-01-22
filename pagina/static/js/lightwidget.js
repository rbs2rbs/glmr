$(document).ready(function() {
  links = $.get('https://beta.rstudioconnect.com/content/3898/imagem/titulo',function(data){
    $('.item-folio__text').each( function(i,index) {
      $(index).find('.item-folio__title').text(data[i+6]);
      $(index).find('.item-folio__cat').text(data[i]);
    });
  });
});