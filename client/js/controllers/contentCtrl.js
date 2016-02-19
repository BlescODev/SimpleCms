app.controller('contentCtrl', ['appService', 'jsonService', '$scope', function(appService, jsonService, $scope){

    var init = function () {
        var url = appService.$location.url();

        if (!url || url == '/') {
            url = appService.get('main');
        }
	
	    url = url.substr(1);

        jsonService.getContent(url).then(function (data) {
            $scope.posts = data;
        }, function (errorMsg) {
            console.error(errorMsg);
        });
    };

    appService.ready(init);

}]);
