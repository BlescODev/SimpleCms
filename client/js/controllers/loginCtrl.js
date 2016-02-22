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

        $scope.messages = [];

        $scope.errors.username = (!$scope.loginInfo.username);
        $scope.errors.password = (!$scope.loginInfo.password);

        if($scope.loginInfo.username && $scope.loginInfo.password){
            user.login($scope.loginInfo).then(function (response) {
                $scope.loginInfo = {};

                appService.notifications.queue({
                    message: "Successfully logged in!",
                    type: "success",
                    time: 3000
                });

                appService.$location.url('/');

            }).catch(function (response) {
                $scope.errors.username = true;
                $scope.errors.password = true;

                $scope.messages = [];

                if(response.status == 401){
                    $scope.messages.push({
                        type: "error",
                        message: "Username or password is wrong!"
                    });
                } else {
                    $scope.messages.push({
                        type: "error",
                        message: "The Server seems to be unavailable!"
                    });
                }
            });
        } else {
            $scope.messages.push({
                type: "error",
                message: "Please enter all information!"
            });
        }

        // ThisIsAnInsecurePassword;ItMustBeReplaced

    };

    $scope.reset = function () {
        $scope.messages = [];
        $scope.loginInfo = {};
        $scope.errors = {
            username: false,
            password: false
        };
    };

}]);
