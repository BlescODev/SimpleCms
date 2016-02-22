app.service('jsonService', ['appService', '$http', '$q', function(appService, $http, $q){

    var navigationPromise;
    var contentPromise;

    var retrieveJson = function (contentName, promise) {
        appService.http("GET", appService.get("location") + 'page/' + contentName, {}, function (response) {
            promise.resolve(response);
        }, function (response) {
            promise.reject(response);
        });
    };

    return {
        getNavData: function () {
            navigationPromise = $q.defer();
            retrieveJson("navigation", navigationPromise);
            return navigationPromise.promise;
        },
        getContent: function (contentName) {
            contentPromise = $q.defer();
            retrieveJson(contentName, contentPromise);
            return contentPromise.promise;
        }
    }
}]);