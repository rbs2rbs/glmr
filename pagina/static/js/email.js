$(document).ready(function(){
    $('#submit').on('click',function(){
        /* local validation */
        $('#contactForm').validate({
                rules: {
                  name: {
                    required: true,
                    minlength: 3,
                    letters: true
                  },
                  from_email: {
                    required: true,
                    email: true
                  }
                },
                messages: {
                  name: "Caracter não válido para o nome",
                  from_email: "Utilize um email válido"
                },
            /* submit via ajax */
            submitHandler: function(form) {
    
                var sLoader = $('.submit-loader');
                var formData = $(form).serializeArray();
                var dataToSend = new FormData();
                for(var a=0; a < formData.length; a++) {
                  dataToSend[formData[a].name] = formData[a].value;
                }
                
                $.ajax({
                    headers: {
                    "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val(),
                    },
                    url: 'email/',
                    processData: false,
                    'type': 'POST',
                    
                    contentType: "application/json",
                    dataType: "json",
                    data: JSON.stringify(dataToSend),
                    beforeSend: function() { 
    
                        sLoader.slideDown("slow");
    
                    },
                    success: function(msg) {
                        // Message was sent
                        if (msg=='OK') {
                            sLoader.slideUp("slow"); 
                            $('.message-warning').fadeOut();
                            $('#contactForm').fadeOut();
                            $('.message-success').fadeIn();
                            $('.message-success').css({'color':'#028090'})
                        }
                        // There was an error
                        else {
                            sLoader.slideUp("slow"); 
                            $('.message-warning').html(msg);
                            $('.message-warning').slideDown("slow");
                            $('.message-warning').css({'color':'#ff6163'})
                        }
    
                    },
                    error: function() {
    
                        sLoader.slideUp("slow"); 
                        $('.message-warning').html("Algo deu Errado. Tente Novamente");
                        $('.message-warning').slideDown("slow");
                        $('.message-warning').css({'color':'#ff6163'})
    
                    }
    
                });
            }
    
        });
    });
});