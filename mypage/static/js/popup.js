logout
$('#logout').click( function(event){
    var link = this;
    event.preventDefault();
    $.confirm({
        title: 'Подтверждение действия',
        async: false,
        content: 'Действительно выйти?',
        buttons: {
            yes: {
                text: 'Да',
                btnClass: 'btn-primary rounded',
                keys: [
                    'enter'
                ],
                action: function(){
                    window.location = link.href;
                }
            },
            no: {
                text: 'Нет',
            }
        }
    });
});
$('#questionForm').submit( function(event){
    event.preventDefault();
    $.confirm({
        title: 'Подтверждение отправки',
        async: false,
        content: 'Действительно отправить?',
        buttons: {
            yes: {
                text: 'Да',
                btnClass: 'btn-primary rounded',
                keys: [
                    'enter'
                ],
                action: function(){
                    localStorage.formSubmitted = true;
                    $("#questionForm").unbind().submit();
                }
            },
            no: {
                text: 'Нет'
            }
        }
    });
});

$( document ).ready(function() {
    console.log(localStorage.formSubmitted);
    if (localStorage.formSubmitted === "true") {
            $.confirm({
                async: false,
                title: 'Спасибо за вопрос!',
                content: 'Я отвечу на него в ближайшее время.',
                type: 'primary',
                typeAnimated: true,
                buttons: {
                    ok: {
                        text: 'ОК',
                        btnClass: 'btn-primary',
                    }
                }
            });
    };
    localStorage.formSubmitted = false;
});