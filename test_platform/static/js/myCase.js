// 获取项目列表
var ProjectInit = function (_cmbProject) {
    // 通过标签的id，获取到
    var cmbProject = document.getElementById(_cmbProject)

    //创建下拉选项
    function cmbAddOption(cmb, obj) {
        console.log(obj)
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = obj.name;
        option.value = obj.id;
    }

    //定义一个方法，获取项目列表
    function getProjectListInfo() {
        // 获取某个用例的信息
        // resp：调用/project/get_project_list/这个接口，得到的返回值对象
        $.get("/project/get_project_list/", {}, function (resp) {
            // status：是views中返回的
            if (resp.status == 10200) {
                // 在html页面的console中打印
                // data：是views中返回的
                console.log(resp.data);
                var dataList = resp.data;
                // 遍历项目列表resp.data
                for (var i = 0; dataList.length; i++) {
                    cmbAddOption(cmbProject, dataList[i])
                }
            } else {
                window.alert(resp.message);
            }
        });
    }

    // 调用getCaseListInfo函数
    getProjectListInfo();

};