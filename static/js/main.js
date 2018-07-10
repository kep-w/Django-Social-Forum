$(function () {
    var status = false;
    var username = $('#username').val();
    if ($("#welcome").html()=='未登录'){
            $('#logout').html();
        }else{
            $('#logout').html('Signout');
        }
    $('.agree').click(function () {
            var that = $(this);
            var msg_id = $(this).parent().find(".msg_id").val();
            $.ajax({
                url:'/user/deal',
                data:{'type':'agree','username':username,'msg_id':msg_id},
                type:'post',
                datatype:'json',
                success:function (data) {
                    var data = JSON.parse(data);
                    console.log(data);
                    if (data.resp == 'ok') {
                        var target = that.find('.num');
                        var num = Number(target.text()) + 1;
                        target.text(num);
                    }else{
                        alert('这是您点过的消息哦!')
                    }
                },
                error:function (error) {
                    // status = false;
                    console.log('错误信息:'+error);
                }
            })
    });
    $('.transpond').click(function () {
        var that = $(this);
        var msg_id = that.parent().find(".msg_id").val();
        $.ajax({
            url:'/user/deal',
            data:{'type':'transpond','username':username,'msg_id':msg_id},
            type:'post',
            datatype:'json',
            success:function (data) {
                var data = JSON.parse(data);
                if (data.resp == 'ok') {
                    var target = that.find('.num');
                    var num = Number(target.text()) + 1;
                    target.text(num);
                    location.reload()
                }else{
                    alert('您已经发过这条消息咯!')
                }
            },
            error:function (error) {
                console.log('错误信息:'+error)
            }
        })
    });
    $('.comment').click(function () {
        var that = $(this);
        var msg_id = that.parent().find(".msg_id").val();
        var com = prompt('输入评论内容:')
        if (com) {
            $.ajax({
                url: '/user/deal',
                data: {'type': 'comment', 'username': username, 'msg_id': msg_id, 'comment_content':com},
                type: 'post',
                datatype: 'json',
                success: function (data) {
                    var target = that.find('.num');
                    var num = Number(target.text()) + 1;
                    target.text(num);
                    alert('评论成功!')
                },
                error: function (error) {
                    console.log('错误信息:' + error);
                }
            })
        }
    });
    $('#welcome').click(function () {
        if ($("#welcome").html()=='未登录'){
            location.href = '/user/login/';
        }else{
            location.href='/';
        }
    });
    $('#logout').click(function () {
        if ($(this).text() == 'Signout'){
            // setCookie('user','');
            $.ajax({
                url:'/user/del',
                data:{'type':'delSession','username': username},
                type:'post',
                datatype:'json',
                success:function (data) {
                    location.href = '/user/login/';
                },
                error:function (data) {
                    console.log('错误信息',data.msg)
                }
            })
        }
    });
    $('.msg').click(function () {
        var msg_id = $(this).parent().parent().find(".msg_id").val();
        $.ajax({
                url:'/user/detail/',
                data:{'type':'details','username': username, 'msg_id': msg_id,},
                type:'post',
                datatype:'json',
                success:function (data) {
                    location.href = '/user/detail/';
                },
                error:function (data) {
                    console.log('错误信息',data.msg)
                }
            })
    });
});