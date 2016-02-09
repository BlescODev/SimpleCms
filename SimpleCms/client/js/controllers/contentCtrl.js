app.controller('contentCtrl', ['appService', 'jsonService', '$scope', '$location', function(appService, jsonService, $scope, $location){

    var init = function () {
        var url = $location.url()

	console.log(url)

        if (!url || url == '/') {
            url = appService.get('main')
        }
	
	url = url.substr(1)

        jsonService.getContent(url).then(function (data) {
            $scope.posts = data;
        }, function (errorMsg) {
            console.error(errorMsg);
        });
    };

    appService.ready(init);

}]);
