app.controller('loginCtrl', ['appService', 'user', '$scope', function (appService, user,  $scope) {

    $scope.loginInfo = {
        username: "",
        password: ""
    };

    $scope.errors = {
        username: false,
        password: false
    };

    $scope.login = function () {

        $scope.errors.username = (!$scope.loginInfo.username);
        $scope.errors.password = (!$scope.loginInfo.password);

        if($scope.loginInfo.username && $scope.loginInfo.password){
            user.login($scope.loginInfo);
        }

    };

    $scope.reset = function () {
        $scope.loginInfo = {
            username: "",
            password: ""
        };
        $scope.errors = {
            username: false,
            password: false
        };
    };

}]);
