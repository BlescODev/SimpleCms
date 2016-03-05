app.controller('headerCtrl', ['appService', '$scope', 'pageService', 'user', function (appService, $scope, pageService, user) {

    //$scope.loginText = "Login";
    $scope.scrolled = false;

    var init = function () {
        pageService.get(appService.get('navigation').substr(1)).then(function (response) {
            $scope.navigation = response.data.content;
        }, function (response) {
            appService.notifications.queue({
                message: "Unable to retrieve navigation data!",
                type: "error"
            });
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
