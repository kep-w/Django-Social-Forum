$(function () {
    var username = $('#username').val();
    if ($("#welcome").html()=='未登录'){
        $('#logout').html();
    }else{
        $('#logout').html('Signout');
    }

    $('#mblog').keyup(function () {
        if ($('#mblog').val().length > 150){
            $('#mblog').val().length = 150
        }
    });

    $("#testForm").submit(function () {
        if ($('#mblog').val().length == 0){
            alert('您还没有输入微博内容哦!');
            return false;
        }else{
            return true;
        }
    });
});