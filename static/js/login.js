/**
 * Created by tarena on 18-7-4.
 */
$(function () {
    $('#sbm').submit(function () {
        var name = $('[name=name]').val();
        var pwd = $('[name=pwd]').val();
        if (name.length>3 && name.length<9){
            return pwd.length > 6 && pwd.length < 12;
        }else{
            return false;
            }
        })
});
