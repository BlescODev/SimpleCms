app.controller('contentCtrl', ['appService', 'jsonService', '$scope', '$routeParams', function(appService, jsonService, $scope, $routeParams){

    var init = function () {
        var contentName = "";

        if ($routeParams.content) {
            contentName = $routeParams.content;
        }
        else {
        	contentName = appService.get('main')
        }

        jsonService.getContent(contentName).then(function (data) {
            $scope.posts = data;
        }, function (errorMsg) {
            console.error(errorMsg);
        });
    };

    appService.ready(init);

}]);