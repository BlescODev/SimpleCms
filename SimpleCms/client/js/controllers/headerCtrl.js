app.controller('headerCtrl', ['appService', '$scope', 'jsonService', function (appService, $scope, jsonService) {

    var init = function () {
        jsonService.getNavData().then(function (navData) {
            $scope.navElements = navData;
        }, function (errorMsg) {
            console.error(errorMsg);
        });
    };

    appService.ready(init);

}]);
