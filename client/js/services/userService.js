app.service('user', ['appService', '$q', '$auth', function (appService, $q, $auth) {

    $auth.setStorageType('localStorage');

    return {
        login: function (loginInfo) {
            return $auth.login(loginInfo);
        },
        logout: function () {
            $auth.logout();
        },
        isLoggedIn: function () {
            return  $auth.isAuthenticated();
        }
    }

}]);
