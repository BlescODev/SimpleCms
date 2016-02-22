app.service('user', ['appService', '$q', '$auth', function (appService, $q, $auth) {

    $auth.setStorageType('localStorage');

    return {
        login: function (loginInfo) {
            return $auth.login(loginInfo);
        },
        logout: function () {
            $auth.logout();
            if(!$auth.isAuthenticated()){
                appService.notifications.queue({
                    message: "Successfully logged out!",
                    type: "success",
                    time: 3000
                });
            }
        },
        isLoggedIn: function () {
            return  $auth.isAuthenticated();
        }
    }

}]);
