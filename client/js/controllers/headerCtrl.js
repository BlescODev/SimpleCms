app.controller('headerCtrl', ['appService', '$scope', 'jsonService', 'user', function (appService, $scope, jsonService, user) {

    //$scope.loginText = "Login";
    $scope.scrolled = false;

    var init = function () {
        jsonService.getNavData().then(function (response) {
            $scope.navElements = response.data;
        }, function (response) {

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
