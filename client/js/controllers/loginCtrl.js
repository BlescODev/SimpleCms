app.controller('loginCtrl', ['appService', 'user', '$scope', function (appService, user,  $scope) {

    $scope.loginInfo = {
        username: "",
        password: ""
    };

    $scope.errors = {
        username: false,
        password: false
    };

    $scope.messages = [];

    $scope.login = function () {

        $scope.errors.username = (!$scope.loginInfo.username);
        $scope.errors.password = (!$scope.loginInfo.password);

        if($scope.loginInfo.username && $scope.loginInfo.password){
            user.login($scope.loginInfo).then(function (response) {
                $scope.loginInfo = {};

                appService.$location.url('/');

            }).catch(function (response) {
                $scope.error.username = true;
                $scope.error.password = true;

                $scope.messages.push({
                    type: "error",
                    message: "Failed to login!"
                })
            });
        }

    };

    $scope.reset = function () {
        $scope.loginInfo = {};
        $scope.errors = {
            username: false,
            password: false
        };
    };

}]);
