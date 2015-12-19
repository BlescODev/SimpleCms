app.service('jsonService', ['appService', '$http', '$q', function(appService, $http, $q){

    var navigationPromise;
    var contentPromise;

    var retrieveJson = function (contentName, promise) {
        $http.get(appService.get("location")+ 'page/'+ contentName)
            .success(function (data) {
                promise.resolve(data);
            })
            .error(function () {
                promise.reject('failed to load the json for ' + contentName);
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