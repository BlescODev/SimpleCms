app.service('settingsService', ['appService', '$http', '$q', function(appService, $http, $q){

    var navigationPromise;
    var contentPromise;

    var get = function (setting, promise) {
        appService.http("GET", appService.get("location") + 'settings/' + setting, {}, function (response) {
            promise.resolve(response);
        }, function (response) {
            promise.reject(response);
        });
    };

    var update = function (setting, promise) {
        appService.http("POST", appService.get("location") + 'settings/' + setting.name, setting.settings, function (response) {
            promise.resolve(response);
        }, function (response) {
            promise.reject(response);
        });
    };

    return {
        get: function (setting) {
            contentPromise = $q.defer();
            get(setting, contentPromise);
            return contentPromise.promise;
        },
        update: function (setting) {
            contentPromise = $q.defer();
            update(setting, contentPromise);
            return contentPromise.promise;
        },
    }
}]);
