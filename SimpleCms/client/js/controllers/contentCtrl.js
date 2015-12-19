app.controller('contentCtrl', ['appService', 'jsonService', '$scope', '$routeParams', function(appService, jsonService, $scope, $routeParams){

    var init = function () {
        var contentName = "";

        if($routeParams.subcontent && $routeParams.content){
            contentName = $routeParams.content + '/' + $routeParams.subcontent;
        } else if ($routeParams.content) {
            contentName = $routeParams.content + '/' + $routeParams.content;
        }

        jsonService.getContent(contentName).then(function (data) {
            $scope.posts = data;
        }, function (errorMsg) {
            console.error(errorMsg);
        });
    };

    appService.ready(init);

}]);