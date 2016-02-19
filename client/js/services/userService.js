app.service('user', ['appService', '$q', function (appService, $q) {


    var checkIfLoggedIn = function () {
        var loggedInPromise = $q.defer();
        appService.http("", {}, function (response) {
            loggedInPromise.resolve(response);
        }, function (response) {
            loggedInPromise.reject(response);
        });
        return loggedInPromise.promise;
    };


    return {
        login: function (loginInfo) {
            var loginPromise = $q.defer();

            appService.http(appService.get("blesc") + '/auth', loginInfo, function (response) {
                console.log(response);
                loginPromise.resolve(response);
            }, function (response) {
                console.log(response);
                loginPromise.reject(response);
            });

            return loginPromise.promise;
        },
        logout: function () {
            
        },
        isLoggedIn: function () {
            return checkIfLoggedIn();
        }
    }

}]);
