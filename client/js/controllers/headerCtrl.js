app.controller('headerCtrl', ['appService', '$scope', 'jsonService', 'user', function (appService, $scope, jsonService, user) {

    //$scope.loginText = "Login";
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

    $scope.isAuthenticated = function () {
        return user.isLoggedIn();
    };

    $scope.logout = function () {
        user.logout();
        appService.$location.url("/login")
    };

}]);
