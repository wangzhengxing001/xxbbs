var lay_alert = {
    "success":function(data){
        layer.msg(data["message"], {
            icon: 1,
         });
    },
    "param_error":function (data) {
        layer.msg(data["message"], {
            icon: 2,
            btnAlign: 'c',
            time:20000,
            btn:["确定"],
         });
    }
}