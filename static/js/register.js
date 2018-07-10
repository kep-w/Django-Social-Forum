$(function () {
    var status = 0;
    $('#submit').submit(function () {
        return !!status;
    });
    $('input[name=uname]').keyup(function () {
        var r = new RegExp("[\\u4E00-\\u9FFF]+","g");
        if (r.test($(this).val())){
            status = 0;
            $('.tip').html('用户名不能包含中文字符')
        }else{
            status = 1;
        }
    })
});