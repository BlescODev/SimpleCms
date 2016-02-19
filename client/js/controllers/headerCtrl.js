app.controller('headerCtrl', ['appService', '$scope', 'jsonService', function (appService, $scope, jsonService) {

    $scope.scrolled = false;

    var init = function () {
        jsonService.getNavData().then(function (navData) {
            $scope.navElements = navData;
        }, function (errorMsg) {
            console.error(errorMsg);
        });
    };

    appService.ready(init);

    window.addEventListener('scroll', function (e) {
        $scope.scrolled = window.pageYOffset != 0;
        $scope.$apply();
    });

}]);
