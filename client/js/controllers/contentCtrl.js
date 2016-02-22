app.controller('contentCtrl', ['appService', 'jsonService', '$scope', function(appService, jsonService, $scope){

    var init = function () {
        var url = appService.$location.url();

        if (!url || url == '/') {
            url = appService.get('main');
        }
	
	    url = url.substr(1);

        jsonService.getContent(url).then(function (response) {
            $scope.posts = response.data;
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
