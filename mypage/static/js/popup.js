$('#target').submit( function(event){
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
                    $("#target").unbind().submit();
                }
            },
            no: {
                text: 'Нет',
                keys: [
                    'enter',
                    'shift'
                ],
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