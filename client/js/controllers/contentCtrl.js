app.controller('contentCtrl', ['appService', 'pageService', '$scope', function(appService, pageService, $scope){

    var init = function () {
        var url = appService.$location.url();

        if (!url || url == '/') {
            url = appService.get('main');
        }

        url = url.substr(1);

        pageService.get(url).then(function (response) {
            $scope.page = response.data;
        }, function (response) {
            if(response.status == 404){
                appService.$location.url('/404');
            } else if (response.status == 500) {
                appService.notifications.queue({
                    message: "The server is experiencing some problems at the moment. Sorry!",
                    type: "error"
                });
            }
        });
    };

    appService.ready(init);

}]);
