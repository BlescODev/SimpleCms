app.controller('navigationCtrl', ['appService', '$scope', 'pageService', 'user', function (appService, $scope, pageService, user) {

    //$scope.loginText = "Login";
    $scope.scrolled = false;

    var init = function () {
	navigation = appService.get('navigation').substr(1)
        pageService.get(navigation).then(function (response) {
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

/*

<li>
<a>SimpleCms</a>
<ul>
<li ng-if="isAuthenticated()">
<a href="#/edit{{route}}">Edit this Page</a>
</li>
<li ng-if="isAuthenticated()">
<a href="/pages/">Pages</a>
</li>
<li ng-if="isAuthenticated()">
<a href="#/settings">Settings</a>
</li>
<li ng-if="!isAuthenticated()">
<a href="#/login">Login</a>
</li>
<li ng-if="isAuthenticated()">
<a ng-click="logout()">Logout</a>
</li>
</ul>
</li>

*/
